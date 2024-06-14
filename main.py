from RationalList import RationalList
from Rational import Rational


def read_rational_file(filename):
    rational_list = RationalList()
    with open(filename, 'r') as file:
        for line in file:
            numbers = line.split()
            for num in numbers:
                if '/' in num:
                    n, d = map(int, num.split('/'))
                    rational_list.append(Rational(n, d))
                else:
                    rational_list.append(int(num))
    return rational_list


file_list = ['input01.txt', 'input02.txt', 'input03.txt']
for filename in file_list:
    r_list = read_rational_file(filename)
    print(f"Сума чисел в {filename}: {r_list.sum()}")
    print(f"Послідовність в {filename}:")
    for rational in r_list:
        print(rational)