def sum_numbers(numbers):
    total=0
    for number in numbers:
        total+=number
        return total
number_list=[1,2,3,4,5]
print(sum_numbers(number_list))