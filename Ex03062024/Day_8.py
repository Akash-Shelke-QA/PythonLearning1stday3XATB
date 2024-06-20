num = [1, 2, 3]  # Num is variable which assign the list of intiger values


def do_some(Akash_list):  # Akash list is argument in the "do_some" function
    Akash_list[0] = 10
    Akash_list.append(100)
    return Akash_list


l = do_some(num)
print(l)
print(id(l))

do_some(Akash_list=l)[2] = 22  # Adding "22" number on the "2nd" index position in the Akash_list
print(l)
print(id(l))

lambda function

o_F = lambda a, b, c: a + b + c
print(o_F(1, 2, 3))


def sum_of(a, b):
    return a + b


A = sum_of(10, 20)
print(A)

A_f = lambda a, b: a + b
print(A_f(10, 20))


def find_odd_even(num):
    if num % 2 == 0:
        print("Number is Even")

    else:
        print("Number is Odd")


find_odd_even(4)

Check_odd_even = lambda b: "Number is even" if b % 2 == 0 else "Number is Odd"
print(Check_odd_even(3))

A_list = [2, 3, 4, 5, 6]

temp_list = []
for i in A_list:
    temp = i * 2
    temp_list.append(temp)
print(temp_list)


# By Using MAP
def double_item(num):
    return num * 2


double_list = list(map(double_item,
                       temp_list))  # Item value is fetched from "temp_list" one by one and stored in "double_item" >> then it wil multiply by "2"
print(double_list)  # And then stored in "double_list"

# By Using lambda
double_list_2 = list(map(lambda a: a * 2, double_list))
print(double_list_2)
