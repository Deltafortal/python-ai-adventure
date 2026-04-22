# 🐉 Python AI Adventure

An AI-powered, text-based RPG built with Python. This project uses a custom node-based state machine and local Large Language Models (LLMs) via Ollama to generate endless, context-aware adventures and turn-based combat encounters based on the player's background.

## ✨ Features

* **Dynamic AI Storytelling:** Uses Llama 3 to generate the narrative on the fly. The AI remembers recent events and adapts the story to the player's custom lore and background.
* **JSON-Driven State Machine:** The game engine operates on a state machine. The AI generates structured JSON outputs to create narration, choices, and combat triggers.
* **Turn-Based Combat System:** A fully integrated combat engine featuring dynamic enemies loaded from a local bestiary, player stats, and skill usage.
* **Modular Architecture:** Designed with scalability (Model-View-Controller inspired).


## 🚀 Prerequisites

Before you begin, ensure you have met the following requirements:
* **Python 3.8+** installed on your machine.
* **Ollama** installed and running on your system ([Download Ollama](https://ollama.com/)).
* At least 8GB of RAM if you want to keep the local LLM (16GB recommended).

## 🛠️ Installation & Setup

1. **Clone the repository:**

2. **Create and activate a virtual environment:**
   * **Windows:**
     \`\`\`bash
     python -m venv venv
     .\venv\Scripts\activate
     \`\`\`

3. **Install the required Python packages:**
   \`\`\`bash
   pip install ollama
   \`\`\`

4. **Download the AI Model:**
   Make sure Ollama is running, then pull the Llama 3 model (this is a one-time download of ~4.7GB):
   \`\`\`bash
   ollama run llama3
   \`\`\`
   *(Type `/bye` to exit the Ollama prompt once it's downloaded).*

## 🎮 How to Play

Run the main script from your terminal:
\`\`\`bash
python main.py
\`\`\`
1. Enter your character's background, personality, and ideals when prompted. The AI will use this as the foundation for your unique story.
2. Read the generated scenarios and type the number corresponding to your choice.
3. If a combat encounter is triggered, choose your targets and use your skills to survive!

## 🔮 Future Roadmap

* [ ] **Advanced RPG Mechanics:** Add an inventory system, consumables (e.g., healing potions), and a wider variety of skills.
* [ ] **Cloud Provider Integration:** Add an alternative provider to support OpenAI/Anthropic APIs alongside the local Ollama provider.
* [ ] **Add more enemies:** updgrade the list of the available enemies.
