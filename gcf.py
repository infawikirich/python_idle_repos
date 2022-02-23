"""

script file: gcf.py

purpose: This program find the greatest common factor a two number

author: Mr. Asiamah

date: 03/09/21


"""

def gcf(num1, num2):
    """This function returns the greatest common factor of two number"""
    empty_1 = []
    empty_2 = []
    
    num1_list = list(range(1, num1 + 1))
    num2_list = list(range(1, num2 + 1))
    
    
    for k in range(num1):
        if num1 == 1 and num2 == 1:
            return 1
        elif num1 % num1_list[k] == 0:
            empty_1.append(num1_list[k])
            
    for i in range(num2):
        if num2 % num2_list[i] == 0:
            empty_2.append(num2_list[i])
            
    # convert the factor list to set and intersect to get the common ones
    set1 = set(empty_1)
    set2 = set(empty_2)
    inter_sect = set1.intersection(set2)
    
    # convert the set again to list
    list_intersect = list(inter_sect)
    
    # remove the maximum items that is the gcf
    max_num = max(list_intersect)
    
            
            
    return max_num
        

soln = gcf(20**30 - 1, 2015)
print(soln)

