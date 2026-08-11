#MATCH CASE STATEMENT
x=9
match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case 5:
        print("x is <10")
    case _:
        print(x) 