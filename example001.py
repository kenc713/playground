def greet(name):
    print(f"Hello, {name}! How are you?")

def add(a, b):
    return a + b

def multiply(a, b):
    # かけ算の結果を文字列にする
    return str(a * b)

if __name__ == "__main__":
    greet("Alice")
    print("Sum:", add(10, 5))  # 数値を変更
    print("Product:", multiply(2, 3))
