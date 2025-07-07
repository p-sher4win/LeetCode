# Kids with the Greatest Number of Candies
def kidsWithCandies(candies, extraCandies):
    # comparison = list()
    # result = list()

    # for x in range(len(candies)):
    #     total = candies[x]+extraCandies
    #     for y in range(len(candies)):
    #         if total >= candies[y]:
    #             comparison.append(True)
    #         else:
    #             comparison.append(False)

    #     if False in comparison:
    #         result.append(False)
    #     else:
    #         result.append(True)
    #     comparison=list()


    # Finds the max candy a kid has in the list of candies
    max_candy = max(candies)
    
    # Empty list to append bool values
    result = []

    for candy in candies:
        # adds the extra candies to each kid's candy
        candy+=extraCandies

        # appends the bool value of if its highest among all the kids candy
        result.append(candy >= max_candy)

    # returns the final bool list
    return result


candies = [2,3,5,1,3]
extraCandies = 3
output = print(kidsWithCandies(candies, extraCandies))