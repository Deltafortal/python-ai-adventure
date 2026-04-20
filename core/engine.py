from core.models import Player

class GameEngine:
    def __init__(self, provider, ui_manager):
        self.provider = provider
        self.ui = ui_manager
        self.current_node_id = self.provider.get_start_node()
        self.is_running = True
        
        # Initialize Player
        self.player = Player(name="Eroe", hp=100, skills=[])




    def run(self):
        while self.is_running:
            node = self.provider.get_node(self.current_node_id)
            
            if not node:
                self.ui.display_text(f"Error: Node '{self.current_node_id}' not found.")
                break

            self.ui.display_text(node['text'])
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
                    #print(f"DEBUG LORE: {self.player.lore}")
                
                self.current_node_id = action['target']



            elif action_type == 'choice':
                next_node = self.ui.get_choice(action['options'])
                self.current_node_id = next_node



            elif action_type == 'goto':
                input("\n[Press ENTER to continue...]")
                self.current_node_id = action['target']



            elif action_type == 'combat':
                self.ui.display_text("⚔️ STARTING COMBAT!:")

                for enemy in action['enemies']:
                    self.ui.display_text(f"  - {enemy['quantity']}x {enemy['id'].replace('_', ' ').title()}")
                
                input("\n[Press ENTER to continue...]")
                self.ui.display_text("🏆 You have defeated the monsters!")
                self.current_node_id = action['on_victory']



            elif action_type == 'end_game':
                self.is_running = False
                self.ui.display_text("\n--- END OF THE ADVENTURE ---\n")