def is_valid_string(s):
    char_freq = {}
    
    # Count the frequency of each character
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    # Count the frequency of frequencies
    freq_freq = {}
    for freq in char_freq.values():
        if freq in freq_freq:
            freq_freq[freq] += 1
        else:
            freq_freq[freq] = 1
    
    # If all characters have the same frequency
    if len(freq_freq) == 1:
        return "YES"
    
    # If there are exactly two frequencies
    if len(freq_freq) == 2:
        # If one frequency has only one occurrence and can be removed
        if 1 in freq_freq.values() and (freq_freq[1] == 1 or abs(list(freq_freq.keys())[0] - list(freq_freq.keys())[1]) == 1):
            return "YES"
    
    # Otherwise, it is not a valid string
    return "NO"


# Example test case 1
s = "abc"
print(is_valid_string(s))  # Output: YES

# Example test case 2
s1 = "abcc"
print(is_valid_string(s1))  # Output: YES
# Explanation: The character 'c' has a frequency of 2, and all other characters have a frequency of 1.
# Removing one occurrence of 'c' results in all characters having the same frequency (1).

# Additional test case 1
s2 = "aabbc"
print(is_valid_string(s2))  # Output: YES
# Explanation: The character 'c' has a frequency of 1, and all other characters have a frequency of 2.
# Removing one occurrence of 'c' results in all characters having the same frequency (2).

# Additional test case 2
s3 = "aaabbbbcc"
print(is_valid_string(s3))  # Output: NO
# Explanation: The characters 'a', 'b', and 'c' have frequencies of 3, 4, and 2 respectively.
# Removing one occurrence of 'c' does not results in all characters having the same frequency.
