# Life Game Simulator

A turn-based ecosystem simulation developed in Python, focusing on Object-Oriented Programming (OOP) principles and dynamic interactions between biological entities.

---

## Tech Stack
* **Language:** Python 3.x
* **GUI Framework:** PyQt6
* **Architecture:** Object-Oriented Programming (Inheritance, Polymorphism, Abstract Classes)
* **Persistence:** Custom file-based Save/Load system

---

## Core Features
* **Advanced Organism Hierarchy:** Implementation of a base `Organism` abstract class with specialized `Animal` and `Plant` subclasses.
* **Complex Interactions:** Each entity possesses unique behaviors (e.g., `PineBorscht` killing nearby animals, `Antelope` having a 50% chance to escape combat).
* **Dynamic World Management:** A grid-based world system that handles movement, collision detection, and turn-order based on initiative.
* **Save/Load System:** State serialization to `.txt` files, allowing sessions to be resumed.
* **Event Logging:** Real-time GUI notifications about interactions (e.g., "Antylopa udało się uciec").

---

## Engineering Logic
The simulation follows a strict initiative-based execution order. The survival of an organism during a collision is determined by the strength parameter S:

**Collision Result:** If Organism A attacks Organism B:
Winner = A if S_A ≥ S_B else B
(Special conditions like escape probability P = 0.5 apply for specific classes).

---

## Installation & Usage (Windows)
**Note:** This application was developed and tested on Windows. Cross-platform compatibility (Linux/macOS) has not been verified.
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/life-game-py.git
   cd life-game-py

2. **Set up virtual environment (Recommended)**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the application:**
   ```bash
   python main.py
