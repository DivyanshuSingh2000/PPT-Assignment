def find_highest_frequency_word_length(string):
    word_freq = {}
    
    # Split the string into words
    words = string.split()
    
    # Count the frequency of each word
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Find the highest frequency
    max_freq = max(word_freq.values())
    
    # Find the length of the highest-frequency word
    highest_freq_word_length = len(max(word_freq, key=word_freq.get))
    
    return highest_freq_word_length
    
# Example test case
string = "write write write all the number from from from 1 to 100"
print(find_highest_frequency_word_length(string))  # Output: 5

# Additional test case 1
string1 = "apple apple orange orange orange banana banana banana banana cherry"
print(find_highest_frequency_word_length(string1))  # Output: 6
# Explanation: The word "banana" appears the most (4 times) and its length is 6.

# Additional test case 2
string2 = "hello hello world world world world world world world"
print(find_highest_frequency_word_length(string2))  # Output: 5
# Explanation: The word "world" appears the most (7 times) and its length is 5.

