class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x=dict(('()', '[]', '{}'))
        stack=[]
        for i in s:
            if i in '({[':
                stack.append(i)
            elif not stack or x[stack.pop()]!=i:
                return False
        return not stack
        pass







    



  

