#nhập chuỗi và điều kiện của chuỗi
s  = str(input("Enter the string to start the game: ").strip().upper())
while len(s) > 10^6:
       s= str(input("reenter the string: "))      
vowels = 'AEIOU'
player1 = 0
player2 = 0
#tính điểm cho người chơi
for i in range(len(s)):
    if s[i] in vowels:
        player1 += (len(s) - i)
    else:
        player2 += (len(s) - i)
#so sánh điểm và đưa ra người thắng cuộc   
if player1 > player2:
    print("Minh", player1)
elif player2 > player1:
    print("An", player2)
else:
    print("Draw")
