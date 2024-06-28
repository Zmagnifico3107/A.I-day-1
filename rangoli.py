import string
alpha = string.ascii_lowercase
n = int(input("Enter the size N= "))

line = []
for i in range(n):
    s = '-'.join(alpha[n-1:i:-1] + alpha[i:n])
# Thêm hàng vào danh sách
    line.append(s.center(4*n-3, '-'))
print('\n'.join(line[::-1] + line[1:]))