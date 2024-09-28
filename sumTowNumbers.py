def sum(num1, num2):
    try :
        return int(num1) + int(num2)
    except ValueError:
        return "You must enter numbers !"
