from streamlit import number_input


HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE,'r')
    lines = file.readline()
    if len(lines) == 0:
        print(" NO history found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file  = open(HISTORY_FILE,'w')
    file.close()
    print("hisory cleared")

def save_history(equation,result):
    file = open(HISTORY_FILE,'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print('Invalid input.use format: number operator number(e.g 8+8)') 
        return
    # num1 = float(parts[0])
    # op = parts[1]
    # num2 = float(parts[2])
def calculate(expression):
    try:
        # Evaluate the full expression securely
        result = eval(expression, {"__builtins__": None}, {})
        print("Result:", result)
        save_history(expression, result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except Exception as e:
        print("Error evaluating expression:", e) 
    
    # if int(result) == result:
    #     result = int(result)
    # print("Result:",result)
    # save_history(number_input, result)

def main():
    print('---SIMPLE CALCULATOR (type history,clear or exit)')
    while True:
        user_input = input("enter calculation (+ - * /) or command (history, clear or exit)")
        if user_input == 'exit':
            print('GOOD BYE')
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)

main()   