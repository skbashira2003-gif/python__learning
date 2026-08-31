#DAY14: Nested loop 

age = 20
has_id = True

if age >= 18:
    print("You are eligible")       # Output: You are eligible

    if has_id:
        print("ID verified")        # Output: ID verified


#Matrix


matrix = [ [4,5,6], [1,2,3], [7,8,9] ]
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        print(matrix[r][c], end=' ')
    print()
print()

#colwise: it should be sqare matrix
for c in range(len(matrix[0])):
    for r in range(len(matrix)):
        print(matrix[r][c], end=' ')
    print()


