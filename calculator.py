import logging
logging.basicConfig(level=logging.DEBUG)

def add(a, b, *args):
    return a + b + sum(args)

def sub(a, b):
    return a - b

def mult(a, b, *args):
    result = a * b
    for i in args:
        result *= i
    return result

def div(a, b):
    return a / b

def check_user_input_float(input):
    try:
        float(input)
        return True
    except ValueError:
        return False 

def check_user_input_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

operations = {
    "1": add,
    "2": sub,
    "3": mult,
    "4": div
    }

operations_instruction = '''Enter the operation number:
      1 (add)
      2 (subtraction)
      3 (multiplication)
      4 (division)'''

op_log_info = {
        "1": "You have chosen addition.",
        "2": "You have chosen subtraction.",
        "3": "You have chosen multiplication.",
        "4": "You have chosen division."
        }

def get_data():
    op = input(operations_instruction)
    while op not in operations:
        print ("Enter a number from 1 to 4")
        op = input(operations_instruction)
    logging.info(op_log_info[op])
    args=[]
    if op in ("1", "3"):
        how_many_num = (input("How many numbers do you need in your operation? "))
        while check_user_input_int(how_many_num) == False:
            logging.info("You have not entered an integer. Enter an integer.")
            how_many_num = input("How many numbers do you need in your operation? ")
        how_many_num = int(how_many_num) 
        for i in range (how_many_num-2):
            x = input("Enter a number: ")
            while check_user_input_float(x) == False:
                logging.info("You have not entered a number. Enter a number")
                x = input("Enter a number: ")
            x = float(x)
            args.append(x)
      
    a = input("Enter a number: ")
    while check_user_input_float(a) == False:
        logging.info("You have not entered a number. Enter a number.")
        a = input("Enter a number: ")
    a = float(a)
       
    b = input("Enter a number: ")
    while check_user_input_float(b) == False:
        logging.info("You have not entered a number. Enter a number.")
        b = input("Enter a number: ")
    b = float(b)
    while op == "4" and b == 0:
        logging.warning("Cannot divide by 0. Please choose a different number.")
        b = input("Enter a number: ")
        while check_user_input_float(b) == False:
            logging.info("You have not entered a number. Enter a number.")
            b = input("Enter a number: ")
        b = float(b)
   
    return op, a, b, args
    
def go():
    operation, a, b, args = get_data()
    result = operations[operation](a, b, *args)
    print ("the result is: ", "%.2f" % result)
    return result


if __name__ == "__main__":
    go()