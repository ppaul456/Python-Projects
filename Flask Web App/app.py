from flask import Flask
app = Flask(__name__) # The module we are using (__name__)

@app.route("/") # 函式的裝飾 (Decorator): 以函式為基礎, 提供附加功能(/根目錄)
def home():
    return "Hello Flask"

@app.route("/test") # 函式的裝飾 (Decorator): 以函式為基礎, 提供附加功能(/test)
def test():
    return "Hello this is Flask testing"

if __name__ == "__main__":  # 如果以主程式執行(main)
    app.run()    # 啟動伺服器



