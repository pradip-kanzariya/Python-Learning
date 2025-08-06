# 5. Testing and Debugging

# Practice Task : 1 | Write tests for a library that performs string manipulation.
def reverse_string(s):
    if not isinstance(s, str):
        raise TypeError()
    return s[::-1]

def capitalize_words(s):
    if not isinstance(s, str):
        raise TypeError()
    return ' '.join(word.capitalize() for word in s.split())

def remove_punctuation(s):
    import string
    return ''.join(c for c in s if c not in string.punctuation)

def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]