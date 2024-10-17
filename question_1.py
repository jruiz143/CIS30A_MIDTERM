#MIDTERM QUESTION 1
#Write a Python program that reads a text file named grades.txt, where each line 
# contains a student's name followed by their grade (e.g., Alice 88). The program should:
#1.Calculate the average grade. 2.Count the number of students who scored above the average.
#3. Write the average and the count of above-average students to a file named results.txt

#CREATE A FUNCTION TO CALC THE AVG GRADES
def calculate_average(grades):
    if len(grades) == 0:  # CHECK IF LIST IS EMPTY
        return 0  
    #COUNT THE NUMBER OF GRADES IN LIST
    sum = 0  # INTIALIZE VARIABLE 
    for grade in grades:  # LOOP THROUGH EACH GRADE IN THE LIST
        sum += grade  # ADD EACH GRADE TO CREATE SUM
    
    return sum / len(grades)  # RETURN THE AVERAGE: TOTAL SUM OF GRADES/ NUMBER OF GRADES COUNTED


# OPEN AND READ GRADES.TXT FILE
with open('grades.txt', 'r') as file:
    lines = file.readlines() #READ ENTIRE FILE

#CREATE LIST OF STUDENT GRADES
grades = [] #INTIALIZE AN EMPTY LIST FOR GRADES TO BE STORED IN
for line in lines:
    student_scores = line.split()  # SPLIT THE STUDENT'S NAME(STRING), AND STUDENT'S SCORE (INT)
    grade = int(student_scores[1])  # CONVERTING STUDENTS SCORE TO INT WHICH IS SECOND ELEMENT[1]
    grades.append(grade) #WILL BE INCLUDED INTO THE GRADES LIST NOW

#CALC THE AVG GRADE
average_grade = calculate_average(grades)

#ACCOUNT FOR STUDENTS WHO SCORE ABOVE AVG/INTIALIZE VARIABLE
amount_above_average = 0  
for grade in grades:  # GO THROUGH EACH GRADE IN LIST CREATED
    if grade > average_grade:  # IF GRADE IS HIGHER THAN AVERAGE
        amount_above_average += 1  # ADD 1 TO THE COUNT

# WRITE RESULTS TO TEXTFILE RESULTS.TXT
with open('results.txt', 'w') as file:
    file.write(f'AVERAGE STUDENT GRADE: {average_grade:.2f}\n')
    file.write(f'NUMBER OF STUDENTS WHO SCORED ABOVE AVERAGE: {amount_above_average}')

print ("Output printed in results.txt file.")
