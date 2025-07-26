# 💰 Bank Simulator

#### 🎥 Video Demo: [Watch Here](https://youtu.be/_ArAqpmJsOk)

---

## 📖 Description

The **Bank Simulator** is a simple yet effective command-line Python application that mimics the basic functionality of a traditional bank. It allows users to perform common banking operations such as adding money, withdrawing funds, viewing current balance, and reviewing their transaction history. All data is stored using standard `.csv` files, providing a lightweight and accessible way to simulate real-world banking behavior without the complexity of databases or external dependencies.

This project serves as an excellent exercise for beginners learning Python. It offers hands-on experience with file handling, user input, data persistence, and displaying tabular data in the terminal. Users interact with the system through a text-based menu that clearly guides them through each operation.

By using this simulator, users can better understand how transactions are tracked, how balances are updated in real time, and how to manage simple financial records programmatically.

---

## 👤 My Details

| Field             | Details               |
|-------------------|-----------------------|
| **Project Title** | Bank Simulation       |
| **Author**        | Abhishek Bansal       |
| **GitHub**        | [abhi280107](https://github.com/abhi280107) |
| **EdX ID**        | abhibansal2801        |
| **City**          | Ahmedabad             |
| **Country**       | India                 |
| **Date**          | 08-Jul-25             |

---

## 🌟 Key Features

- 💵 **Add Balance**: Users can deposit money into their virtual account. The amount is added to the balance and logged in the transaction history.
- 🧾 **Withdraw Funds**: Users can withdraw funds as long as they have sufficient balance. If not, the system notifies them and prevents the transaction.
- 📊 **View Balance**: Quickly view the current balance in your account with a single command.
- 📁 **Transaction History**: All actions are recorded with a timestamp and displayed in a clean table using the `tabulate` module.
- 🧭 **Interactive CLI**: A command-driven interface that continuously prompts users to take action until they choose to exit.

---

## 📂 File Structure

The following files are essential for the program to run:

- `project.py` – Main Python script containing all functionality and user interface.
- `balance.csv` – Stores the current balance in the format: `Balance,<amount>`.
- `transaction history.csv` – Logs each transaction in the format: `Action,Amount,Date,Time`.
- `_.csv` – Contains the menu/instructions shown to users during each loop iteration.

Each file plays a specific role in ensuring that the banking experience is smooth, and that no data is lost between sessions.

---

## 📦 Required Modules

Make sure you have the following Python modules installed:

- `tabulate` – For displaying formatted tables in the terminal.
- `datetime` – For capturing and formatting dates and times for transactions.

To install tabulate, run:

```bash
pip install tabulate
```
## 🚀 How to Run the Project
1. Place all required files `project.py`, `balance.csv`, `transaction history.csv`, `_.csv` into the same folder
2. Open a terminal or command prompt in that folder.
3. Run the application by typing:
```bash
python project.py
```
4. Follow on-screen instructions using the command options displayed.

All commands:

Press `A` to Add Balance

Press `W` to Withdraw

Press `V` to View Balance

Press `L` to view Last Transactions

Press `X` to Exit

## Thanks To CS50P Authors:
This was my final project for CS50P which provided me with a opportunity to learn CS50P and I am very greatful to the authors