a = [
    [1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],

]
start = 0, 1
end = 5, 6
a1 = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
]
start1 = 3, 0
end1 = 1, 6
a2 = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
]
start2 = 4, 1
end2 = 4, 5
m = []

class Stack:
    def __init__(self):
        self.item = []
    def push(self, item):
        self.item.append(item)
    def show(self):
        print("Путь:")
        return (self.item)
    def __reversed__(self):
        self.item.reverse()

def print_map(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                print( str("*").ljust(2), end="")
            else:
                print(str().ljust(2), end="")
        print()
    print()

def find_path(k, a):
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == k:
        if i>0 and m[i-1][j] == 0 and a[i-1][j] == 0:
          m[i-1][j] = k + 1
        if j>0 and m[i][j-1] == 0 and a[i][j-1] == 0:
          m[i][j-1] = k + 1
        if i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0:
          m[i+1][j] = k + 1
        if j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:
           m[i][j+1] = k + 1

def save_path(k, path, i, j, s):
    ii = 0
    s.push(path[ii])
    while k > 1:
        if i > 0 and m[i - 1][j] == k-1:
            i, j = i-1, j
            path.append((i, j))
            ii+=1
            s.push(path[ii])
            k-=1
        elif j > 0 and m[i][j - 1] == k-1:
            i, j = i, j-1
            path.append((i, j))
            ii += 1
            s.push(path[ii])
            k-=1
        elif i < len(m) - 1 and m[i + 1][j] == k-1:
            i, j = i+1, j
            path.append((i, j))
            ii += 1
            s.push(path[ii])
            k-=1
        elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
            i, j = i, j+1
            path.append((i, j))
            ii += 1
            s.push(path[ii])
            k -= 1
    s.__reversed__()

def print_m(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print( str(m[i][j]).ljust(2),end=' ')
        print()

def create_zeromass(m, a):
    for i in range(len(a)):
        m.append([])
        for j in range(len(a[i])):
            m[-1].append(0)

def main(a, start, end):
    create_zeromass(m, a)
    print_map(a)
    start = start
    end = end
    i,j = start
    m[i][j] = 1
    k = 0
    while m[end[0]][end[1]] == 0:
        k += 1
        find_path(k, a)

    i, j = end
    k = m[i][j]
    path = [(i,j)]
    s = Stack()
    save_path(k, path, i, j, s)
    print_m(m)
    print(s.show())
    m.clear()

def text():
    print("Выберите уровень или завершите программу:")
    print(" [1] Первый уровень")
    print(" [2] Второй уровень")
    print(" [3] Третий уровень")
    print(" [0] выход")

def menu():
    text()
    try:
        option = int(input())
    except ValueError:
        option = 5
    while option:
        if option == 1:
            main(a, start, end)
        elif option == 2:
            main(a1, start1, end1)
        elif option == 3:
            main(a2, start2, end2)
        else:
            print("Введена неккоректная команда")
        text()
        try:
            option = int(input())
        except ValueError:
            option = 5


if __name__ == '__main__':
    menu()