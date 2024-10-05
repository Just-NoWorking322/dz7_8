import sqlite3

conn = sqlite3.connect('bank_system.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    address TEXT NOT NULL,
                    email TEXT NOT NULL,
                    balance REAL DEFAULT 0)''')
conn.commit()

def create_account():
    name = input("Введите ваше имя: ")
    surname = input("Введите вашу фамилию: ")
    age = int(input("Введите ваш возраст: "))
    address = input("Введите ваш адрес: ")
    email = input("Введите ваш email: ")
    
    cursor.execute('''INSERT INTO accounts (name, surname, age, address, email)
                      VALUES (?, ?, ?, ?, ?)''', (name, surname, age, address, email))
    conn.commit()
    
    print(f"Счет создан. Ваш ID: {cursor.lastrowid}")

def deposit(account_id, amount):
    cursor.execute('SELECT balance FROM accounts WHERE id = ?', (account_id,))
    result = cursor.fetchone()
    
    if result is None:
        print("Счет не найден.")
    else:
        new_balance = result[0] + amount
        cursor.execute('UPDATE accounts SET balance = ? WHERE id = ?', (new_balance, account_id))
        conn.commit()
        print(f"Счет пополнен на {amount}. Новый баланс: {new_balance}")

def counting_error(account_id, amount):
    cursor.execute('SELECT balance FROM accounts WHERE id = ?', (account_id,))
    result = cursor.fetchone()
    
    if result is None:
        print("Счет не найден.")
    elif amount > result[0]:
        print("Недостаточно средств для снятия.")
    else:
        new_balance = result[0] - amount
        cursor.execute('UPDATE accounts SET balance = ? WHERE id = ?', (new_balance, account_id))
        conn.commit()
        print(f"Снято {amount}. Новый баланс: {new_balance}")

def check_balance(account_id):
    cursor.execute('SELECT balance FROM accounts WHERE id = ?', (account_id,))
    result = cursor.fetchone()
    
    if result is None:
        print("Счет не найден.")
    else:
        print(f"Текущий баланс: {result[0]}")

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Открыть счет")
        print("2. Пополнить счет")
        print("3. Снять средства")
        print("4. Проверить баланс")
        print("5. Выйти")
        
        choice = input("Введите номер действия: ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            account_id = int(input("Введите ID счета: "))
            amount = float(input("Введите сумму для пополнения: "))
            deposit(account_id, amount)
        elif choice == '3':
            account_id = int(input("Введите ID счета: "))
            amount = float(input("Введите сумму для снятия: "))
            counting_error(account_id, amount)
        elif choice == '4':
            account_id = int(input("Введите ID счета: "))
            check_balance(account_id)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()

conn.close()








"""Домашняя работа №7


Разработать программу для управления базой банковской системой.

Функциональные требования:

Открытие счета:

Пользователи могут открыть банковский счет, указав свои личные данные (имя, фамилия, возраст, адрес и email).
Каждый счет должен иметь уникальный номер (id).
Так же добавьте поле для хранения денег пользователя ( balance или wallet )

Пополнение и снятие средств:

Пользователи должны иметь возможность пополнять счет.
Пользователи должны иметь возможность снимать средства со своего счета.
Нельзя снимать сумму, превышающую текущий баланс.

Просмотр баланса:

Пользователи должны иметь возможность проверять текущий баланс своего счета."""


