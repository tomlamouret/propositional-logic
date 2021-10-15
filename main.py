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
        if not "P" + str(i + 1) in sentence:
            string_to_print += "P" + str(i + 1) + " is missing from the propositional sentence.\n"
            ask_for_input = True
    for i in range(n + 1, n + 100):
        if "P" + str(i) in sentence:
            string_to_print += "P" + str(i) + " is not one of the propositional variables you originally declared.\n"
            ask_for_input = True
    if ask_for_input:
        print(string_to_print[0:len(string_to_print) - 1])
        return False
    else:
        return True


def simplify(sentence, n):
    operators = set()
    for i in range(n):
        operators.add('P' + str(i + 1))
    replaced = False
    i = 0
    while replaced != False and i < 2:
        if "!!" in sentence:
            sentence.replace("!!", '')
        if "!T" in sentence:
            sentence = sentence.replace("!T", 'F')
        if "!(T)" in sentence:
            sentence = sentence.replace("!(T)", 'F')
        if "!F" in sentence:
            sentence = sentence.replace("!F", 'T')
        if "!(F)" in sentence:
            sentence = sentence.replace("!(F)", 'T')

        if "(T&T)" in sentence:
            sentence = sentence.replace("(T&T)", 'T')
        if "(T&F)" in sentence:
            sentence = sentence.replace("(T&F)", 'F')
        if "(F&T)" in sentence:
            sentence = sentence.replace("(F&T)", 'F')
        if "(F&F)" in sentence:
            sentence = sentence.replace("(F&F)", 'F')
        if "T&T" in sentence:
            sentence = sentence.replace("T&T", 'T')
        if "T&F" in sentence:
            sentence = sentence.replace("T&F", 'F')
        if "F&T" in sentence:
            sentence = sentence.replace("F&T", 'F')
        if "F&F" in sentence:
            sentence = sentence.replace("F&F", 'F')
        if "(T)&T" in sentence:
            sentence = sentence.replace("(T)&T", 'T')
        if "(T)&F" in sentence:
            sentence = sentence.replace("(T)&F", 'F')
        if "(F)&T" in sentence:
            sentence = sentence.replace("(F)&T", 'F')
        if "(F)&F" in sentence:
            sentence = sentence.replace("(F)&F", 'F')
        if "T&(T)" in sentence:
            sentence = sentence.replace("T&(T)", 'T')
        if "T&(F)" in sentence:
            sentence = sentence.replace("T&(F)", 'F')
        if "F&(T)" in sentence:
            sentence = sentence.replace("F&(T)", 'F')
        if "F&(F)" in sentence:
            sentence = sentence.replace("F&(F)", 'F')

        if "(F|F)" in sentence:
            sentence = sentence.replace("(F|F)", 'F')
        if "(T|F)" in sentence:
            sentence = sentence.replace("(T|F)", 'T')
        if "(F|T)" in sentence:
            sentence = sentence.replace("(F|T)", 'T')
        if "(T|T)" in sentence:
            sentence = sentence.replace("(T|T)", 'T')
        if "F|F" in sentence:
            sentence = sentence.replace("F|F", 'F')
        if "T|F" in sentence:
            sentence = sentence.replace("T|F", 'T')
        if "F|T" in sentence:
            sentence = sentence.replace("F|T", 'T')
        if "T|T" in sentence:
            sentence = sentence.replace("T|T", 'T')
        if "(F)|F" in sentence:
            sentence = sentence.replace("(F)|F", 'F')
        if "(T)|F" in sentence:
            sentence = sentence.replace("(T)|F", 'T')
        if "(F)|T" in sentence:
            sentence = sentence.replace("(F)|T", 'T')
        if "(T)|T" in sentence:
            sentence = sentence.replace("(T)|T", 'T')
        if "F|(F)" in sentence:
            sentence = sentence.replace("F|(F)", 'F')
        if "T|(F)" in sentence:
            sentence = sentence.replace("T|(F)", 'T')
        if "F|(T)" in sentence:
            sentence = sentence.replace("F|(T)", 'T')
        if "T|(T)" in sentence:
            sentence = sentence.replace("T|(T)", 'T')

        if "(T>F)" in sentence:
            sentence = sentence.replace("(T>F)", 'F')
        if "(F>F)" in sentence:
            sentence = sentence.replace("(F>F)", 'T')
        if "(F>T)" in sentence:
            sentence = sentence.replace("(F>T)", 'T')
        if "(T>T)" in sentence:
            sentence = sentence.replace("(T>T)", 'T')
        if "T>F" in sentence:
            sentence = sentence.replace("T>F", 'F')
        if "F>F" in sentence:
            sentence = sentence.replace("F>F", 'T')
        if "F>T" in sentence:
            sentence = sentence.replace("F>T", 'T')
        if "T>T" in sentence:
            sentence = sentence.replace("T>T", 'T')
        if "(T)>F" in sentence:
            sentence = sentence.replace("(T)>F", 'F')
        if "(F)>F" in sentence:
            sentence = sentence.replace("(F)>F", 'T')
        if "(F)>T" in sentence:
            sentence = sentence.replace("(F)>T", 'T')
        if "(T)>T" in sentence:
            sentence = sentence.replace("(T)>T", 'T')
        if "T>(F)" in sentence:
            sentence = sentence.replace("T>(F)", 'F')
        if "F>(F)" in sentence:
            sentence = sentence.replace("F>(F)", 'T')
        if "F>(T)" in sentence:
            sentence = sentence.replace("F>(T)", 'T')
        if "T>(T)" in sentence:
            sentence = sentence.replace("T>(T)", 'T')
        i += 1
    return sentence


