from collections import deque

def is_palindrome(s):
    # Видаляємо пробіли та перетворюємо рядок на нижній регістр
    s = ''.join(s.split()).lower()
    d = deque(s)
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

print(is_palindrome("A man a plan a canal Panama"))  # True
