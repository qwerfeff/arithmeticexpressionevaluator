def evaluate_binary_operation(num1, num2, operator):
   if not isinstance(num1,(float,int)) or not isinstance(num2,(float,int)):
       raise ValueError("Only int or float is valid for parameters ==> num1,num2 in function ==> evaluate binary operation")
   if operator not in ["^","/","*","+"]:
       raise ValueError("Only binary operators +,~,*,/,^ are valid for parameter ==> operator in function ==> evaluate binary operation")
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
       raise ValueError("Only operators +,~,*,/,^,(,) are valid for parameter ==> operator1,operator2 in function ==> precedence")
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
def factorial(input_number):
    position = input_number.find("!")
    if position != -1:
        number = (input_number[:position])
        if not number.isdigit():
            raise SyntaxError("The factorial function is only defined for non-negative integers")
        number = int(number)
        if number<0:
            raise SyntaxError("The factorial function is only defined for non-negative integers")
        if number == 1 or number == 0:
            return 1
        if number>1:
            i=number
            result=1
            while i > 1:
                result=result*i
                i=i-1
            return factorial(str(result)+input_number[position+1:])
    else:
        return input_number
def remove_all_instances(input_list,item):
   if not type(input_list) is list:
       raise ValueError("Only datatype:list is valid input for parameter ==> input_list in function ==> remove_all_instances")
   list_to_be_returned=[]
   for i in input_list:
       if i != item:
           list_to_be_returned.append(i)
   return list_to_be_returned