def next_proposition(sentence, truth_table, n):
    operators = {'!', '&', '|', '>'}
    o_n = 0
    for i in sentence:
        if i in operators:
            o_n += 1
    operands = {'T', 'F'}
    for i in range(n):
        operands.add('P' + str(i + 1))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i in sentence:
            operands.add(i)
    proposition = str()
    for i in operands:
        if "!(" + i + ")" in sentence:
            proposition = "!(" + i + ")"
            break
        if "!" + i in sentence:
            proposition = "!(" + i + ")"
            break
        if "(" + i + "&" in sentence:
            if sentence[sentence.index("(" + i + "&") + len(i) + 2] in {'(', '!'}:
                continue
            else:
                for j in operands:
                    if j == sentence[sentence.index("(" + i + "&") + len(i) + 2: sentence.find(')', sentence.index(
                            "(" + i + "&") + len(i) + 2, len(sentence))]:
                        proposition = "(" + i + "&" + j + ")"
                        break
        if i + "&" in sentence:
            if sentence[sentence.index(i + "&") + len(i) + 1] in {'(', '!'}:
                continue
            else:
                for j in operands:
                    for k in operators:
                        if k in sentence and j == sentence[
                                                  sentence.index(i + "&") + len(i) + 1: sentence.find(k, sentence.index(
                                                          i + "&") + len(i) + 1, len(sentence))]:
                            proposition = i + "&" + j
                            break
        if "(" + i + "|" in sentence:
            if sentence[sentence.index("(" + i + "|") + len(i) + 2] in {'(', '!'}:
                continue
            else:
                for j in operands:
                    if j == sentence[sentence.index("(" + i + "|") + len(i) + 2: sentence.find(')', sentence.index(
                            "(" + i + "|") + len(i) + 2, len(sentence))]:
                        proposition = "(" + i + "|" + j + ")"
                        break
        if i + "|" in sentence:
            if sentence[sentence.index(i + "|") + len(i) + 1] in {'(', '!'}:
                continue
            else:
                for j in operands:
                    for k in operators:
                        if k in sentence and j == sentence[
                                                  sentence.index(i + "|") + len(i) + 1: sentence.find(k, sentence.index(
                                                          i + "|") + len(i) + 1, len(sentence))]:
                            proposition = i + "|" + j
                            break
        if "(" + i + ">" in sentence:
            if sentence[sentence.index("(" + i + ">") + len(i) + 2] in {'(', '!'}:
                continue
            else:
                for j in operands:
                    if j == sentence[sentence.index("(" + i + ">") + len(i) + 2: sentence.find(')', sentence.index(
                            "(" + i + ">") + len(i) + 2, len(sentence))]:
                        proposition = "(" + i + ">" + j + ")"
                        break
        if i + ">" in sentence:
            if sentence[sentence.index(i + ">") + len(i) + 1] in {'(', '!'}:
                continue
            else:
                for j in operands:
                    for k in operators:
                        if k in sentence and j == sentence[
                                                  sentence.index(i + ">") + len(i) + 1: sentence.find(k, sentence.index(
                                                          i + ">") + len(i) + 1, len(sentence))]:
                            proposition = i + ">" + j
                            break
    if o_n > 1:
        letter = 'a'
        for i in truth_table:
            if i is not None:
                if i[0] == letter:
                    letter = alphabet[alphabet.find(letter) + 1]
        sentence = sentence.replace(proposition, letter)
    else:
        letter = '?'
    if proposition[0] != '(' and proposition[len(proposition) - 1] != ')':
        proposition = '(' + proposition + ')'
    to_return = [sentence, proposition, letter]
    return to_return


