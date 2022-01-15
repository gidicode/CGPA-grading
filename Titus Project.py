    ######### Grading the student first #####################

def Calculate_Score_First():
    print( "*****First Semester Score*******")
    student = {

        'student1': {
            'Name': input('Enter first student name '),
            "math": int(input(' Enter math score')),
            'math_grade': '',
            'math_grade_point': 0,
            'math_CreditUnit': 3,
            'math_QualityPoint': 0,

            'english': int(input(' Enter English score')),
            'english_grade': '',
            'englishgrade_point': 0,
            'english_CreditUnit': 4,
            'english_QualityPoint': 0,

            'economics': int(input('Enter Economics score')),
            'economic_grade': '',
            'economic_grade_point': 0,
            'economics_CreditUnit': 2,
            'economics_QualityPoint': 0,

            'physics': int(input('Enter Physics score')),
            'physics_grade': '',
            'physics_grade_point': 0,
            'physics_CreditUnit': 3,
            'physics_QualityPoint': 0,

            'Quality_point': 0,
            'Credit_Unit': 0,
            'Grade_point_average':0
        },

        'student2': {
            'Name': input('Enter first student name '),
            "math": int(input(' Enter math score')),
            'math_grade': '',
            'math_grade_point': 0,
            'math_CreditUnit': 3,
            'math_QualityPoint': 0,

            'english': int(input(' Enter English score')),
            'english_grade': '',
            'englishgrade_point': 0,
            'english_CreditUnit': 4,
            'english_QualityPoint': 0,

            'economics': int(input('Enter Economics score')),
            'economic_grade': '',
            'economic_grade_point': 0,
            'economics_CreditUnit': 2,
            'economics_QualityPoint': 0,

            'physics': int(input('Enter Physics score')),
            'physics_grade': '',
            'physics_grade_point': 0,
            'physics_CreditUnit': 3,
            'physics_QualityPoint': 0,

            'Quality_point': 0,
            'Credit_Unit': 0,
            'Grade_point_average':0
        },

        'student3': {
            'Name': input('Enter first student name '),
            "math": int(input(' Enter math score')),
            'math_grade': '',
            'math_grade_point': 0,
            'math_CreditUnit': 3,
            'math_QualityPoint': 0,

            'english': int(input(' Enter English score')),
            'english_grade': '',
            'englishgrade_point': 0,
            'english_CreditUnit': 4,
            'english_QualityPoint': 0,

            'economics': int(input('Enter Economics score')),
            'economic_grade': '',
            'economic_grade_point': 0,
            'economics_CreditUnit': 2,
            'economics_QualityPoint': 0,

            'physics': int(input('Enter Physics score')),
            'physics_grade': '',
            'physics_grade_point': 0,
            'physics_CreditUnit': 3,
            'physics_QualityPoint': 0,

            'Quality_point': 0,
            'Credit_Unit': 0,
            'Grade_point_average':0
        }
    }

