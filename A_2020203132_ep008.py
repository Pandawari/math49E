import time
begin = time.time()
# First i thought about calculating the first 13th digit product. Then multiply the 14th digit and divide by first to shift the product to the next sequence.
# When i encounter zeroes. I actually dont have to scan the next 12 numbers. but with loopin over like this. It was inevitable.
# I could have solved this issue by moving 12 digitys to the right and calcualte first 13th sequence and start the shifting the product window there.
# This would be 3 operations in O(n) in best scenario.
# Then i thought about pythons split function. Splitting the string from zeroes. It would returns a list of segments that. Some are shorter than 13 digits. This would be mean they are useless to calcualte 13th digit products and i can only focus on the ones who is longer than 13 digits

number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
greatest_product = 1 # last variable to store maximum value
str_number = str(number)

# I splitted the string from the zeroes. This function in python returns a list of strings.
lst_of_segments = str_number.split('0')

for segment in lst_of_segments:
    
    if len(segment) >= 13: # Now I can do the the first shifting algorithm i wrote about and eliminate the ones with length smaller than 13. 

        product = 1 
        for digit in range(13):
           product *= int(segment[digit]) # This calculates the first 13 digit product in each segment. 

        
        if product > greatest_product:
            greatest_product = product
           
        # this part is the shifting part. I beleive its called Sliding windows algorithm. It hold a 13 digit window and slides right.
        for digit in range(len(segment) - 13):
            
            new_digit = int(segment[digit + 13])
            old_digit = int(segment[digit])
            product = product * new_digit // old_digit # This could be problematic if the old digit could be zero but in my case there is no 0 in the segments.
            
            # Loop might end here so we check again. 
            if product > greatest_product:
                greatest_product = product

print(greatest_product)
    
end = time.time()
print(f"Finished in {end - begin} seconds.")