import time
from tokenizer import tokenize_expression
from datastructures import Stack,Queue,ArithmeticExpression
from binary_operators_and_functions import evaluate_binary_operation,precedence,remove_all_instances
def measure_time(function):
    def wrapper(args,**kwargs):
        start=time.time()
        function(args, **kwargs)
        end=time.time()
        print(f"Execution time for {function.__name__}() is {end-start} seconds")
        return function(args,**kwargs)
    return wrapper
def evaluate_simple_arithmetic_expression(expression):
   tokenized_expression=expression
   for operator in "^/*+":
       stack = Stack()
       if operator in "/*+":
           for i in range(len(tokenized_expression)):
               if i % 2 != 0 and i >= 3:
                   num2 = stack.pop()
                   popped_operator = stack.pop()
                   num1 = stack.pop()
                   if popped_operator == operator:
                       stack.push(str(evaluate_binary_operation(float(num1), float(num2), popped_operator)))
                   else:
                       stack.push(num1)
                       stack.push(popped_operator)
                       stack.push(num2)
                   stack.push(tokenized_expression[i])
               else:
                   stack.push(tokenized_expression[i])
           tokenized_expression = stack.items
       else:
           for i in range(len(tokenized_expression)-1,-1,-1):
               if i % 2 != 0 and i <= len(tokenized_expression)-4:
                   num1=stack.pop()
                   popped_operator=stack.pop()
                   num2=stack.pop()
                   if popped_operator == operator:
                       stack.push(str(evaluate_binary_operation(float(num1), float(num2), popped_operator)))
                   else:
                       stack.push(num2)
                       stack.push(popped_operator)
                       stack.push(num1)
                   stack.push(tokenized_expression[i])
               else:
                   stack.push(tokenized_expression[i])
           stack.items.reverse()
           tokenized_expression=stack.items
   return str(tokenized_expression[0])
@measure_time
def evaluate_arithmetic_expression(expression):
   input_expression=expression
   input_expression = input_expression.replace(" ", "")
   input_expression = input_expression.replace("~", "+-")
   input_expression = input_expression.replace("--", "")
   tokenized_expression=tokenize_expression(input_expression,"^/*+()")
   tokenized_expression=remove_all_instances(tokenized_expression,'')
   stack=Stack()
   expression_in_brackets=["0","+"]
   for i in range(len(tokenized_expression)):
       if tokenized_expression[i] == ")":
           while not stack.peek() == "(":
               expression_in_brackets.append(stack.pop())
           stack.pop()
           expression_in_brackets.reverse()
           expression_in_brackets=["0","+"]+expression_in_brackets
           value_of_expression_in_brackets=evaluate_simple_arithmetic_expression(expression_in_brackets)
           expression_in_brackets=["0","+"]
           stack.push(value_of_expression_in_brackets)
       else:
           stack.push(tokenized_expression[i])
   stack.push("+")
   stack.push("0")
   return evaluate_simple_arithmetic_expression(["0","+"]+stack.items)
def postfix_converter(expression):
   input_expression=expression.replace(" ","")
   input_expression=input_expression.replace("~","+-")
   input_expression=input_expression.replace("--","")
   operator_stack=Stack()
   queue=Queue()
   number=""
   for i in range(len(input_expression)):
       if input_expression[i] == "(":
           operator_stack.push("(")
       elif input_expression[i] == ")":
           while operator_stack.peek() != "(":
               popped_operator=operator_stack.pop()
               queue.enqueue(popped_operator)
           operator_stack.pop()
       elif input_expression[i] in ["^","/","*","+"]:
           if operator_stack.is_empty():
               operator_stack.push(input_expression[i])
           elif precedence(operator_stack.peek(),input_expression[i]) == 1:
               while not operator_stack.is_empty() and precedence(operator_stack.peek(), input_expression[i]) == 1:
                   popped_operator=operator_stack.pop()
                   queue.enqueue(popped_operator)
               operator_stack.push(input_expression[i])
           elif precedence(operator_stack.peek(),input_expression[i]) == 2:
               operator_stack.push(input_expression[i])
       elif input_expression[i].isdigit() or input_expression[i] == "-" or input_expression[i] == ".":
           number = number + input_expression[i]
           if i+1 < len(input_expression):
               if input_expression[i+1] in ["^","/","*","+","(",")"]:
                   queue.enqueue(float(number))
                   number=""
           if i == len(input_expression)-1:
               queue.enqueue(float(number))
   while not operator_stack.is_empty():
       popped_operator=operator_stack.pop()
       queue.enqueue(popped_operator)
   return queue
