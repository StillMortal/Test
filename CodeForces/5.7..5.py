n, m, module = [int(i) for i in input().split()]

d = [[0] * (m + 1) for _ in range(1 << n)]
d[0][0] = 1
# print(*d, sep='\n')

bank_of_masks = [False] * (1 << n)
for num in range(1 << n):
    nexus = num
    binary_representation = []
    while num != 0:
        binary_representation.append(num % 2)
        num //= 2
    binary_representation.extend([0] * (n - len(binary_representation)))
    flag = 0
    zeros = 0
    for zero_or_one in binary_representation:
        if zero_or_one == 0:
            zeros += 1
        else:
            if zeros % 2 == 0:
                zeros = 0
            else:
                flag = 1
                break
    # print(flag, binary_representation)
    if flag == 0 and zeros % 2 == 0:
        bank_of_masks[nexus] = True
    else:
        bank_of_masks[nexus] = False
print(bank_of_masks)


def can(left_mask, right_mask):
    return True if left_mask & right_mask == 0 and bank_of_masks[left_mask | right_mask] else False


for i in range(m):
    for mask in range(1 << n):
        for new_mask in range(1 << n):
            if can(mask, new_mask):
                d[new_mask][i + 1] = (d[new_mask][i + 1] + d[mask][i]) % module

print(*d, sep='\n')
print(d[0][m])

