class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        current_op = []
        operators = {"+", "-", "*", "/"}
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                current_op.append(int(tokens[i]))  
            else:
                b = current_op.pop()
                a = current_op.pop()
                op = tokens[i]

                if op == "+":
                    result = (a+b)
                elif op == "-":
                    result = (a-b)
                elif op == "*":
                    result = (a*b)
                elif op == "/":
                    result = int(a/b)
                current_op.append(result)
        return current_op[0]