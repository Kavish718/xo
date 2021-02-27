arr=[['a','a','a'],['a','a','a'],['a','a','a']]
def check1(arr):
    if(arr[0][0]=='x' and arr[1][1]=='x' and arr[2][2]=='x' ):
        print("player 1 has won")
        return 1
    elif(arr[2][0]=='x' and arr[1][1]=='x' and arr[0][2]=='x'):
        print("player 1 has won")
        return 1
    r1=0 
    r2=0
    r3=0
    for i in range(3):
        if arr[i][0]=='x' :
            r1+=1
            if r1==3:
                print("player 1 has won")
                return 1
        elif arr[i][1]=='x' :
             r2+=1
             if r2==3:
                print("player 1 has won")
                return 1
        elif arr[i][2]=='x' :
            r3+=1
            if r3==3:
                print("player 1 has won")
                return 1
    c1=0; c2=0 ;c3=0
    for j in range(3):
        if arr[0][j]=='x' :
            c1+=1
            if c1==3:
                print("player 1 has won")
                return 1
        elif arr[1][j]=='x' :
             c2+=1
             if c2==3:
                print("player 1 has won")
                return 1
        elif arr[2][j]=='x' :
            c3+=1
            if c3==3:
                print("player 1 has won")
                return 1
def check2(arr):
    if(arr[0][0]=='o' and arr[1][1]=='o' and arr[2][2]=='o' ):
        print("player 2 has won")
        return 1
    elif(arr[2][0]=='o' and arr[1][1]=='o' and arr[0][2]=='o'):
        print("player 2 has won")
        return 1
    r1=0;r2=0;r3=0
    for i in range(3):
        if arr[i][0]=='o' :
            r1+=1
            if r1==3:
                print("player 2 has won")
                return 1
        elif arr[i][1]=='o' :
             r2+=1
             if r2==3:
                print("player 2 has won")
                return 1
        elif arr[i][2]=='o' :
            r3+=1
            if r3==3:
                print("player 2 has won")
                return 1
    c1=0;c2=0;c3=0
    for j in range(3):
        if arr[0][j]=='o' :
            c1+=1
            if c1==3:
                print("player 2 has won")
                return 1
            elif arr[1][j]=='o' :
                c2+=1
                if c2==3:
                    print("player 2 has won")
                    return 1
        elif arr[2][j]=='o' :
            c3+=1
            if c3==3:
                print("player 2 has won")
                return 1
checklist=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
temp=[0,0]
n=0
for n in range(9):
    r=int(input("player 1 enter row :"))
    c=int(input("player 1 enter column :"))
    for k in range(9):
        while (checklist[k][0]==r and checklist[k][1]==c) :
            print("position already occupied")
            r=int(input("player 1 enter row :"))
            c=int(input("player 1 enter column :"))
    temp[0]=r
    temp[1]=c
    checklist[n]=temp   
    n+=1 
    arr[r-1][c-1]='x'
    check1(arr)
    if check1(arr)== 1:
        break
    r=int(input("player 2 enter row :"))
    c=int(input("player 2 enter column :"))
    for k in range(9):
        while (checklist[k][0]==r and checklist[k][1]==c) :
            print("position already occupied")
            r=int(input("player 2 enter row :"))
            c=int(input("player 2 enter column :"))
    temp[0]=r
    temp[1]=c
    checklist[n]=temp
    n+=1
    arr[r-1][c-1]='o'
    check2(arr)
    if check2(arr)== 1:
        break



