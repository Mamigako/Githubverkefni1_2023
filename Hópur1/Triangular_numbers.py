# Ask for input, cconvert to int.
num = int(input()) # Do not change this line

# Loop through 1 to input number and apply triangular formula to each number on the way.
for i in range(1, num+1):
    triangular_num = i * (i+1) // 2
    
    # Print each result.
    print(triangular_num)
