# 274. H-Index
# https://leetcode.com/problems/h-index/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations) # total number of books with citation
        paper_counts = [0] * (n + 1) # we want to do essentially a count sort

        for c in citations: # here we make sure that we the value (x) of i means: that there are x papers with i citations
            paper_counts[min(n, c)] += 1 # we want the last index meaning that there are >= n citations

        papers = paper_counts[n] # we start backwards with papers at the last index being the number of papers having more than ore equal to n citations
        h = n # initially we assume the h index to be equal to n

        while papers < h: # we will get a h index when we reach the condition papers >= h; and will break out of the loop
            h -= 1 # we haven't met the condition so we decrement the h
            papers += paper_counts[h] # and increase the number of papers that have at least h citations

        return h # when we break the loop we have found the h index

# Time: O(n)
# Space: O(n)