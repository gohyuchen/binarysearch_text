import sys

sys.path.append('/usr/local/lib/python3.9/site-packages')

from pytimedinput import timedInput


def main():
    """
    2 options: response, no response

    wait for timeout ~3s to 'no response'
    press arrowkey or enterkey to 'respond'
    """
    count = 3
    array = []
    alphabets = [' ','A','B','C','D','E','F','G','H','I','J','K','L',
                'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    print('BEGIN! A->L = 1, M->Z = 0')

    while count > 0:
        while len(alphabets) > 1:
            a, timedOut = timedInput("Is alphabets from left or right?",
                                    timeout=3)

            if(timedOut):
                k = len(alphabets) // 2
                alphabets = alphabets[:k]
                print('Current list =',alphabets)
            else:
                k = len(alphabets) // 2
                alphabets = alphabets[k:]
                print('Current list =',alphabets)

        array += alphabets
        alphabets = [' ','A','B','C','D','E','F','G','H','I','J','K','L',
                    'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        count -=1
        print('Current word =', ''.join(array))
        print('RESET! A->L = 1, M->Z = 0')


if __name__ == "__main__":
    main()
