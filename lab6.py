from calc import *
import copy


def exec_program(input, dic = None):
    """ Executes the program """

    if not dic:
        my_table = {}
    else:
        my_table = dic


    if is_program(input) == True:
        return exec_statments(program_statements(input), my_table)   
    else:
        raise ValueError
    


def exec_statments(input, dic):
    """ Executes statements """

    if empty_statements(input) == True:
        return dic

    if is_statements(input) == True:
        statement = first_statement(input)
        return exec_statments(rest_statements(input), exec_statement(statement, dic))
    else:
        raise ValueError



def exec_statement(statement, dic):
    """ Checks eval for the true input """

    if is_variable(first_statement(statement)):
        if is_output(statement) == True:
            return eval_output(statement, dic)

        if is_selection(statement) == True:
            return eval_selection(statement, dic)
        
        if is_assignment(statement) == True:
            return exec_assignment(statement, dic)
        
        if is_input(statement) == True:
            return eval_input(statement, dic)

        if is_repetition(statement) == True:
            return eval_repetition(statement, dic)
        
        else:
            raise TypeError
        
    else:
        raise ValueError



def eval_variable(variable, dic):
    """ Returns variable value """
    
    if variable in dic.keys():
        return dic[variable]
    else:
        return variable



def eval_binaryoper(expr):
    """ Calculates the expression"""

    if binaryexpr_operator(expr) == "+":
        return binaryexpr_left(expr) + binaryexpr_right(expr)
    elif binaryexpr_operator(expr) == "-":
        return binaryexpr_left(expr) - binaryexpr_right(expr)
    elif binaryexpr_operator(expr) == "*":
        return binaryexpr_left(expr) * binaryexpr_right(expr)
    elif binaryexpr_operator(expr) == "/":
        return binaryexpr_left(expr) / binaryexpr_right(expr)
    else:
        raise ValueError ("Not a correct binaryoper")
    

def eval_condoper(expr):
    """ Calculates expression """
    
    if condition_operator(expr) == "<":
        if condition_left(expr) < condition_right(expr):
            return True
        else:
            return False
    elif condition_operator(expr) == '>':
        if condition_left(expr) > condition_right(expr):
            return True
        else:
            return False
    elif condition_operator(expr) == '=':
        if condition_left(expr) == condition_right(expr):
            return True
        else:
            return False
    else:
        raise ValueError ("Not a correct condoper!")



def eval_output(expr, dic):
    """ Evaluates output """
    
    if is_constant(output_expression(expr)) == True:
        print(output_expression(expr))

    elif is_variable(output_expression(expr)) == True:
        print(output_expression(expr), '=', eval_variable(output_expression(expr), dic))

        
    else:
        print(eval_binaryoper(eval_statement(output_expression(expr), dic)))
    return dic



def eval_selection(expr, dic):
    """ Evaluates selection """
    
    if is_selection(expr) == True and not selection_has_false_branch(expr): 
        
        if eval_condoper(eval_statement(selection_condition(expr), dic)) == True:
            return exec_statement(selection_true_branch(expr), dic)
        else:
            return dic

    elif is_selection(expr) == True and selection_has_false_branch(expr) == True: 
        if eval_condoper(eval_statement(selection_condition(expr), dic)) == True:
            return exec_statement(selection_true_branch(expr), dic)
        else:
            return exec_statement(selection_false_branch(expr), dic)



def exec_assignment(expr, dic):
    """ Assings variable in dictionary to assigned value """
    
    new_dic = copy.deepcopy(dic)
    new_dic[assignment_variable(expr)] = eval_assignment(assignment_expression(expr), new_dic)
    
    return new_dic


def eval_input(expr, dic):
    """ Assigns the input to variable in dictionary """

    new_dic = copy.deepcopy(dic)
    new_dic[input_variable(expr)] = get_input(input_variable(expr)) 
    return new_dic
        

def eval_repetition(expr, dic):
    """ Returns statements until repetition condition is false """

    new_dic = copy.deepcopy(dic)  
    if eval_assignment(repetition_condition(expr), new_dic) == False:
        return new_dic    
    
    return exec_statement(expr, exec_statments(repetition_statements(expr), new_dic))


def get_input(variable):
    """ When 'read', enters input """

    return int(input("Enter value for " + variable + ": "))



