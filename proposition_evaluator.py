def is_input_valid(string):
    ob_n = cb_n = o_n = 0
    operators = {'|', '&', '!', '>'}
    operators_and_operands = {'P', 'T', 'F', '|', '&', '!', '>'}
    ask_for_input = False
    string_to_print = str()
    invalid_inputs = list()
    if string == "":
        print("You must type something.")
        return False
    for i in string:
        if i == '(':
            ob_n += 1
        elif i == ')':
            cb_n += 1
        elif i in operators:
            o_n += 1
        elif i not in operators_and_operands and not i.isdigit():
            if i == ' ':
                invalid_inputs.append("spaces")
            else:
                invalid_inputs.append(i)
    if cb_n > ob_n:
        if cb_n == ob_n + 1:
            string_to_print += "Missing opening bracket.\n"
        else:
            string_to_print += "Missing opening brackets.\n"
        ask_for_input = True
    elif cb_n < ob_n:
        if ob_n == cb_n + 1:
            string_to_print += "Missing closing bracket.\n"
        else:
            string_to_print += "Missing closing brackets.\n"
        ask_for_input = True
    # elif ob_n < o_n - 1:
    #     string_to_print += "Make sure the expression is fully parenthesized.\n"
    #     ask_for_input = True
    if not len(invalid_inputs) == 0:
        string_to_print = string_to_print + "The following inputs are invalid: " + ', '.join(invalid_inputs) + ".\n"
        ask_for_input = True
    for i in range(n):
        if not "P" + str(i + 1) in S:
            string_to_print += "P" + str(i + 1) + " is missing from the propositional sentence.\n"
            ask_for_input = True
    for i in range(n + 1, n + 100):
        if "P" + str(i) in S:
            string_to_print += "P" + str(i) + " is not one of the propositional variables you originally declared.\n"
            ask_for_input = True
    if ask_for_input:
        print(string_to_print[0:len(string_to_print) - 1])
        return False
    else:
        return True


def has_precedence(operator_1, operator_2):
    if operator_1 == '!':
        if operator_2 == '!':
            return True
        else:
            return False
    elif operator_1 == '&':
        if operator_2 == '!' or operator_2 == '&':
            return True
        else:
            return False
    elif operator_1 == '|':
        if operator_2 == '!' or operator_2 == '&' or operator_2 == '|':
            return True
        else:
            return False
    elif operator_1 == '>':
        if operator_2 == '!' or operator_2 == '&' or operator_2 == '|' or operator_2 == '>':
            return True
        else:
            return False

n = input("Please enter a number n of propositional variables:\n")

while not n.isdigit():
    if n.isdigit() and int(n) == 0:
        break
    print("The number must be entered as an integer.")
    n = input("Please enter a number n of propositional variables:\n")
n = int(n)
TF_values = list(())
if n != 0:
    print("Please enter the truth values of the propositional variables: 'T' or 'F':")
    for i in range(n):
        value = input("P" + str(i + 1) + "=")
        if value == "T":
            TF_values.append(True)
        elif value == "F":
            TF_values.append(False)
        else:
            print("The truth value must be entered as 'T' or 'F'.")
            while value != ("T" or "F"):
                value = input("P" + str(i + 1) + "=")
                print("The truth value must be entered as 'T' or 'F'.")
            if value == "T":
                TF_values.append(True)
            elif value == "F":
                TF_values.append(False)
S = input('''Please enter a propositional sentence using '|' for disjunction, '&' for conjunction, '!' for negation, 
'>' for condition, 'T' for True and 'F' for False:\n''')
while not is_input_valid(S):
    S = input('''Please enter a propositional sentence using '|' for disjunction, '&' for conjunction, '!' for negation,
'>' for condition, 'T' for True and 'F' for False:\n''')
for i in reversed(range(n)):
    if TF_values[i]:
        S = S.replace("P" + str(i + 1), "T")
    elif not TF_values[i]:
        S = S.replace("P" + str(i + 1), "F")
