# tasks/task5.py

def solve():




    s = int(input())
    h = s // 3600
    s %= 3600
    m = s // 60
    sec = s % 60
    print(f"{h}:{m:02}:{sec:02}")
# Ниже пишите решение задачи


   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()