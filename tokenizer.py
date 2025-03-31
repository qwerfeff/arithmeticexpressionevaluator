def tokenize_expression(string,delimiter):
   if not type(string) is str and not type(delimiter) is str:
       raise SyntaxError("Incorrect data type only str is valid for parameter ==> string,incorrect data type only str is valid for parameter ==> delimiter")
   if not type(string) is str:
       raise SyntaxError("Incorrect data type only str is valid for parameter ==> string")
   if not type(delimiter) is str:
       raise SyntaxError("Incorrect data type only str is valid for parameter ==> delimiter")
   tokens=[]
   token=""
   for i in range(len(string)):
       if string[i] in delimiter:
           tokens.append(token)
           tokens.append(string[i])
           token=""
       else:
           token=token+string[i]
       if i == len(string)-1:
           tokens.append(token)
   return tokens
