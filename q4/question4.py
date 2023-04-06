def factorial(x):
    if x == 0:
        return 0
    elif x ==1 :
        return 1
    else:
        return(x * factorial(x-1))

def main():
    for i in range(0, 15, 2):
        print('factorial', i, ':', factorial(i))

if __name__ == '__main__':
    main()

