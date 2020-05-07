def no_dups(s):
    # Implement me.

    no_dups=[]
    for w in s.split():
        if w not in no_dups:
            no_dups.append(w)

    return " ".join(no_dups)




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))