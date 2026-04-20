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
        Sei il Dungeon Master di un'avventura testuale RPG.
        Rispondi sempre e solo in formato JSON valido. 
        Non usare markdown (niente ```json).

        REGOLE DI NARRAZIONE:
        - Crea una storia coerente con il background del personaggio.
        - Se il giocatore ha appena vinto un combattimento, descrivi le conseguenze.
        - Aggiungi un combattimento ogni 3-10 nodi, bilanciando la difficoltà in base alla progressione del giocatore.
        - Non ripetere mai lo stesso nemico più di 3 volte.
        - Non creare incongruenze narrativa
        - Utilizza un linguaggio evocativo e coinvolgente, adatto a un'avventura fantasy.
        - Non rivelare mai dettagli tecnici o meccaniche di gioco al giocatore.
        - Crea una storia di crescente ritmo, complessità e tensione, con momenti di respiro narrativo.
        - Basati su archetipi narrativi classici (eroe, mentore, sfida, ricompensa, tradimento, ecc.) per costruire la trama.
        - Sfrutta elementi di worldbuilding per rendere il mondo di gioco più immersivo e credibile, ma senza appesantire la narrazione.
        - Basati su libri, film e giochi fantasy classici per ispirarti, ma crea sempre qualcosa di originale e sorprendente.
        - Termina l'avventura con un climax narrativo soddisfacente, che risolva le principali tensioni e domande poste durante.
        - Ogni nodo deve avere un filo conduttore a quello precedente, creando una narrazione fluida e coerente.
        - Aggiungi il nodo type "end_game" solo quando la storia raggiunge una conclusione naturale, evitando di forzare finali prematuri o insoddisfacenti e MAI prima di 10 nodi.

        SCHEMA JSON OBBLIGATORIO:
        {{
          "text": "Descrizione narrativa (max 5 frasi)",
          "actions": [
             {{ "type": "choice", "options": [{{ "label": "...", "target": "..." }}] }},
             {{ "type": "combat", "enemies": [{{ "id": "...", "quantity": 1 }}], "on_victory": "...", "on_defeat": "game_over" }},
             {{ "type": "end_game" }}
          ]
        }}
        
        LIMITAZIONI NEMICI:
        Puoi usare SOLO questi ID nemico: {enemies_list}.
        """


    def get_start_node(self):
        # TODO: ADD DYNAMIC CHARACTER
        return "character_creation"



    def get_node(self, node_id, player_lore=""):

        # Add Fixed systems nodes
        if node_id == "character_creation":
            return {
                "text": "Benvenuto avventuriero. Prima di iniziare, dimmi: qual è il tuo background, il tuo carattere e quali sono i tuoi ideali?",
                "actions": [{"type": "input", "save_as": "player_lore", "target": "ai_start_01"}]
            }
        elif node_id == "game_over":
            return {
                "text": "La tua avventura finisce qui...",
                "actions": [{"type": "end_game"}]
            }




        # --- AI CALL ---
        print(f"\n[L'AI sta scrivendo il nodo '{node_id}'...]")
        
        user_content = f"Genera il nodo '{node_id}'. "
        if player_lore:
            user_content += f" Background giocatore: {player_lore}."

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
                "text": "C'è stato un errore nella creazione della realtà.",
                "actions": [{"type": "choice", "options": [{"label": "Riprova", "target": node_id}]}]
            }