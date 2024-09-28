import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request():
    request_id = random.randint(1000, 9999)
    print(f"Generated request with ID: {request_id}")
    request_queue.put(request_id)

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Processing request with ID: {request_id}")
    else:
        print("No requests to process")

# Головний цикл програми
def main():
    try:
        while True:
            generate_request()
            time.sleep(1)  # Імітація часу між генерацією заявок
            process_request()
            time.sleep(1)  # Імітація часу на обробку заявки
    except KeyboardInterrupt:
        print("Exiting program")

if __name__ == "__main__":
    main()
