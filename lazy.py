import sys

sys.path.append('/usr/local/lib/python3.9/site-packages')

from pytimedinput import timedInput


def main():
    """
    2 options: response, no response

    wait for timeout ~3s to 'no response'
    press arrowkey or enterkey to 'response'

    Spacebar: no response (timeout) all the way
    Backpace: response all the way
    """
    count = 30
    array = []
    alphabets = [' ',
                'A','B','C','D','E','F','G','H','I','J','K','L','M',
                'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                'BACK'
                ]
    print('BEGIN! A->M = 1, N->Z = 0')

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
        
        if alphabets == ['BACK']:
            array.pop()
        else: array += alphabets

        alphabets = [' ',
                    'A','B','C','D','E','F','G','H','I','J','K','L','M',
                    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                    'BACK'
                    ]
        count -=1
        print('Current word =', ''.join(array))
        print('RESET! A->M = 1, N->Z = 0')


if __name__ == "__main__":
    main()
