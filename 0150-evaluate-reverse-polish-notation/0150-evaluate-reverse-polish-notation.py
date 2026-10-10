class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack=[]
        for i in tokens:
           
           if i=="+":
                stack.append(stack.pop()+stack.pop())
           elif i=="*":
                stack.append(stack.pop()*stack.pop())
           elif i=="-":
                s,f=stack.pop(),stack.pop()
                stack.append(f-s)

           elif i=="/":
                s,f=stack.pop(),stack.pop()
                stack.append(int(f/s))
           else:
                stack.append(int(i))

        return stack[0]
            

            
