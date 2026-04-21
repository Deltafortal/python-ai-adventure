from core.models import Player, Skill
from core.combat import CombatManager


class GameEngine:

    def __init__(self, provider, ui_manager):
        self.provider = provider
        self.ui = ui_manager
        self.current_node_id = self.provider.get_start_node()
        self.is_running = True
        
        # Story Memory
        self.story_history = [] 
        
        self.combat_manager = CombatManager()
        basic_attack = Skill(name="Strike", description="A basic melee attack", type="damage", duration=0, power=10)
        self.player = Player(name="Hero", hp=50, skills=[basic_attack])




    def run(self):

        while self.is_running:
            node = self.provider.get_node(self.current_node_id, self.player.lore, self.story_history)
            
            if not node:
                self.ui.display_text(f"Error: Node '{self.current_node_id}' not found.")
                break

            self.ui.display_text(node['text'])
            
            self.story_history.append(node['text'])
            if len(self.story_history) > 10:  # Limit history to last 10 entries
                self.story_history.pop(0)

            self.process_actions(node['actions'])



    def process_actions(self, actions):

        for action in actions:
            action_type = action['type']

            if action_type == 'input':
                user_text = self.ui.get_text_input("Write your background here:")


                # Save player lore
                if action['save_as'] == 'player_lore':
                    self.player.lore = user_text
                    self.ui.display_text(f"[SYSTEM: Lore saved! Welcome, {self.player.name}.]")
                self.current_node_id = action['target']


            # --- CHOICE ACTION ---
            elif action_type == 'choice':
                next_node = self.ui.get_choice(action['options'])
                self.current_node_id = next_node
                break 

            
            # --- GOTO ACTION ---
            elif action_type == 'goto':
                input("\n[Press ENTER to continue...]")
                self.current_node_id = action['target']
                break


            # --- COMBAT ACTION ---
            elif action_type == 'combat':
                victory = self.combat_manager.start_combat(self.player, action['enemies'], self.ui)
                if victory:
                    self.current_node_id = action['on_victory']
                    self.story_history.append("The player has just won a bloody battle.")
                else:
                    self.current_node_id = action['on_defeat']
                break



            # --- END GAME ACTION ---
            elif action_type == 'end_game':
                self.is_running = False
                self.ui.display_text("\n--- END OF THE ADVENTURE ---\n")
                break