def postfix_evaluator(queue):
   stack=Stack()
   input_queue=queue
   while not input_queue.is_empty():
       element = input_queue.dequeue()
       if element in ["^","*","/","+"]:
           num2=stack.pop()
           num1=stack.pop()
           result=evaluate_binary_operation(num1,num2,element)
           stack.push(result)
       else:
           stack.push(element)
   return stack.pop()
@measure_time
def shunting_yard_algorithm(expression):
    return postfix_evaluator(postfix_converter(expression))
def interpret_simple_arithmetic_expression(expression):
   input_expression=expression
   input_expression=input_expression.replace(" ","")
   input_expression=input_expression.replace("~","+-")
   input_expression=input_expression.replace("--","")
   processed_expression=ArithmeticExpression(input_expression)
   precedence_of_operator="^/*+"
   for Operator in precedence_of_operator:
       iterations=processed_expression.number_of_instances_of_operator(Operator)
       instance=1
       if Operator == "^":
           instance=-1
       for i in range(iterations):
           num1 = ""
           num2 = ""
           j = processed_expression.location_of_instance(instance,Operator) + 1
           while j < len(processed_expression.string):
               if processed_expression.string[j] in ["+","*","/","^"]:
                   break
               num2 = num2 + processed_expression.string[j]
               j = j + 1
           k = processed_expression.location_of_instance(instance,Operator) - 1
           while k + 1 > 0:
               if processed_expression.string[k] in ["+","*","/","^"]:
                   break
               num1 = num1 + processed_expression.string[k]
               k = k - 1
           num1 = num1[::-1]
           result = str(evaluate_binary_operation(float(num1),float(num2),Operator))
           evaluated_expression = processed_expression.string[:k + 1] + result + processed_expression.string[j:]
           processed_expression = ArithmeticExpression(evaluated_expression)
   return processed_expression.string
@measure_time
def interpret_arithmetic_expression(expression):
   input_expression=expression
   processed_expression=ArithmeticExpression(input_expression)
   iterations=processed_expression.number_of_instances_of_operator("(")
   start=0
   end=len(input_expression)
   for i in range(iterations):
       for j in range(len(processed_expression.string)):
           if processed_expression.string[j] == "(":
               start=j
           if processed_expression.string[j] == ")":
               end=j
               break
       expression_in_brackets=processed_expression.string[start+1:end]
       evaluated_expression=processed_expression.string[:start]+interpret_simple_arithmetic_expression(expression_in_brackets)+processed_expression.string[end+1:]
       processed_expression=ArithmeticExpression(evaluated_expression)
   result = interpret_simple_arithmetic_expression(processed_expression.string)
   result = float(result)
   return result
def main():
    while True:
        try:
            print("Enter the expression:")
            expression = input()
            if expression == "end":
                break
            print('Loading answers ...')
            time.sleep(2)
            print(f"Result as calculated by interpret_arithmetic_expression(): {interpret_arithmetic_expression(expression)}")
            print(f"Result as calculated by shunting_yard_algorithm(): {shunting_yard_algorithm(expression)}")
            print(f"Result as calculated by evaluate_arithmetic_expression(): {evaluate_arithmetic_expression(expression)}")
        except ZeroDivisionError:
            print("Cannot divide by zero")
        except SyntaxError:
            print("Cannot do complex number algebra")
        except ValueError:
            print("Invalid syntax for arithmetic expression")
        except IndexError:
            print("Invalid syntax for arithmetic expression")
if __name__ =="__main__":
    main()
