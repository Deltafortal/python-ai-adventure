import json
from core.models import Enemy


class CombatManager:

    def __init__(self, bestiary_path="data/enemies.json"):
        with open(bestiary_path, 'r', encoding='utf-8') as f:
            self.bestiary = json.load(f)


    def start_combat(self, player, enemies_data, ui):

        # Start enemies
        enemies = []
        for enemy_record in enemies_data:
            e_id = enemy_record['id']
            qty = enemy_record['quantity']
            stats = self.bestiary.get(e_id)
            
            if not stats:
                ui.display_text(f"[ERROR] Enemy '{e_id}' not found in bestiary.")
                continue
            
            for i in range(qty):
                # Add enemies with unique names
                name = f"{stats['name']} {i+1}" if qty > 1 else stats['name']
                enemy = Enemy(entity_id=e_id, name=name, hp=stats['hp'], skills=[])
                enemies.append(enemy)



        # Combat Loop
        ui.display_text("\n⚔️ BATTLE START! ⚔️")
        round_num = 1
        
        while player.is_alive and any(e.is_alive for e in enemies):
            ui.display_text(f"\n=== ROUND {round_num} ===")
            ui.display_text(f"{player.name} HP: {player.current_hp}/{player.max_hp}")
            
            
            # --- PLAYER TURN ---
            alive_enemies = [e for e in enemies if e.is_alive]
            
            ui.display_text("Choose your target:")
            options = [{"label": f"{e.name} (HP: {e.current_hp}/{e.max_hp})", "target": e} for e in alive_enemies]
            
            target = ui.get_choice(options)
            
            # TODO: ADD SKILL CHOICE !!!!!
            skill = player.skills[0]
            ui.display_text(f"\n> You used {skill.name} on {target.name} for {skill.power} damage!")
            target.take_damage(skill.power)
            
            if not target.is_alive:
                ui.display_text(f"💀 {target.name} has been defeated!")



            # --- ENEMIES TURN ---
            alive_enemies = [e for e in enemies if e.is_alive]

            for enemy in alive_enemies:
                # TODO: ADD DYNAMIC DAMAGE
                enemy_dmg = 5 
                ui.display_text(f"> {enemy.name} attacks you for {enemy_dmg} damage!")
                player.take_damage(enemy_dmg)
                
                if not player.is_alive:
                    break
                    
            round_num += 1



        # End combat
        if player.is_alive:
            ui.display_text("\n🏆 VICTORY! You have defeated all enemies!")
            return True
        else:
            ui.display_text("\n☠️ DEFEAT... You have fallen in battle.")
            return False