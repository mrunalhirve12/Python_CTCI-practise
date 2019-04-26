class Course():
    def __init__(self, cno, cname, terms):
        self.cNo = cno
        self.cName = cname
        self.terms = terms

    def display(self):
        str = " Course No:{} \n Course Name:{} \n Terms:{} \n"
        str = str.format(self.cNo, self.cName, self.terms)
        print(str)


class Transcript():
    def __init__(self, course, grades):
        self.courseList = {}
        self.course = course
        self.grades = grades

    def add(self):
        courses = []
        self.courseList[self.course] = self.grades
        for key, value in self.courseList.items():
            courses.append(key)
        return courses

    def gpa(self):
        credits = 3
        result = 0
        for i in self.courseList:
            result += (self.courseList[i] * credits) / credits
        return result


class Student(Transcript):
    def __init__(self, name, courseNo, grades):
        self.name = name
        super(Student, self).__init__(courseNo, grades)

    """
    def to_string(self):
        course = super(Student, self).add()
        gpa= super(Student, self).gpa()
    """

    def display(self):
        course = super(Student, self).add()
        gpa = super(Student, self).gpa()
        str = " StudentName:{} \n List of Courses:{} \n GPA:{} \n"
        str = str.format(self.name, course, gpa)
        print(str)



def demo():
    course1 = Course(1, "OS", ["Fall"])
    course2 = Course(2, "DB", ["Winter"])
    course3 = Course(3, "ML", ["Fall"])
    course4 = Course(4, "AI", ["Winter"])

    course1.display()
    course2.display()
    course3.display()
    course4.display()

    #t1 = Transcript(1, 3)
    #t2 = Transcript(2, 2)

    student1 = Student("Amarjit", 1, 3)
    #student1 = Student("Amarjit", 2, 3)
    student2 = Student("Amar", 2, 3)

    student1.display()
    student2.display()


if __name__ == "__main__":
    demo()
