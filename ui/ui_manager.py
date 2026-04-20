class ConsoleUIManager:


    def display_text(self, text):
        print(f"\n{text}")


    def get_choice(self, options):
        for i, option in enumerate(options):
            print(f"{i + 1}. {option['label']}")
        
        while True:
            choice = input("\nChoose an option: ")
            if choice.isdigit():
                choice_index = int(choice) - 1
                if 0 <= choice_index < len(options):
                    return options[choice_index]['target']
            print("Invalid choice, please enter the correct number.")