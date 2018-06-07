def writeOutput(outfile,output):
    file = open(outfile,'w')

    file.write('Case #1:\n')
    for i in range(len(output)):
        for j in range(10):
            output[i][j] = str(output[i][j])

    for element in output:
        file.write(' '.join(element) + '\n')

    file.close()

def isPrime(integer):
    i = 2
    while i * i <= integer:
        if integer % i == 0:
            return False,i
        i += 1
    return True,-1

def compute(length,numOfCoin):
    '''
    :type length:int    meaning length:length of coinjam
    :type numOfCoin:int
    '''
    coin = '1' + (length - 2) * '0' + '1'
    result = []
    while coin <= length * '1' and len(result) < numOfCoin:
        possible = [int(coin)]
        print(coin)
        for i in range(2,11):
            prime = isPrime(int(coin,base = i))
            if not prime[0]:
                possible.append(prime[1])
            else:
                break
        if len(possible) == 10:
            result.append(possible)
            print('The number of coins are:',len(result))
        coin = bin(int(coin,base = 2) + int('10',base = 2))[2:]
    return result

def main():
    length = 32
    numOfCoin = 500
    output = compute(length,numOfCoin)
    writeOutput('solve_coinjam_large.txt',output)

main()
