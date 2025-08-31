def greet(name):
    print(f"Hello, {name}! How are you?")  # 同じ行を変更

def add(a, b):
    return a + b + 2  # 同じ行を変更

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    greet("Alice")
    print("Sum:", add(2, 3))
    print("Product:", multiply(2, 3))
