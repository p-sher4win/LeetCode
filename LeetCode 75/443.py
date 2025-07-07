# String Compression
class Solution:
    def compress(self, chars: list[str]) -> int:
        # initialize c(index) and s(size) = zero
        c=s=0

        while c < len(chars):
            # assign curr to the value at c index
            curr = chars[c]
            # declare variable occ to zero
            occ = 0

            # loop chars and check if value at index c and curr matches
            while c < len(chars) and chars[c]==curr:
                # increment occ and index c by 1
                occ+=1
                c+=1
            
            # assign curr to the c index in chars arr
            chars[s]=curr
            # increment s by 1
            s+=1
            
            # if occ is greater than 1
            if occ > 1:
                # convert integer occ to string
                occStr = str(occ)
                
                # loop through size of string occ
                for j in range(len(occStr)):
                    # assign value of string occ at index j to index s in chars arr
                    chars[s]=occStr[j]
                    # again increment s by 1
                    s+=1
        
        # return the s(size) of the new compress string
        return s



# testcases
chars=["a","a","b","b","c","c","c"]
# chars = ["a"]
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# chars = ["a","a","a","b","b","a","a"]
s = Solution()
print(s.compress(chars))