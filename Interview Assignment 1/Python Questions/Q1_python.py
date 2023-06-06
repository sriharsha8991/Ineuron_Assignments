# Question 1: -
# Write a program that takes a string as input, and counts the frequency of each word in the string, there might
# be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
# highest-frequency word.

# Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
# an explanation for the same.
# Example input - string = “write write write all the number from from from 1 to 100”
# Example output - 5
# Explanation - From the given string we can note that the most frequent words are “write” and “from” and
# the maximum value of both the values is “write” and its corresponding length is 5

def repeated_max_string(text):
    #We can upgrade this code by converting everything into lowercase if case is not an issue

    ls = text.split(" ")         # Converting the Text into a list format for easy access
    dc = dict()                 # Dictionary for Frequency of words

    for i in ls:
        dc[i] = ls.count(i)
    max_rep = max(dc.values())      # Get the word/words that has highest frequency

    ans=[]                      # load the words in the list ans

    for key,value in dc.items():
        if value == max_rep:
            ans.append(key)

    op = ''                     # checking for the max length of words in ans
    for i in ans:
        if len(i)>len(op):
            op = i
    return op
    

#Sample Test Cases
tc1 = "sample sample sample test test test case case case 1"
#Explaination for tc1 : returns "sample" it has maximum number of characters and one of most repeated value in the text 
tc2 = "Example Test Case 2"
#Explaination for tc2 : returns "Example" as it has maximum number of characters even all are having same fequency of repetations
tc3 = "Example test test case case case 2"
#Explaination for tc3 : return "case" as it is most repeated in the given text

print(repeated_max_string(tc1))
print(repeated_max_string(tc2))
print(repeated_max_string(tc3))