def update_table(truth_table, proposition, letter):
    index = int
    if truth_table[0][0] != "P1":
        index = 2
    else:
        index = 1
    operator = ''
    operand = []
    if '!' in proposition:
        operator = '!'
        operand.append(proposition[proposition.index('(') + 1:proposition.index(')')])
        operand.append("null")
        proposition = operator + operand[0]
    elif '&' in proposition:
        operator = '&'
        operand.append(proposition[proposition.index('(') + 1:proposition.index('&')])
        operand.append(proposition[proposition.index('&') + 1:proposition.index(')')])
        proposition = operand[0] + operator + operand[1]
    elif '|' in proposition:
        operator = '|'
        operand.append(proposition[proposition.index('(') + 1:proposition.index('|')])
        operand.append(proposition[proposition.index('|') + 1:proposition.index(')')])
        proposition = operand[0] + operator + operand[1]
    elif '>' in proposition:
        operator = '>'
        operand.append(proposition[proposition.index('(') + 1:proposition.index('>')])
        operand.append(proposition[proposition.index('>') + 1:proposition.index(')')])
        proposition = operand[0] + operator + operand[1]
    indexes = [-1, -1]
    i = 0
    if index == 1:
        while truth_table[i][0] != ' ' and i < len(truth_table):
            i += 1
        truth_table[i][0] = proposition
    else:
        while truth_table[i][1] != ' ' and i < len(truth_table):
            i += 1
        if truth_table[i - 1][1] == proposition:
            truth_table.remove(truth_table[i])
            return truth_table
        truth_table[i][1] = proposition
        if letter != '?':
            truth_table[i][0] = letter
    for j in truth_table:
        if j is not None:
            if index == 1:
                if j[0] == operand[0]:
                    indexes[0] = truth_table.index(j)
                if j[0] == operand[1]:
                    indexes[1] = truth_table.index(j)
            else:
                if j[0] == operand[0] or j[1] == operand[0]:
                    indexes[0] = truth_table.index(j)
                if j[0] == operand[1] or j[1] == operand[1]:
                    indexes[1] = truth_table.index(j)
    for k in range(index, len(truth_table[0])):
        if operator == '!':
            if truth_table[indexes[0]][k] == 'T':
                truth_table[i][k] = 'F'
            else:
                truth_table[i][k] = 'T'
        elif operator == '&':
            if truth_table[indexes[0]][k] == 'T' and truth_table[indexes[1]][k] == 'T':
                truth_table[i][k] = 'T'
            else:
                truth_table[i][k] = 'F'
        elif operator == '|':
            if truth_table[indexes[0]][k] == 'F' and truth_table[indexes[1]][k] == 'F':
                truth_table[i][k] = 'F'
            else:
                truth_table[i][k] = 'T'
        elif operator == '>':
            if truth_table[indexes[0]][k] == 'T' and truth_table[indexes[1]][k] == 'F':
                truth_table[i][k] = 'F'
            else:
                truth_table[i][k] = 'T'
    return truth_table