#grade maths

    if student['student1']['math'] in range(70, 100):
        student['student1']['math_grade'] = 'A'           
        student['student1']['math_grade_point'] = 5.00        

    elif student['student1']['math'] in range(60, 69):    
        student['student1']['math_grade'] = 'B'           
        student['student1']['math_grade_point'] = 4.00        

    elif student['student1']['math'] in range(50, 59):    
        student['student1']['math_grade'] = 'C'           
        student['student1']['math_grade_point'] = 3.00        

    elif student['student1']['math'] in range(45, 49):    
        student['student1']['math_grade'] = 'D'           
        student['student1']['math_grade_point'] = 3.00        

    elif student['student1']['math'] in range(40, 44):    
        student['student1']['math_grade'] = 'E'           
        student['student1']['math_grade_point'] = 2.00

    else:
        student['student1']['math_grade'] = 'F'
        student['student1']['math_grade_point'] = 1.00

     #Computing the quality point after it has been decleared by the if statement   
    student['student1']['math_QualityPoint'] = student['student1']['math_CreditUnit']  * student['student1']['math_grade_point']

    #grade english
    if student['student1']['english'] in range(70, 100):
        student['student1']['english_grade'] = 'A'           
        student['student1']['englishgrade_point'] = 5.00        

    elif student['student1']['english'] in range(60, 69):    
        student['student1']['english_grade'] = 'B'
        student['student1']['englishgrade_point'] = 4.00        

    elif student['student1']['english'] in range(50, 59):    
        student['student1']['english_grade'] = 'C'           
        student['student1']['englishgrade_point'] = 3.00    

    elif student['student1']['english'] in range(45, 49):    
        student['student1']['english_grade'] = 'D'
        student['student1']['englishgrade_point'] = 2.00        

    elif student['student1']['english'] in range(40, 44):    
        student['student1']['english_grade'] = 'E'
        student['student1']['englishgrade_point'] = 1.00
        
    else:
        student['student1']['english_grade'] = 'F'
        student['student1']['englishgrade_point'] = 1.00
    
    #Computing the quality point after it has been decleared by the if statement
    student['student1']['english_QualityPoint'] = student['student1']['english_CreditUnit']  * student['student1']['englishgrade_point']

    #Economics 
    if student['student1']['economics'] in range(70, 100):
        student['student1']['economic_grade'] = 'A'
        student['student1']['economic_grade_point'] = 5.00        

    elif student['student1']['economics'] in range(60, 69):    
        student['student1']['economic_grade'] = 'B'
        student['student1']['economic_grade_point'] = 4.00        

    elif student['student1']['economics'] in range(50, 59):    
        student['student1']['economic_grade'] = 'C'           
        student['student1']['economic_grade_point'] = 3.00        

    elif student['student1']['economics'] in range(45, 49):    
        student['student1']['economic_grade'] = 'D'
        student['student1']['economic_grade_point'] = 3.00        

    elif student['student1']['economics'] in range(40, 44):    
        student['student1']['economic_grade'] = 'E'           
        student['student1']['economic_grade_point'] = 2.00    
        
    else:
        student['student1']['economic_grade'] = 'F'
        student['student1']['economic_grade_point'] = 1.00

    #Computing the quality point after it has been decleared by the if statement
    student['student1']['economics_QualityPoint'] = student['student1']['economics_CreditUnit']  * student['student1']['economic_grade_point']

    #Physics
    if student['student1']['physics'] in range(70, 100):
        student['student1']['physics_grade'] = 'A'           
        student['student1']['physics_grade_point'] = 5.00
        
    elif student['student1']['physics'] in range(60, 69):    
        student['student1']['physics_grade'] = 'B'           
        student['student1']['physics_grade_point'] = 4.00
        
    elif student['student1']['physics'] in range(50, 59):    
        student['student1']['physics_grade'] = 'C'           
        student['student1']['physics_grade_point'] = 3.00

    elif student['student1']['physics'] in range(45, 49):    
        student['student1']['physics_grade'] = 'D'           
        student['student1']['physics_grade_point'] = 3.00

    elif student['student1']['physics'] in range(40, 44):    
        student['student1']['physics_grade'] = 'E'           
        student['student1']['physics_grade_point'] = 2.00

    else:
        student['student1']['physics_grade'] = 'F'
        student['student1']['physics_grade_point'] = 1.00

    student['student1']['physics_QualityPoint'] = student['student1']['physics_CreditUnit']  * student['student1']['physics_grade_point']

    if student['student2']['math'] in range(70, 100):
        student['student2']['math_grade'] = 'A'           
        student['student2']['math_grade_point'] = 5.00

    elif student['student2']['math'] in range(60, 69):    
        student['student2']['math_grade'] = 'B'           
        student['student2']['math_grade_point'] = 4.00

    elif student['student2']['math'] in range(50, 59):    
        student['student2']['math_grade'] = 'C'           
        student['student2']['math_grade_point'] = 3.00

    elif student['student2']['math'] in range(45, 49):    
        student['student2']['math_grade'] = 'D'           
        student['student2']['math_grade_point'] = 3.00

    elif student['student2']['math'] in range(40, 44):    
        student['student2']['math_grade'] = 'E'           
        student['student2']['math_grade_point'] = 2.00
    else:
        student['student2']['math_grade'] = 'F'
        student['student2']['math_grade_point'] = 1.00
    student['student2']['math_QualityPoint'] = student['student2']['math_CreditUnit']  * student['student2']['math_grade_point']

    #grade english
    if student['student2']['english'] in range(70, 100):
        student['student2']['english_grade'] = 'A'           
        student['student2']['englishgrade_point'] = 5.00

    elif student['student2']['english'] in range(60, 69):    
        student['student2']['english_grade'] = 'B'
        student['student2']['englishgrade_point'] = 4.00

    elif student['student2']['english'] in range(50, 59):    
        student['student2']['english_grade'] = 'C'           
        student['student2']['englishgrade_point'] = 3.00

    elif student['student2']['english'] in range(45, 49):    
        student['student2']['english_grade'] = 'D'
        student['student2']['englishgrade_point'] = 3.00

    elif student['student2']['english'] in range(40, 44):    
        student['student2']['english_grade'] = 'E'
        student['student2']['englishgrade_point'] = 2.00
    else:
        student['student2']['english_grade'] = 'F'
        student['student2']['englishgrade_point'] = 1.00
    student['student2']['english_QualityPoint'] = student['student2']['english_CreditUnit']  * student['student2']['englishgrade_point']

    #Economics
    if student['student2']['economics'] in range(70, 100):
        student['student2']['economic_grade'] = 'A'
        student['student2']['economic_grade_point'] = 5.00

    elif student['student2']['economics'] in range(60, 69):    
        student['student2']['economic_grade'] = 'B'
        student['student2']['economic_grade_point'] = 4.00

    elif student['student2']['economics'] in range(50, 59):    
        student['student2']['economic_grade'] = 'C'           
        student['student2']['economic_grade_point'] = 3.00

    elif student['student2']['economics'] in range(45, 49):    
        student['student2']['economic_grade'] = 'D'
        student['student2']['economic_grade_point'] = 3.00

    elif student['student2']['economics'] in range(40, 44):    
        student['student2']['economic_grade'] = 'E'           
        student['student2']['economic_grade_point'] = 2.00    
    else:
        student['student2']['economic_grade'] = 'F'
        student['student2']['economic_grade_point'] = 1.00

    student['student2']['economics_QualityPoint'] = student['student2']['economics_CreditUnit']  * student['student2']['economic_grade_point']

    #Physics
    if student['student2']['physics'] in range(70, 100):
        student['student2']['physics_grade'] = 'A'           
        student['student2']['physics_grade_point'] = 5.00

    elif student['student2']['physics'] in range(60, 69):    
        student['student2']['physics_grade'] = 'B'           
        student['student2']['physics_grade_point'] = 4.00

    elif student['student2']['physics'] in range(50, 59):    
        student['student2']['physics_grade'] = 'C'           
        student['student2']['physics_grade_point'] = 3.00

    elif student['student2']['physics'] in range(45, 49):    
        student['student2']['physics_grade'] = 'D'           
        student['student2']['physics_grade_point'] = 3.00

    elif student['student2']['physics'] in range(40, 44):    
        student['student2']['physics_grade'] = 'E'           
        student['student2']['physics_grade_point'] = 2.00

    else:
        student['student2']['physics_grade'] = 'F'
        student['student2']['physics_grade_point'] = 1.00
    student['student2']['physics_QualityPoint'] = student['student2']['physics_CreditUnit']  * student['student2']['physics_grade_point']

    #Student 3
    if student['student3']['math'] in range(70, 100):
        student['student3']['math_grade'] = 'A'           
        student['student3']['math_grade_point'] = 5.00

    elif student['student3']['math'] in range(60, 69):    
        student['student3']['math_grade'] = 'B'           
        student['student3']['math_grade_point'] = 4.00

    elif student['student3']['math'] in range(50, 59):    
        student['student3']['math_grade'] = 'C'           
        student['student3']['math_grade_point'] = 3.00

    elif student['student3']['math'] in range(45, 49):    
        student['student3']['math_grade'] = 'D'           
        math_grade_point = 3.00

    elif student['student3']['math'] in range(40, 44):    
        student['student3']['math_grade'] = 'E'           
        student['student3']['math_grade_point'] = 2.00
    else:
        student['student3']['math_grade'] = 'F'
        student['student3']['math_grade_point'] = 1.00
    
    student['student3']['math_QualityPoint'] = student['student3']['math_CreditUnit']  * student['student3']['math_grade_point']

    #grade english
    if student['student3']['english'] in range(70, 100):
        student['student3']['english_grade'] = 'A'           
        student['student3']['englishgrade_point'] = 5.00

    elif student['student3']['english'] in range(60, 69):    
        student['student3']['english_grade'] = 'B'
        student['student3']['englishgrade_point'] = 4.00

    elif student['student3']['english'] in range(50, 59):    
        student['student3']['english_grade'] = 'C'           
        student['student3']['englishgrade_point'] = 3.00

    elif student['student3']['english'] in range(45, 49):    
        student['student3']['english_grade'] = 'D'
        student['student3']['englishgrade_point'] = 3.00

    elif student['student3']['english'] in range(40, 44):    
        student['student3']['english_grade'] = 'E'
        student['student3']['englishgrade_point'] = 2.00
    else:
        student['student3']['english_grade'] = 'F'
        student['student3']['englishgrade_point'] = 1.00

    student['student3']['english_QualityPoint'] = student['student3']['english_CreditUnit']  * student['student3']['englishgrade_point']

    #Economics
    if student['student3']['economics'] in range(70, 100):
        student['student3']['economic_grade'] = 'A'
        student['student3']['economic_grade_point'] = 5.00

    elif student['student3']['economics'] in range(60, 69):    
        student['student3']['economic_grade'] = 'B'
        student['student3']['economic_grade_point'] = 4.00

    elif student['student3']['economics'] in range(50, 59):    
        student['student3']['economic_grade'] = 'C'           
        student['student3']['economic_grade_point'] = 3.00

    elif student['student3']['economics'] in range(45, 49):    
        student['student3']['economic_grade'] = 'D'
        student['student3']['economic_grade_point'] = 3.00

    elif student['student3']['economics'] in range(40, 44):    
        student['student3']['economic_grade'] = 'E'           
        student['student3']['economic_grade_point'] = 2.00    
    else:
        student['student3']['economic_grade'] = 'F'
        student['student3']['economic_grade_point'] = 1.00

    student['student3']['economics_QualityPoint'] = student['student3']['economics_CreditUnit']  * student['student3']['economic_grade_point']

    #Physics
    if student['student3']['physics'] in range(70, 100):
        student['student3']['physics_grade'] = 'A'           
        student['student3']['physics_grade_point'] = 5.00

    elif student['student3']['physics'] in range(60, 69):    
        student['student3']['physics_grade'] = 'B'           
        student['student3']['physics_grade_point'] = 4.00

    elif student['student3']['physics'] in range(50, 59):    
        student['student3']['physics_grade'] = 'C'           
        student['student3']['physics_grade_point'] = 3.00

    elif student['student3']['physics'] in range(45, 49):    
        student['student3']['physics_grade'] = 'D'           
        student['student3']['physics_grade_point'] = 3.00

    elif student['student3']['physics'] in range(40, 44):    
        student['student3']['physics_grade'] = 'E'           
        student['student3']['physics_grade_point'] = 2.00

    else:
        student['student3']['physics_grade'] = 'F'
        student['student3']['physics_grade_point'] = 1.00
    
    student['student3']['physics_QualityPoint'] = student['student3']['physics_CreditUnit']  * student['student3']['physics_grade_point']

    #CalculateEach Student QP CU GPA
    student['student1']['Quality_point'] = (
        student['student1']['math_QualityPoint'] + 
        student['student1']['english_QualityPoint'] +
        student['student1']['economics_QualityPoint'] +
        student['student1']['physics_QualityPoint']
        )

    student['student1']['Credit_Unit'] = (
        student['student1']['math_CreditUnit'] + 
        student['student1']['english_CreditUnit'] +
        student['student1']['economics_CreditUnit'] +
        student['student1']['physics_CreditUnit']
    )

    student['student1']['Grade_point_average'] = student['student1']['Quality_point'] / student['student1']['Credit_Unit']

    for student_id, student_info in student.items():
        print("\nStudentID: ", student_id)

        for key in student_info:
            print(key + ':', student_info[key])
            
    return student


#FirstSemester
#print('Math Score:', math, '\n' + 'Math Grade: ' + math_grade + '\n' + 'Grade Point:', math_grade_point)
Calculate_Score_First()

#secondSemester = Calculate_Score() 