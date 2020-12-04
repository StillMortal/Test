def can(a, b):
    return True if a & b == 0 and bank_of_masks[bin(a | b)[2:]] else False


n, m = map(int, input().split())

bank_of_masks = {}
for mask in range(1 << n):
    bmask = bin(mask)[2:]
    x = 0
    f = 1
    while x < len(bmask):
        if bmask[x] == '0':
            if bmask[x: x + 2] == '00':
                x += 2
            else:
                f = 0
                break
        else:
            x += 1
    if f == 1:
        bank_of_masks[bmask] = True
    else:
        bank_of_masks[bmask] = False
print(bank_of_masks)


d = [[0 for i in range(1 << n)] for j in range(m + 1)]
d[0][0] = 1
for i in range(m):
    for mask in range(1 << n):
        for new_mask in range(1 << n):
            if can(mask, new_mask):
                d[i + 1][new_mask] += d[i][mask]

print(*d, sep='\n')
print(d[m][0])