def eval_assignment(expr, dic):
    """ Help function for assignment """
    if is_constant(expr) == True:
        return expr
    
    if is_condition(expr) == True:
        if is_binaryexpr(binaryexpr_left(expr)):
            return eval_assignment([eval_assignment(binaryexpr_left(expr), dic)] + rest_statements(expr), dic) 
        if is_binaryexpr(binaryexpr_right(expr)):
            return eval_assignment([binaryexpr_left(expr)] + [binaryexpr_operator(expr)] + [eval_assignment(binaryexpr_right(expr), dic)], dic)
            
        else:
            return eval_condoper(eval_statement(expr, dic))


    if is_binaryoper(binaryexpr_operator(expr)) == True:
        if is_binaryexpr(binaryexpr_left(expr)):
            return eval_assignment([eval_assignment(binaryexpr_left(expr), dic)] + rest_statements(expr), dic) 
        if is_binaryexpr(binaryexpr_right(expr)):
            return eval_assignment([binaryexpr_left(expr)] + [binaryexpr_operator(expr)] + [eval_assignment(binaryexpr_right(expr), dic)], dic)        
        else:
            return eval_binaryoper(eval_statement(expr, dic))
        
    else:
        raise TypeError



def eval_statement(statement, dic):
    """ Checks if statements are in dictionary """
    if binaryexpr_left(statement) in dic.keys():
        left = dic[binaryexpr_left(statement)]
    else:
        left = binaryexpr_left(statement)

    if binaryexpr_right(statement) in dic.keys():
        right = dic[binaryexpr_right(statement)]
    else:
        right = binaryexpr_right(statement)

    return  [left] + [binaryexpr_operator(statement)] + [right]




""" Different inputs """

calc1 = ['calc', ['print', 2], ['print', 7]] # 2, 7
calc2 = ['calc', ['if', ['x', '>', 'y'],['print', 2], ['print', 4]]] # False, 4
calc3 = ['calc', ['if', [9, '>', 8],['print', 2], ['print', 4]]] # True, 2
calc4 = ['calc', ['print', [2, "+", 4]]] # 6
calc5 = ['calc', ['if', [5, '=', 5], ['print', [2, '*', 5]], ['print', [4, '/', 2]]]] # 10

calc6 = ['calc', ['set', "x", [8, '-', 2]], ['print', 'x']] # x = 6
calc7 = ['calc', ['set', 'x', 7], ['set', 'y', 12], ['set', 'z', ['x', '+', 'y']], ['print', 'z']] # z = 19
calc9 = ['calc', ['if', [8, '>', 8],['print', 2]]] # None, false
calc10 = ['calc', ['read', 'p1'],  ['set', 'p2', 47], ['set', 'p3', 179], ['set', 'result', [['p1', '*', 'p2'], '-', 'p3']], ['print', 'result']] # result = 9, if p1 = 4
calc11 = ['calc', ['read', 'n'], ['set', 'sum', 0], ['while', ['n', '>', 0], ['set', 'sum', ['sum', '+', 'n']], ['set', 'n', ['n', '-', 1]]], ['print', 'sum']] # sum = 3, n = 2

calc12 = [
        "calc",
        ["read", "x"],
        ["if", ["x", ">", 0], ["set", "a", 1], ["set", "a", -1]],
        ["if", ["x", "=", 0], ["set", "a", 0]], ['print', 'a']
    ] # {'x': 0, 'a': 0} x = 0, {'x': -1, 'a': -1} if x = -1 or lower, 

calc13 = [
        "calc",
        ["read", "x"],
        ["set", "zero", 0],
        ["set", "pos", 1],
        ["set", "nonpos", -1],
        ["if", ["x", "=", 0], ["print", "zero"]],
        ["if", ["x", ">", 0], ["print", "pos"]],
        ["if", ["x", "<", 0], ["print", "nonpos"]],] #  if x = 3, pos = 1, {'x': 3, 'zero': 0, 'pos': 1, 'nonpos': -1}

calc14 = ['calc', ['set', 'x', [3, '+', [3, '*', 2]]], ['print', 'x']]

calc1002 = ['calc', ['print', [4, '-', 2]]] # 2
calc1003 = ['calc', ['print', ['y', '-', 'x']]] # 4
calc1004 = ['calc', ['print', 4]] # 4
calc1005 = ['calc', ['print', 'y']] # 9
tablos = {'x': 5, 'y': 9}

#exec_program(calc14)
#return eval_assignment(exp[:2] + [eval_assignment(binaryexpr_right(expr), dic)], dic)
            #return eval_assignment(expr[:2] + [eval_assignment(binaryexpr_right(expr), dic)], dic)

""" Exception """

error1 = ['print', 4] # no calc
error2 = ['calc'] # no statements
error3 = ['calc', ['if', [9, ';', 8],['print', 2], ['print', 4]]] # Not a binaryoper/condoper,  2
error4 = ['calc', ['print', [2, "_", 4]]] # not a binaryoper/condoper
error5 = ['calc', []] # empty statements
error6 = ['calc', ['if', [], ['print', 1]]] # empty statement for if
error7 = ['calc', ['if', [5, '>', 3], [4]]] # no print or similar