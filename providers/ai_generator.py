import json
import ollama


class AIGeneratorProvider:


    def __init__(self, model_name="llama3", bestiary_path="data/enemies.json"):
        self.model_name = model_name

        with open(bestiary_path, 'r', encoding='utf-8') as f:
            bestiary = json.load(f)
            self.available_enemies = list(bestiary.keys())



    def _get_system_prompt(self):
        enemies_list = ", ".join(self.available_enemies)
        
        return f"""
        You are the DUNGEON MASTER of a text-based RPG.
        You must respond ONLY with a valid JSON object. No markdown or extra text.

        RULES:
        - Continue the story in a logical manner based on previous events.
        - If there was just a combat, describe the corpses and loot.
        - The 'actions' array must contain EXACTLY ONE action object (either a choice or a combat). Never put two together.

        JSON SCHEMA TO FOLLOW:
        {{
          "text": "The description of the current scene (max 4 sentences).",
          "actions": [
             // INSERT ONE ACTION OBJECT HERE BETWEEN THESE TWO:
             // OPTION A (Choice): {{ "type": "choice", "options": [{{ "label": "Go north", "target": "invented_node_1" }}, {{ "label": "Explore", "target": "invented_node_2" }}] }}
             // OPTION B (Combat): {{ "type": "combat", "enemies": [{{ "id": "goblin_warrior", "quantity": 1 }}], "on_victory": "victory_id", "on_defeat": "game_over" }}
          ]
        }}
        
        CONSENTED ENEMIES (if choosing combat): {enemies_list}.
        """



    def get_start_node(self):
        return "character_creation"


    def get_node(self, node_id, player_lore="", history=None):
        if history is None:
            history = []

        if node_id == "character_creation":
            return {
                "text": "Welcome, adventurer. Before we begin, tell me: what is your background, your personality, and what are your ideals?",
                "actions": [{"type": "input", "save_as": "player_lore", "target": "ai_start_01"}]
            }
        elif node_id == "game_over":
            return {
                "text": "Your adventure ends here...",
                "actions": [{"type": "end_game"}]
            }



        print(f"\n[AI is writing the node: '{node_id}'...]")
        


        # Buid prompt
        user_content = f"Background of the player: {player_lore}\n\n"
        if history:
            user_content += "RECENT EVENTS IN THE STORY:\n"
            for past_event in history:
                user_content += f"- {past_event}\n"
        
        user_content += f"\nGenerate the next node (ID: '{node_id}') continuing from these events."


        try:

            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {'role': 'system', 'content': self._get_system_prompt()},
                    {'role': 'user', 'content': user_content}
                ],
                format='json'
            )
            return json.loads(response['message']['content'])
        
        except Exception as e:
            print(f"[AI ERROR]: {e}")
            return {
                "text": "The fabric of space-time vibrates intensely (AI Error).",
                "actions": [{"type": "choice", "options": [{"label": "Advance cautiously", "target": node_id}]}]
            }