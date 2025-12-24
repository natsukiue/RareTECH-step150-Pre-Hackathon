#ハッカソン事前入門テスト
#1番
print('hello world')

#2番
def greet(): #関数greet作成
    print('こんにちは')

greet()      #関数greet実行

#3番
def print_name(name):
    print(f"私の名前は{name}です")

name = input("名前を入力して下さい：")
print_name(name)

#4番
def get_greet():
    message = "おはようございます"
    return message  #文字列を返す
#関数を呼び出して結果を受け取る
result = get_greet()
print(result)

#5番
def add(a,b):
    return a + b
a = int(input("1つ目の数字を入力してください："))
b = int(input("２つ目の数字を入力してください："))

result = add(a,b)
print(result)
