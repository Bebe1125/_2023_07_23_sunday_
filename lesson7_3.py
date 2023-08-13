import random #隨機亂數

#定義funtion
def play_game() -> None:  #def可把裡面重複執行的程式收合，畫面看起來較簡潔(-> None可以不用寫)
    min = 1
    max = 100
    target = random.randint(min,max) #設定亂數範圍
    print(target)  #作弊 先秀出答案
    count = 0  #猜了幾次
    print("============猜數字遊戲============\n\n")  # \n 斷行
    while True:  #馬上進入迴圈
        keyin = int(input(f"猜數字範圍{min}~{max}:"))
        count += 1
        if keyin >= min and keyin <= max:
            if(keyin == target):
                print(f"賓果!猜對了,答案是:{target}")
                print(f"您猜了{count}次")
                break
            elif keyin > target:
                print("再小一點")
                max = keyin - 1
                
            elif keyin < target:
                print("再大一點")
                min = keyin + 1
            
            print(f"您已經猜了{count}次")
        else:
            print("請輸入提示範圍內的數字")

while True:
    #呼叫funtion
    play_game()
    play_again = input("還要繼續嗎?(y,n)") #猜對後，詢問要不要再玩
    if play_again == "n":
        break
print("遊戲結束")
