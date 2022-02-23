"""

script file: factor_of_num.py

purpose: This program find the factor of a number

author: Mr. Asiamah

date: 03/09/21


"""

def fact(n):
    empty = []
    if n == 1:
        print(n)
    elif n > 1:
        n_list = list(range(1, n+1))
        for k in range(len(n_list)):
            if n % n_list[k] == 0:
                empty.append(n_list[k])
    else:
        return None
    print(empty)
