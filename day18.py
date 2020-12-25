# Advent of Code - Day 18
# @curiouskiwi / @gary_anderson
# 25 Dec 2020  (This is part two ... completed part one on 18 Dec)


def main():

    with open("data.txt", "r") as f:
        lines = f.readlines()
    sum = 0
    for line in lines:
        sum += parseeq(line)
    print(sum)


def parseeq (text):
    while True:
        start = text.rfind('(')
        if start == -1:
            break
        end = text[start:].find(')')
        n = str(calc(text[start+1:start+end]))
        text = text[:start] + n + text[start+end+1:]

    return calc(text)


def calc(eq):

    parts = eq.split()
    print(parts)
    currentop = 'x'
    a = 0
    b = 0
    result = 0
    done = 0
    interim = 1
    for i, part in enumerate(parts):
        try:
            if currentop == 'x':
                a = int(part)
                result =a
            else:
                b = int(part)
                if currentop == '+':
                    result = calcit(result, b, currentop)
                else:
                    interim *= result
                    result = b
                currentop = 'x'
        except:
            if part in ['+', '*']:
                currentop = part
            elif part[0] == '(':
                new = ' '.join(parts[i:])
                pos = new.find(')')
                newl = new[1:pos]
                result = calcit( result, calc(newl),  currentop)
            else:
                if part[-1] == ')':
                    return result
                
    return result * interim


# ['10', '+', '5', '+', '8', '-', '12', '*', '5', '-', '(3', '+', '4)']

def calcit(a, b, op):
    if op == '+':
        return a+b
    elif op == '*':
        return a*b
    else:
        print("ERROR")
        return 0


main()
