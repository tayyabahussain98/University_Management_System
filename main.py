class Person:
    def __init__(self, my_name: str, my_age: int):
        self.name = my_name
        self.age = my_age

    def get_name(self):
        return f'Name: {self.name} | Age: {self.age}'

class Student(Person):
    def __init__(self, name: str, age: int, roll_num: str):
        super().__init__(name, age)
        self.roll_num = roll_num
        self.course_list = []

    def register_for_courses(self, course: str):
        self.course_list.append(course)

class Instructor(Person):
    def __init__(self, name: str, age: int, salary: int, courses: str):
        super().__init__(name, age)
        self.salary = salary
        self.courses = courses

    def assign_course(self):
        return f'Sir {self.name} assign {self.courses}'
    
class Courses:
    def __init__(self, course_id: int, course_name: str):
        self.id = course_id
        self.name = course_name
        self.student_list = []
        self.instructor_list = []

    def add_students(self, student: Student):
        self.student_list.append(student)

    def set_insturctor(self, instructor: Instructor):
        self.instructor_list.append(instructor)

class Department():
    def __init__(self, dept_name: str):
        self.name = dept_name
        self.course_list = []

    def add_course(self, course: Courses):
        self.course_list.append(course)


print('\n--- University Management System ---')
stud1 = Student('Tayyaba', 27, 'GIAIC123')
print(f'Student Created: {stud1.get_name()} | Roll Number: {stud1.roll_num}')

inst1 = Instructor('Hamzah Syed', 30, 50000, 'Agentic AI')
print(f'Instructor Created: {inst1.get_name()} | Salary: {inst1.salary} | Course: {inst1.courses}')
print(inst1.assign_course())

ai_course = Courses(1, 'Agentic AI')
print(f'Course Created: {ai_course.id}. {ai_course.name}')
py_course = Courses(2, 'Python')
print(f'Course Created: {py_course.id}. {py_course.name}')

dep1 = Department('Development')
dep1.add_course(ai_course)
dep1.add_course(py_course)
print(f'Department Created: {dep1.name}')

ai_course.add_students(stud1)
py_course.add_students(stud1)
ai_course.set_insturctor(inst1)
py_course.set_insturctor(inst1)

stud1.register_for_courses(ai_course)
stud1.register_for_courses(py_course)


print('\n--- Course Enrollment Details ---')
print(f'Course: {ai_course.id}. {ai_course.name}')
print(f'Course: {py_course.id}. {py_course.name}')
print(f'Students:', [stud.get_name() for stud in ai_course.student_list or py_course.student_list])
print(f'Instructors:', [inst.get_name() for inst in ai_course.instructor_list or py_course.instructor_list])

print('\n--- Student Registered Course ---')
for stud in stud1.course_list:
    print(f'{stud1.name} is registered in {stud.name}')