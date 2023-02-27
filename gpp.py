try :
    from os import system
    from re import findall

    file_name = input("Enter file name : ")

    system("cls")

    file = open(file_name, "r")
    file_text = file.read()
    file_lines = file_text.split("\n")

    line_number = 0


    A = None
    B = None
    C = None
    D = None

    a = None
    b = None
    d = None
    
    for_if = None

    while line_number < len(file_lines):
        line = file_lines[line_number]
        
        set_comment = findall("//.*", line)
        
        move_a = findall("A,.*", line)
        move_b = findall("B,.*", line)
        move_c = findall("C,.*", line)
        move_d = findall("D,.*", line)
            
        if line == "" : pass
        
        elif len(set_comment) > 0 : pass
        
        elif len(move_a) > 0 :
            A = line.replace("A,", "")
            if A == "B" : A = B
            if A == "D" : A = D
        elif len(move_b) > 0 :
            B = line.replace("B,", "")
            if B == "A" : B = A
            if B == "D" : B = D
        elif len(move_c) > 0 :
            C = line.replace("C,", "")
        
        elif len(move_d) > 0 :
            D = line.replace("D,", "")
            if D == "A" : D = A
            if D == "B" : D = B
        
        elif line == "." :
            # a's
            if C == "a+" :
                    a = float(A)
                    b = float(B)
                    D = a + b
            elif C == "a-" :
                    a = float(A)
                    b = float(B)
                    D = a - b
            elif C == "a*" :
                    a = float(A)
                    b = float(B)
                    D = a * b
            elif C == "a/" :
                    a = float(A)
                    b = float(B)
                    D = a / b
            elif C == "a%" :
                    a = float(A)
                    b = float(B)
                    D = a % b
            # b's
            elif C == "b+" :
                    a = float(A)
                    b = float(B)
                    D = a + b
            elif C == "b-" :
                    a = float(A)
                    b = float(B)
                    D = a + b
            elif C == "b*" :
                    a = float(A)
                    b = float(B)
                    D = a * b
            elif C == "b/" :
                    a = float(A)
                    b = float(B)
                    D = a / b
            elif C == "b%" :
                    a = float(A)
                    b = float(B)
                    D = a % b
            # other
            elif C == "pa" : print(A)
            elif C == "pb" : print(B)
            elif C == "pd" : print(D)
            elif C == "in" : input()
            elif C == "i"  : input(B)
            elif C == "ia" : A = input(B)
            elif C == "ib" : B = input(A)
            elif C == "ga" : line_number = int(A) - 1
            elif C == "gb" : line_number = int(B) - 1
            elif C == "gd" : line_number = int(D) - 1
            elif C == "c"  : A,B,D = None
            elif C == "ca" : A = None
            elif C == "cb" : B = None
            elif C == "cd" : D = None
            elif C == "cls": system("cls")
            elif C == "q"  : exit()
            # file stuff
            elif C == "wf" :
                    file = open(A, "w")
                    file.write(B)
            elif C == "rf" :
                    file = open(A, "r")
                    D = file.read()
            elif C == "af" :
                    file = open(A, "a")
                    file.append(B)
            elif C == "cf" : file = open(A, "x")
            
            else : print("Invalid C Value")
                       
        else : print(f"SyntaxError : line {line_number+1}")
        
        line_number += 1
    
except TypeError : print(f"DataTypeError")
except ZeroDivisionError : print("ZeroDivisionError")
except FileExistsError : print("FileExistsError")
except FileNotFoundError : print("FileNotFoundError")
except KeyboardInterrupt : pass