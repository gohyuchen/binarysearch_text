def main():
    """
    3 options represented by 3 buttons
    1, 0, undo
    """
    
    #initializer
    count = 30
    array = []
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    print('LETS BEGIN! A->M = 1, N->Z = 0')

    while count > 0:
        while len(alphabets) > 1:
            a = input("Is alphabets from left or right half of the list?")
            if a == '1':
                k = len(alphabets) // 2
                alphabets = alphabets[:k]
                print('Current list of alphabets =',alphabets)
            else:
                k = len(alphabets) // 2
                alphabets = alphabets[k:]
                print('Current list of alphabets =',alphabets)

        array += alphabets
        alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        count -=1
        print('Current word =',array)
        print('Lets RESET! A->M = 1, N->Z = 0')


if __name__ == "__main__":
    main()
