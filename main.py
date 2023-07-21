class Semester:
    # def __init__(self, courseCode, courseGrade, courseUnit):
    #     self.courseCode = courseCode
    #     self.courseGrade = courseGrade
    #     self.courseUnit = courseUnit

    def calculateGPA(self):
        course_delimeter = 0
        a = int(input('enter your number of courses this semester: '))

        #constants
        total_units = 0
        total_point = 0
        points = 0
        score= 0
        tryings=0
        for i in range(a):
            self.courseCode = input("Enter your course: ")
            self.courseGrade = input("Enter your grade: ")
            self.courseUnit = int(input("Enter your units here: "))
            course_delimeter+=1
            print("you've calculated " + str(course_delimeter) +  " courses")
            print("##################################################################")
            total_units += self.courseUnit
            if self.courseGrade == "A":
                score=5
                
            elif self.courseGrade == "B":
                score=4
                
            elif self.courseGrade == "C":
                score=3
                
            elif self.courseGrade == "D":
                score=2
                
            elif self.courseGrade == "E":
                score=1
                
            elif self.courseGrade == "F":
                score=0

            points += score
            first_point_generated= score * self.courseUnit
            tryings += first_point_generated
        
        print(total_units)

        Cgpa= tryings / total_units
        print(Cgpa)
        cgpa =float(tryings/ total_units)
        classs = ""

        di = {
             "1st": "First Class, You're the best, 100%",
             "2nd up": "Second Class Upper, You did very well, Don't give up",
             "2nd low": "Second Class Lower, Nice, Keep pushing",
             "3rd": "Third Class, Ah stafiroullah",
             "pas": "Pass, Oya dey go your village"
        }


        if Cgpa >= 4.50:
            classs = di["1st"]
                # classs = "First class"
        elif Cgpa >= 3.50 and Cgpa<= 4.49:
            classs = di["2nd up"]
        elif Cgpa >= 2.40 and Cgpa <= 3.49:
            classs = di["2nd low"]
        else:
            classs = di["3rd"]
        print("YOUR CGPA IS: " + str(round(Cgpa, 2)))
        print("You got a " + classs)
