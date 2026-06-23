class Solution:
    def calPoints(self, ops: List[str]) -> int:
        

        # list of string operations[str]
        # int x: record new score of x
        # +: record that sum of 2 previous scores, it's guaranteed at least 2 previous records
        # D: new record tha doucble the prevous score, at least one previous score on the record.
        # C: remove the previous score, at least one previous score on the record.
        # Return: value in integer
        

        stack = []
        for op in ops:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)