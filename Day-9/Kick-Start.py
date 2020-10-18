"""
Problem Name: Kick Start
Platform: Google Kickstart Round G 2020
Problem Link: https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414bfb
"""


def kick_start(arr):

    # kick and start will be used to match the character of the string with 'KICK' and 'START'.
    kick = 'KICK'
    start = 'START'

    # kick_count will store the number of characters matching at any point during the while-loop with 'KICK'.
    # start_count will store the number of characters matching at any point during the while-loop with 'START'.
    kick_count = 0
    start_count = 0

    # count is used to store number of 'KICK' sub-strings found.
    # total is used to store the number of occurences where 'KICK...START' is found in the string.
    # Initializing index to first index (0).
    count = 0
    total = 0
    i = 0

    # Using while-loop to iterate through the character of strings.
    while i != len(arr):

        # This condition finds the occurences of 'KICK' in the string.
        # If it is found then count is incremented.
        if arr[i] == kick[kick_count]:
            start_count = 0

            # The reason to not increment index here is that the last 'K' of 'KICK' can also be first 'K' of 'KICK'.
            # E.g.: 'KICKICK'.
            if kick_count == 3:
                count += 1
                kick_count = 0
            else:
                kick_count += 1
                i += 1

        # This condition finds the occurences of 'START' in the string.
        # If 'START' is found in the string then it can form 'KICK...START' substring with every preceeding 'KICK' occurences.
        # count stores the 'KICK' occurences. So add the current count to the total.
        elif arr[i] == start[start_count]:
            kick_count = 0
            if start_count == 4:
                total += count
                start_count = 0
                i += 1
            else:
                start_count += 1
                i += 1

        # If at any point, the character is not a part of either 'KICK' or 'START' sub-string then,
        else:

            # check if the current count of 'KICK' or 'START' is greater than 0. If yes then, initialize the counters to 0 and don't increment index.
            # The reason to not increment index is that the character can be 'K' or 'S', so it is necessary to consider that character again.
            if kick_count > 0 or start_count > 0:
                kick_count = 0
                start_count = 0

            # If the above condition is not the case then simply increment index.
            else:
                i += 1

    # Finally return the total.
    return total


# Code to take input and print the output by calling the above function.
if __name__ == "__main__":
    test = int(input())
    for i in range(test):
        arr = input()
        print("Case #{}: {}".format(i+1, kick_start(arr)))
