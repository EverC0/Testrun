

# stack_m = []
# n = 3
# open_p = 0
# closed_p = 0

# Note: closed < open
# if n = 3 then we must have 3 open, closed
# open parenthesis "(" should always come before ")"

class solution:
    def generateP(self, n):
        # only add open paranthesis if open < n
        # only add a closing peranthesis if closed < open
        # valid IIF open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
            
        return res

# With the use of backtracking and recurison this
# Systematic Approach
# Explore Every Option: At each step, the algorithm tries 
# both adding an open ( and a close ) if possible.
# Backtrack and Retry: After completing or exhausting a path,
#  it goes back and tries a different path.
# No Combinations Missed: This ensures every possible valid combination is generated.
# By following this structured method, the algorithm ensures it doesn't 
# miss any possible combinations and covers all valid sequences of n pairs of parentheses.





# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string 
# inside the square brackets is being repeated exactly k times. Note that
#  k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; there are no extra white spaces,
#  square brackets are well-formed, etc. Furthermore, you may assume that the original 
# data does not contain any digits and that digits are only for those repeat numbers, k. 
# For example, there will not be input like 3a or 2[4].


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[": # continue to pop until find open bracket
                    substr = stack.pop() + substr
                stack.pop() #pops off the "[" open bracket 

                k = ""
                while stack and stack[-1].isdigit(): #this finds the integer were muliplying the substring by
                    k = stack.pop() + k #perserves order

                stack.append(int(k) * substr) # append the substring k times to the stack

        return "".join(stack)
