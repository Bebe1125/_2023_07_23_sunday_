import random
def get_all_names() -> list[list]:
    with open('names.txt',mode='r',encoding='utf-8') as file:
        names:list[str] = []
        for line in file:
            #names.append(line)
            line = line.rstrip('\n')
            names.append(line)
        return names
    
def get_random_names(nums:int) -> list[str]:
    names = get_all_names()
    random_list = random.choices(names,k=nums)
    return random_list

def get_students(student_num:int) -> list[list]:    
    students:list[list] = [] #建立第一維list
    names = get_random_names(nums=student_num)
    for i in range(student_num):
        one_student = [random.randint(50, 100) for _ in range(5)] #建立第2維list
        name = names[i]
        one_student = [name] + one_student
        students.append(one_student)
    return students

nums = int(input("請輸入學生的數量:"))
print(get_students(student_num=nums))


