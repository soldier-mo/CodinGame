width = int(input()) 
height = int(input())  
matrix = []
for i in range(height):
    line = input()  
    matrix.append([*line])
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        right =""
        bottom =""
        if matrix[y][x] == ".":
            continue
        #right
        i = 0
        while i < width:
            i+=1
            if x+i < width:
                if matrix[y][x+i] ==".":
                    continue
                right += str(x+i)+" "+str(y) + " "
                break
            else:
                bottom += "-1 -1 "
                break
        i = 0
        #down
        while i < height:
            i+=1
            if y+i< height:
                if matrix[y+i][x] == ".":
                    continue
                bottom += str(x)+" "+str(y+i) + " "
                break
            else:
                bottom += "-1 -1 "
                break     
        print("".join([str(x)+" "+str(y)+" ",right,bottom]))