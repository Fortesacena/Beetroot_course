#------------------------------Task1----------------------

from typing import List, Tuple

# We assume that all lists passed to functions are same length N


def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res

def question2(n: int) -> int:
	for _ in range(10):
		n **= 3
	return n

def question3(first_list: List[int], second_list: List[int])-> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


def question4(input_list: List[int]) -> int:
    res = 0
    for el in input_list:
        if el > res:
            res = el
    return res



# answers 
# 1 - n^2
# 2 - 1
# 3 - n^2
# 4 - n




