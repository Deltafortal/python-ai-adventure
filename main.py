#from providers.local_json import LocalJSONProvider <-- Local Provider used for testing now replaced by AI
from providers.ai_generator import AIGeneratorProvider
from ui.ui_manager import ConsoleUIManager
from core.engine import GameEngine


def main():
    provider = AIGeneratorProvider(model_name="llama3")
    ui_manager = ConsoleUIManager()
    

    engine = GameEngine(provider, ui_manager)
    engine.run()


if __name__ == "__main__":
    main()