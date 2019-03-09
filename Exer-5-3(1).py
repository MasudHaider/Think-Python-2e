def is_triangle(length1, length2, length3):
    case1 = length1 + length2
    case2 = length1 + length3
    case3 = length2 + length3
    if length1 > case3 or length2 > case2 or length3 > case1:
        print("No")
    elif length1 == case3 or length2 == case2 or length3 == case1:
        print("Degenerate triangle")
    else:
        print("Yes")


prompt = "Enter value for length1: "
a = int(input(prompt))
prompt = "Enter value for length2: "
b = int(input(prompt))
prompt = "Enter value for length3: "
c = int(input(prompt))

is_triangle(a, b, c)
