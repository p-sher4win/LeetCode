# Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        # convert the string into list by spliting each word
        s_list=s.split()
        
        # reverse the list using negative index
        reverse = s_list[::-1]

        # return the reverse list by using the join function
        return ' '.join(reverse)


# s="the sky is blue"
# s="  hello world  "
s = "a good   example"
string = Solution()
print(string.reverseWords(s))