def print_truth_table(truth_table, indexes):
    for j in range(indexes[1]):
        row = str()
        for i in range(len(truth_table)):
            if truth_table[i] is not None:
                column_width = len(truth_table[i][indexes[0] - 1])
                if len(truth_table[i][j]) == column_width:
                    row += truth_table[i][j] + ' '
                else:
                    row += ' ' * (column_width - len(truth_table[i][j]) - round(
                        (column_width - len(truth_table[i][j])) / 2)) + truth_table[i][j] + ' ' * round(
                        (column_width - len(truth_table[i][j])) / 2) + ' '
        print(row)
        if truth_table[i] is not None:
            if j == indexes[0] - 1:
                dashes = str()
                for k in range(len(truth_table)):
                    dashes += '-' * (len(truth_table[k][indexes[0] - 1]) + 1)
                dashes = dashes[0:len(dashes) - 1]
                print(dashes)


n = input("Please enter a number n of propositional variables:\n")
while not (n.isdigit()) or int(n) == 0:
    print("The number must be entered as an integer, greater or equal to 1.")
    n = input("Please enter a number n of propositional variables:\n")
proposition_width = len(n) + 1
n = int(n)

sentence = input('''Please enter a propositional sentence using '|' for disjunction, '&' for conjunction, '!' for 
negation, '>' for condition, 'T' for True and 'F' for False:\n''')
while not is_input_valid(sentence):
    sentence = input('''Please enter a propositional sentence using '|' for disjunction, '&' for conjunction, '!' for 
negation, '>' for condition, 'T' for True and 'F' for False:\n''')
S = simplify(sentence, n)
if S[0] != '(' or S[len(S) - 1] != ')':
    S = '(' + S + ')'
o_n = 0
operators = {'|', '&', '!', '>'}
for i in sentence:
    if i in operators:
        o_n += 1
truth_table = [None] * (n + o_n)
indexes = list()
for i in range(n + o_n):
    if 0 <= o_n <= 1:
        truth_table[i] = [' '] * (2 ** n + 1)
        indexes.append(1)
        indexes.append(2 ** n + 1)
    else:
        truth_table[i] = [' '] * (2 ** n + 2)
        indexes.append(2)
        indexes.append(2 ** n + 2)
    if i in range(n):
        if 0 <= o_n <= 1:
            truth_table[i][0] = "P" + str(i + 1)
        else:
            truth_table[i][1] = "P" + str(i + 1)
        truth_value = True
        repeats = int(2 ** n / 2 ** (i + 1))
        counter = 0
        for j in range(indexes[0], indexes[1]):
            if counter == repeats:
                if truth_value:
                    truth_value = False
                    counter = 0
                else:
                    truth_value = True
                    counter = 0
            if truth_value and counter < repeats:
                truth_table[i][j] = 'T'
                counter += 1
            elif not truth_value and counter < repeats:
                truth_table[i][j] = 'F'
                counter += 1
        truth_value = True
    else:
        SPL = next_proposition(S, truth_table, n)
        m = 0
        S = SPL[0]
        truth_table = update_table(truth_table, SPL[1], SPL[2])
print("The truth table for the propositional sentence is:")
print_truth_table(truth_table, indexes)
tautology_or_contradiction = bool
for i in range(indexes[0] + 1, indexes[1]):
    if truth_table[len(truth_table) - 1][i] != truth_table[len(truth_table) - 1][indexes[0]]:
        tautology_or_contradiction = False
        break

if not tautology_or_contradiction:
    print("The propositional sentence is a contingency.")
elif truth_table[len(truth_table) - 1][indexes[0]] == 'T':
    print("The propositional sentence is a tautology.")
else:
    print("The propositional sentence is a contradiction.")
