print("WELCOME TO CALCULATOR")
print("------------------------")
while True:
   try:
       exp= input("Enter the expression (or 'quit' to exit): ")
       if exp.lower() == 'quit':
           break
       
       else:
           result = eval(exp)
           print(f"The result is: {result:.2f}")

   except Exception as e:
       print(f"Error: {e}")
    
           
           