# Python Account & Inventory Manager

A robust Python-based management system demonstrating **Object-Oriented Programming (OOP)** and **Data Persistence** through JSON.

## 🚀 Key Features
- **Account Management:** Create user profiles with starting balance and unique filenames.
- **Shopping Logic:** Buy items (Star, Shell, Block) with real-time balance and inventory slot validation.
- **Selling Mechanic:** Sell items back to the system with a 10% transaction fee.
- **Persistent Storage:** Full Save/Load functionality using `json` to keep player data across sessions.
- **Inventory System:** Built-in limits (max 5 slots) to simulate game mechanics.

## 🛠 Tech Stack
- **Language:** Python3
- **Storage Format:** JSON

## 🕹️ How to Use
1. Run the script: `python account.py`
2. Choose to **load** an existing profile or **create** a new one.
3. Use commands like `kaufen` (buy), `verkaufen` (sell), `status`, or `ausgeben` (save & exit).
