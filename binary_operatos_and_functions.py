def evaluate_binary_operation(num1, num2, operator):
   if not isinstance(num1,(float,int)) or not isinstance(num2,(float,int)):
       raise SyntaxError("Only int or float is valid for parameters ==> num1,num2")
   if operator not in ["^","/","*","+"]:
       raise SyntaxError("Only binary operators +,~,*,/,^ are valid for parameter ==> operator")
   if operator == "+":
       return num1+num2
   if operator == "*":
       return num1*num2
   if operator == "/":
       if num2 != 0:
           return num1/num2
       else:
           raise ZeroDivisionError("Error cannot divide by zero")
   if operator == "^":
       result=num1**num2
       if type(result) is int or type(result) is float:
           return float(result)
       else:
           raise SyntaxError("Cannot do complex number algebra")
def precedence(operator1,operator2):
   if (operator1 or operator2) not in ["^","/","*","+","(",")"]:
       raise SyntaxError("Only operators +,~,*,/,^,(,) are valid for parameter ==> operator1,operator2")
   precedence_levels = {
       '+': 1,
       '*': 2,
       '/': 3,
       '^': 4,
       '(': 0,
       ')': 0
   }
   precedence_of_operator1 = precedence_levels.get(operator1)
   precedence_of_operator2 = precedence_levels.get(operator2)
   if precedence_of_operator1 > precedence_of_operator2:
       return 1
   if precedence_of_operator1 == precedence_of_operator2 and operator1 in ["/","*","+"]:
       return 1
   else:
       return 2
def remove_all_instances(input_list,item):
   list_to_be_returned=[]
   for i in input_list:
       if i != item:
           list_to_be_returned.append(i)
   return list_to_be_returned
