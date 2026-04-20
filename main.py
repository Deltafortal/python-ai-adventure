from providers.local_json import LocalJSONProvider
from ui.ui_manager import ConsoleUIManager
from core.engine import GameEngine


def main():
    provider = LocalJSONProvider("data/test_story.json")
    ui_manager = ConsoleUIManager()
    

    engine = GameEngine(provider, ui_manager)
    engine.run()


if __name__ == "__main__":
    main()