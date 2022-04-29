class Human:
    def __init__(self, name, first, last):
        self.name = name
        self.first = first
        self.last = last

    @property
    def walk(self, name):
        print(f"{name} is walking")

    @property
    def run(self, name):
        print(f"{name} is running")

    @property
    def sit(self,name):
        print(f"{name} is sitting")

    def fullname(self,first,last):
        return f'Fullname is {first} {last}'


    def fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last


    def fullname(self):
        print('Deleting fullname')
        self.first = None
        self.last = None


class Adult(Human):
    def __init__(self, car):
        self.car=car
    def drive(self, name, car):
        print(f"{name} is driving {car}")


class Student(Adult):
    def __init__(self):
        pass

    def study(self, name):
        print(f"{name} is studying in university")


class Child(Human):
    def __init__(self):
        pass

    def play(self,name):
        print(f"{name} is playing on playground")


class Worker(Adult):
    def __init__(self):
        pass

    def relax(self,name):
        print(f"{name} is relaxing at home")


class Teacher(Worker):
    def __init__(self, students):
        self.index = 0
        self.students = students
        self.list_of_students = self.students.split()


    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.list_of_students):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.list_of_students[index]
    @staticmethod
    def gen_students(students):
        for student in students:
            yield student


    def __getitem__(self, k):
        return [k]

    def teach(self, name):
        print(f"{name} is teaching students")


w = Adult("Porshe")
# w.drive("Taras", "Porshe")
q = Teacher("Grisha, Oliya, Taras, Yasha.")
# for i in q:
#     print()
# for i in q:
#     print(i)
# for j in range(2):
#     print(q.__getitem__(j))
print(q.list_of_students[2])
