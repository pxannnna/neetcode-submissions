class Solution:

    def calculate(self, s: str) -> int:
        stack = []
        curr_num = 0
        prev_op = "+"

        for i, char in enumerate(s):
            # create multi-digit numbers
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)

            # process operator or end of string
            if (not char.isdigit() and char != " ") or i == len(s) - 1:
                if prev_op == "+":
                    stack.append(curr_num)
                elif prev_op == "-":
                    stack.append(-curr_num)
                elif prev_op == "*":
                    stack.append(stack.pop() * curr_num)
                elif prev_op == "/":
                    stack.append(int(stack.pop() / curr_num))

                # Reset for next number and update operator
                prev_op = char
                curr_num = 0

        return sum(stack)
