# Program to Find Longest Common Subsequence (LCS)
# Using Dynamic Programming (Tabulation)

def LCS_DP(firstString, secondString):

    length1 = len(firstString)
    length2 = len(secondString)

    # Creating DP table
    dp = []
    for i in range(length1 + 1):
        row = []
        for j in range(length2 + 1):
            row.append(0)
        dp.append(row)

    # Filling the DP table
    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):

            if firstString[i - 1] == secondString[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    # Finding the LCS
    i = length1
    j = length2
    answer = []

    while i > 0 and j > 0:

        if firstString[i - 1] == secondString[j - 1]:
            answer.append(firstString[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    answer.reverse()
    lcs = "".join(answer)

    return lcs, dp[length1][length2]


# Main Program
str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")

result, lcsLength = LCS_DP(str1, str2)

print("\nLongest Common Subsequence :", result)
print("Length of LCS :", lcsLength)
