# syntax_error_example.py

def greet(name):
    # コロン(:)が抜けている → SyntaxError
    print("Hello, " + name)

# 不正なインデント
print("This line is incorrectly indented")

# 不正な文字列
text = "Hello world  # クオートが閉じていない → SyntaxError

# 関数呼び出しの括弧ミス
greet("Alice"