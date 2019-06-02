#Given a base-10 integer,n , convert it to binary (base-)2.
#Then find and print the base- integer denoting the maximum number of consecutive ‘s in ‘s binary representation.

n = int(input().strip())

binary = list(bin(n)[2:])


count = 0
max_count = 0
for i in binary:
    if (i == '1'):
        count += 1
    else:
    #reset count when next 0 is found
        if count > max_count:
            max_count = count
        count = 0
if count > max_count:
    max_count = count
print (max_count)
