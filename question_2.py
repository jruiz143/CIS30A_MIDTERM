#MIDTERM QUESTION 2
#Write a Python function called transform_data that accepts a list of integers. The function should:
#1. Create a new list containing each integer from the original list squared.
#2. Calculate the sum of the squared values.
#3. Return both the new list and the sum.
#Tips: to test Question 2, call your function and pass in the values

# DEFINE FUNCTION
def transform_data(numbers):
# CREATE A NEW LIST OF INTEGERS THAT SQUARES THE ORIGINAL
    squared_numbers = [] #INTIALIZE EMPTY LIST FOR SQUARED VALUES TO BE PLACED IN
    for num in numbers: 
        squared_value = num ** 2  # SQUARE THE NUMBERS
        squared_numbers.append(squared_value)  # ADD SQUARED NUMBERS TO LIST
    
    # CALC SUM OF THE SQUARED NUMBERS
    sum_of_squares = 0  # INTIALIZE VARIABLE
    for squared in squared_numbers:
        sum_of_squares += squared  # ADD EACH SQUARED VALUE
    
    # RETURN THE LIST OF SQUARED NUMBERS
    return squared_numbers  

#LIST OF NUMBERS
numbers = [1, 2, 3, 4]

#CALL FUNCTION
squared_list = transform_data(numbers)

#SUM OF SQUARED NUMBERS THAT GOT RETURNED
sum_of_squares = sum(squared_list)

# DISPLAY RESULTS
print ("ORIGINAL LIST OF NUMBERS:", numbers)
print("SQUARED NUMBER LIST:", squared_list)
print("SUM OF SQUARED NUMBERS:", sum_of_squares)
