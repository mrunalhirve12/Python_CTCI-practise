

class Course():
    cNo=[]
    cName=[]
    terms=[]
    def __init__(self, cno, cname, terms):
        self.cNo.append(cno)
        self.cName.append(cname)
        self.terms.append(terms)

    def get_course(self, courseNo):
        idx = self.cNo.index(courseNo)
        return self.cName.index[idx]


    def display(self):
        str = " Course No:\t {} \n Course Name:\t {} \n Terms:\t {} \n"
        str = str.format(self.cNo, self.cName, self.terms)
        print(str)


class Transcript(Course):
    def __init__(self,cNumber, grades):
        #self.courseList = {}
        self.course_list = []
        self.grades = []

        if type(cNumber)== list:
            for a,b in zip(cNumber,grades):
                self.course_list.append(a)
                self.grades.append(b)
        else:
            self.course_list.append(a)
            self.grades.append(b)

    def get_transcript(self):
        width = 30
        trans = ""
        for each in self.course_list:
            idx = self.course_list.index(each)
            trans += self.cName[idx]
            trans += "{0:{width}}".format(self.gpa(self.grades[idx]), width=width)
            trans += "\n"
        print(trans)
    def gpa(self,grade):
        #credits = 3
        #result = 0
        #for i in range(len(self.courseList)):
        #    result += (self.courseList[i] * credits) / credits
        #return result
        gpa = {"A":4.0, "A-":3.67,"B+":3.33,"B":3.0,"B-":2.67,"C+":2.33,"F":2.0}
        return gpa[grade]


class Student(Transcript):
    def __init__(self, name, courseNo, grades):
        self.name = name
        super(Student, self).__init__(courseNo, grades)
        #self.gpa = 0
        #self.course = []

    def getTranscript(self):
        print("Student's name: ", self.name)
        print("Below is the overall transcript\n")
        print("{0:{width}}".format(" Course Name.", width=30), end='')
        #print("{0:{width}}".format("Grade", width=10), end='')
        print("GPA")
        super(Student, self).get_transcript()


    def display(self):
        str = " StudentName:\t {} \n List of Courses:\t {} \n GPA:\t {} \n"
        str = str.format(self.name, self.course, self.gpa)
        print(str)



def demo():
    course1 = Course(1, "OS", ["Fall"])
    course2 = Course(2, "DB", ["Winter"])
    course3 = Course(3, "ML", ["Fall"])
    course4 = Course(4, "AI", ["Winter"])

    #course1.display()
    #course2.display()
    #course3.display()
    #course4.display()

    #t1 = Transcript(1, 3)
    #t2 = Transcript(2, 2)

    s1 = Student("Amarjit",[1,2], ["A","A-"])
    s2 = Student("Shraddha", [1, 2], ["A", "A"])
    s1.getTranscript()
    s2.getTranscript()
    #student2 = Student("Amar",2, 3)

    #student1.add_course()
    #student2.add_course()

    #student1.display()
    #student2.display()


if __name__ == "__main__":
    demo()

