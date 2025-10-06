# tasks/task3.py

def solve():
    # tasks/task3.py

    n = int(input())
    d = [100, 20, 10, 5, 1]
    c = 0
    for x in d:
     c += n // x
     n %= x
    print(c)

# Ниже пишите решение задачи
    


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()