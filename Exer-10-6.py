def is_anagram(s1, s2):
    for l in s1:
        if l in s2:
            continue
        return False

    return True


if __name__ == '__main__':
    word1 = "listen"
    word2 = "silent"
    print(is_anagram(word1, word2))
