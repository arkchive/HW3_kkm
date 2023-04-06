def reverse_words(str):
    list = str.split()
    list.reverse()
    return " ".join(list)

def main():
    str1 = 'Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;'
    str2 = 'Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,'
    print('str1 :', str1)
    print('reverse_str1 :', reverse_words(str1))
    print('str2 :', str2)
    print('reverse_str2 :', reverse_words(str2))

if __name__ == '__main__':
    main()
