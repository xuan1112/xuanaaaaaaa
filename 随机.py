import random
#随机数字
a = (random.randint(0,100))
print("随机的数字是：", a)

import random
#随机点名
students = ["A", "B", "C", "D", "E", "F", "T"]

random_student = random.choice(students)

print("随机的字母是: ", random_student)