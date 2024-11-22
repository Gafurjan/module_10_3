import threading
import random
import time

lock = threading.Lock()
x = 0
class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        
    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                if self.balance + amount <= 500:
                    self.balance += amount
                    print(f"\rПополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            request = random.randint(50, 500)
            print(f"\rЗапрос на {request}")
            with self.lock:
                if request > self.balance:
                    print("Запрос отклонён, недостаточно средств")
                else:
                    self.balance -= request
                    print(f"Снятие: {request}. Баланс: {self.balance}")
            time.sleep(0.001)

bk = Bank()

# Т.К. Методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')









