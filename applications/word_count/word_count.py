import re
rxp = r'[":;,.\-+=/\\|\[\]{}()*\^&]'
def word_count(s):
    # Implement me.
    s = s.casefold()
    s = re.sub(rxp,"", s)
    word_list = s.split()
    word_dict = {}
    while len(word_list):
        word = word_list.pop()
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))