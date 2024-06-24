# Tuple
import time

t = (1, 2, 3, 4, "Akash")
print(t)

# Conversion of list into tuple
l = [1, 2, 3, 4, "Akash", "Suraj", ]
t1 = tuple(l)
print(t1)
print(type(t1))
new_t = (t, t1)
print("This is tuple = ", new_t)

# SET= Collection of item (uniq item), its not allowed to duplicate the item

New_set = {1, 2, 3, 4, "Akash", "Suraj", 2, 3, 4, "Akash", "Suraj"}
print("This is SET not allowed duplicates = ", New_set)
print(len(New_set))
print(type(New_set))

S1 = {1, 2, 3, "Akash", "Engineers"}
S2 = {3, 4, 5}
se_t = S1.union(S2)
print("This is Union of two set = ", se_t)
s_et = S1.intersection(S2)
print("This is Intersection of two set = ", s_et)
for i in S1:
    print(i)

S1.remove("Akash")
print(S1)
S2.add("Akash")
print(S2)

#Decoratores = it is function which takes another funcion as argument , it can be use multiple times

def my_decorators(fun):
    def wrapper():
        print("Hello Everyone")
        fun()
        print("Thank you ! have Good day")
    return wrapper


@my_decorators
def my_self():
    print("I am Akash")
    print("I am a Software Engineer")
my_self()

def note_time(fun):
    import datetime
    def wrapper():
        start_time = time.time()
        fun()
        end_time = time.time()
        print ("Time taken = " + str(end_time-start_time))
    return wrapper
@note_time
def log_time():
    time.sleep(10)
    print ("Log Time taken is " )
log_time()

#Dictionary = it is key and value pair, it is mutable in nature
dict = {"Name":"Akash", "Age":25, "City":"Pune"}
print(len(dict))
print(dict["Name"])
print(dict.keys())
print(dict.values())
dict["Age"] = 26

for k,v in dict.items():
    print(k,v)

