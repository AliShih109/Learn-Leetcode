'''
844. Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(N) time and O(1) space?
'''


#Solution1
class Solution:
    
    def backspace(self, C):
        i=0
        
        while i < len(C):
            if C[i] == '#':
                C = C[:(i-1)]*min(i, 1) + C[(i+1):]
                i = max(0, i-1)
            else:
                i = i+1
        return C

    
    def backspaceCompare(self, S, T):
        return self.backspace(S) == self.backspace(T)


#Solution2
class Solution:
    def backspace(self, S):
        s = []
        for i in S:
            if i=='#':
                try:
                    s.pop()
                except:
                    pass
            else:
                s.append(i)
        return s
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.backspace(S) == self.backspace(T)