while not (S == 'T' or S == 'F' or S == '(T)' or S == '(F)'):
    if "!!" in S:
        S = S.replace("!!", '')
    if "!T" in S:
        S = S.replace("!T", 'F')
    if "!(T)" in S:
        S = S.replace("!(T)", 'F')
    if "!F" in S:
        S = S.replace("!F", 'T')
    if "!(F)" in S:
        S = S.replace("!(F)", 'T')

    if "(T&T)" in S:
        S = S.replace("(T&T)", 'T')
    if "(T&F)" in S:
        S = S.replace("(T&F)", 'F')
    if "(F&T)" in S:
        S = S.replace("(F&T)", 'F')
    if "(F&F)" in S:
        S = S.replace("(F&F)", 'F')
    if "T&T" in S:
        S = S.replace("T&T", 'T')
    if "T&F" in S:
        S = S.replace("T&F", 'F')
    if "F&T" in S:
        S = S.replace("F&T", 'F')
    if "F&F" in S:
        S = S.replace("F&F", 'F')
    if "(T)&T" in S:
        S = S.replace("(T)&T", 'T')
    if "(T)&F" in S:
        S = S.replace("(T)&F", 'F')
    if "(F)&T" in S:
        S = S.replace("(F)&T", 'F')
    if "(F)&F" in S:
        S = S.replace("(F)&F", 'F')
    if "T&(T)" in S:
        S = S.replace("T&(T)", 'T')
    if "T&(F)" in S:
        S = S.replace("T&(F)", 'F')
    if "F&(T)" in S:
        S = S.replace("F&(T)", 'F')
    if "F&(F)" in S:
        S = S.replace("F&(F)", 'F')

    if "(F|F)" in S:
        S = S.replace("(F|F)", 'F')
    if "(T|F)" in S:
        S = S.replace("(T|F)", 'T')
    if "(F|T)" in S:
        S = S.replace("(F|T)", 'T')
    if "(T|T)" in S:
        S = S.replace("(T|T)", 'T')
    if "F|F" in S:
        S = S.replace("F|F", 'F')
    if "T|F" in S:
        S = S.replace("T|F", 'T')
    if "F|T" in S:
        S = S.replace("F|T", 'T')
    if "T|T" in S:
        S = S.replace("T|T", 'T')
    if "(F)|F" in S:
        S = S.replace("(F)|F", 'F')
    if "(T)|F" in S:
        S = S.replace("(T)|F", 'T')
    if "(F)|T" in S:
        S = S.replace("(F)|T", 'T')
    if "(T)|T" in S:
        S = S.replace("(T)|T", 'T')
    if "F|(F)" in S:
        S = S.replace("F|(F)", 'F')
    if "T|(F)" in S:
        S = S.replace("T|(F)", 'T')
    if "F|(T)" in S:
        S = S.replace("F|(T)", 'T')
    if "T|(T)" in S:
        S = S.replace("T|(T)", 'T')

    if "(T>F)" in S:
        S = S.replace("(T>F)", 'F')
    if "(F>F)" in S:
        S = S.replace("(F>F)", 'T')
    if "(F>T)" in S:
        S = S.replace("(F>T)", 'T')
    if "(T>T)" in S:
        S = S.replace("(T>T)", 'T')
    if "T>F" in S:
        S = S.replace("T>F", 'F')
    if "F>F" in S:
        S = S.replace("F>F", 'T')
    if "F>T" in S:
        S = S.replace("F>T", 'T')
    if "T>T" in S:
        S = S.replace("T>T", 'T')
    if "(T)>F" in S:
        S = S.replace("(T)>F", 'F')
    if "(F)>F" in S:
        S = S.replace("(F)>F", 'T')
    if "(F)>T" in S:
        S = S.replace("(F)>T", 'T')
    if "(T)>T" in S:
        S = S.replace("(T)>T", 'T')
    if "T>(F)" in S:
        S = S.replace("T>(F)", 'F')
    if "F>(F)" in S:
        S = S.replace("F>(F)", 'T')
    if "F>(T)" in S:
        S = S.replace("F>(T)", 'T')
    if "T>(T)" in S:
        S = S.replace("T>(T)", 'T')
if S == 'T' or S == '(T)':
    print("The propositional sentence is true.")
else:
    print("The propositional sentence is false.")
