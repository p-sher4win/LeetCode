# Can Place Flowers
def canPlaceFlowers(flowerbed: list[int], n):
    for i in range(len(flowerbed)):

        # find the index with the value zero
        if flowerbed[i]==0:

            # check if the left and right of the index is also zero
            left_empty = (i==0 or flowerbed[i-1]==0)
            right_empty = (i==len(flowerbed)-1 or flowerbed[i+1]==0)

            # if left and right are both empty
            if right_empty and left_empty:
                
                # replace the value of that index with 1 indicating the plot has plants
                flowerbed[i]=1

                # decrement the n value after each successful planting
                n-=1

                # return true if no plants remain
                if n == 0:
                    return True
    
    # return false if plants remain
    return n <= 0






flowerbed = [0]
n = 2
print(canPlaceFlowers(flowerbed, n))