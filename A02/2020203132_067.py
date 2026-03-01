import time
begin = time.time()

# First i will start by reading the file once and write it to a matrix. This way i can avoiod doing file operations every time. 
triangle_matrix = []
with open("./0067_triangle.txt", "r") as file:
    for line in file:
        triangle_matrix.append([int(x) for x in line.split()]) # split each line from whitespaces. in each line.split it returns the line in a list where each element is a string. Like ["12","41"] ect. List comprehension uses this lists and converts each string element into a integer and finally it is added to the matrix as a list.
        
# I need to store the elements in matrix but i would like each number to be int instead of converting during my function below. That is why i used this list comprehension
## TXT FILE MUST BE NAMED EXACTLY AS ABOVE IN THE SAME WORKING DIRECTORY.
        

def maximum_path_sum(triangle_matrix):
    #Okey my big idea is so to start from left side of the second last row. Look for the "children" of the number meaning its available paths. Check which is greater. add the bigger number to my oroginal number. iterate to the right. Until every pair in that row is scanned.
    #Then move up in rows and now start from left side again. Now check the new children numbers. Which would be updated from addition from previous row
    depth = len(triangle_matrix) 
    
    for row in range(depth-2,-1,-1): # from second last row to the first row 0
        for i in range(row + 1): # inside the row. Go from left to right index and look its availabie paths or children.
            
            first_number = (triangle_matrix[row+1][i])
            second_number = (triangle_matrix[row+1][i+1])
            #simple logic didnt forget =
            if first_number >= second_number:
                bigger_number = first_number
            elif second_number > first_number:
                bigger_number = second_number
            
            triangle_matrix[row][i] += bigger_number # add the bigger number into our original number
            
        # By going up in rows and doing the same operations. Last row would get bigger and bigger as we sum the numbers. They will get compared and in the last iteration the biggest summ would be added to the first element and we return
        
    return triangle_matrix[0][0] ## In the largest summation would be added to the first element



print(maximum_path_sum(triangle_matrix))
end = time.time()
print(f"Finished in {end - begin} seconds.")