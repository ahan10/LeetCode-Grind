# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A, B = len(word1), len(word2) # lengths of the strings
        a, b = 0, 0 # pointers for the strings
        s = [] # empty array

        word = 1 # starting merging with the first word

        while a < A and b < B: #both the words are not fully parsed
            if word == 1: # if word 1, append the current character, move the pointer and switch the word to 2
                s.append(word1[a])
                a += 1
                word = 2
            else: # # if word 2, append the current character, move the pointer and switch the word to 1
                s.append(word2[b])
                b += 1
                word = 1

        while a < A: # string B has been traversed through so we append the rest of string A
            s.append(word1[a])
            a += 1

        while b < B: # string A has been traversed through so we append the rest of string B
            s.append(word2[b])
            b += 1

        return ''.join(s) # return the string version of the array

# Time: O(A+B)
# Space: O(A+B)