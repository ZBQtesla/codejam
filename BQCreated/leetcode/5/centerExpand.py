def solution(s):
    n = len(s)
    maxN = 0
    maxStr = ''
    for i in range(2*n-1):
        count = 0
        index = i // 2
        l = 0
        r = 0
        if (i % 2) == 0:
            count += 1
            l = index - 1
            r = index + 1
        else:
            l = index
            r = index +1

        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                count += 2
                l -= 1
                r += 1
            else:
                break

        if count > maxN: 
            maxN = count
            maxStr = s[l+1:r]

    return maxStr



print(solution("bb"))
