def interpret(source):
    """ An interpreter for a language truly ahead of its time; brainfuck """
    array = [0]*30000
    ptr = 0
    stack = []
    i = 0
    while i < len(source):
        lexeme = source[i]
        if lexeme == ">":
            ptr += 1
            if not ptr < len(array):
                array.append(0)
        elif lexeme == "<":
            ptr -= 1
        elif lexeme == "+":
            array[ptr] += 1
        elif lexeme == "-":
            old = array[ptr]
            array[ptr] -= 1
        elif lexeme == ".":
            print(chr(array[ptr]), end="")
        elif lexeme == ",":
            array[ptr] = ord(input(">")[0])
        elif lexeme == "[":
            if array[ptr] != 0:
                stack.append(i)
            elif array[ptr] == 0:
                i += 1
                open_brackets = 0
                while True:
                    if source[i] == "[":
                        open_brackets += 1
                    elif source[i] == "]":
                        if open_brackets:
                            open_brackets -= 1
                        else:
                            i += 1
                            break
                    i += 1
                continue
        elif lexeme == "]" and stack:
            i = stack.pop()
            continue
        elif lexeme == "#":
            for i, val in enumerate(array):
                if val != 0:
                    print(i,val)
        i += 1
