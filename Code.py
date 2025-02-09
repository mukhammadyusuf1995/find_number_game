import random

print("wellcome find a number game".upper())
# Foydalanuvchidan tilni tanlashni so'rash
til = input("Choose your language:\nEnglish(en)\nO'zbek(uz)\nKorean(kr)\n")

# Pc o'ylagan sonlarni user topish kodi
def sontop_en(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"I think one number from 1 to {x}. Can you guess the number", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print(f"Opps,The number is bigger than {taxmin}, try to find again", end="")
        elif taxmin > tasodifiy_son:
            print(f"Opps,The number is smaller than {taxmin}, try to find again", end="")
        else:
            break
            
    print(f"Congratulation! You found the number in {taxminlar} tries.")
    return taxminlar

# Pc user oylagan sonni topish kodi
def sontop_pc_en(x=10):
    input (f"Think one of any number from 1 to {x} and press ENTER.\nI try to find.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else: 
            taxmin = quyi
        javob = input(f"You thought {taxmin}\nyes(y)\n"
                          f"The number is bigger than {taxmin}, type (+)\nThe number is smaller than {taxmin}, type (-)\n")
        if javob == "-":
                yuqori = taxmin - 1
        elif javob == "+":
                quyi = taxmin + 1
        else:
            break
        
    print(f"I found the number in {taxminlar} tries")
    return taxminlar

#natijalar
def play_en(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop_en(x)
        taxminlar_pc = sontop_pc_en(x)
        
        if taxminlar_user>taxminlar_pc:
            print("I won!")
        elif taxminlar_user<taxminlar_pc:
            print(f"You found the number in {taxminlar_user} tries and You won!")
        else:
            print("Both of us found the number in {taxminlar_pc} tries and  It is Draw!")
            
        yana = input("Do you want to play again?\nYes(y)\nNo(n):")
        if yana.lower() == 'y':
            yana = 1
        elif yana.lower() == 'n':
            yana = 0
        else:
            print("Invalid choice. Please choose y or n.")
            
#ozbek tilidagi kodlar
def sontop_uz(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:", end="")
        elif taxmin>tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:", end="")
        else:
            break
        
    print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar

def sontop_pc_uz(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar

def play_uz(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop_uz(x)
        taxminlar_pc = sontop_pc_uz(x)
        if taxminlar_user>taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print(f"Ikkalamiz ham {taxminlar_pc} ta taxmin bilan topdik va Durrang!")
            
        yana = input("Yana o'ynashni xoxlaysizmi?\nHa(h)\nYo'q(y):")
        if yana.lower() == 'h':
            yana = 1
        elif yana.lower() == 'y':
            yana = 0
        else:
            print("Iltimos yuqorida keltirilgan 'y' yoki 'h' birini tanlang")
            
# Karis tilidagi kodlar
def sontop_kr(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"저는 1부터 {x}까지 숫자 중에 하나 생각합니다. 제가 생각했던 숫자를 맞춰보세요. ", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print(f"제가 생각했던 숫자가 {taxmin}보다 큽니다. 다시 맞춰보세요.", end="")
        elif taxmin > tasodifiy_son:
            print(f"제가 생각했던 숫자가 {taxmin}보다 작습니다. 다시 맞춰보세요.", end="")
        else:
            break
            
    print(f"정답입니다! 제가 생각햇던 숫자를 {taxminlar}번만에 맞췄어요.")
    return taxminlar

# Pc user oylagan sonni topish kodi
def sontop_pc_kr(x=10):
    input (f"1부터 {x}까지 숫자 중에 하나 생각하시고 ENTER를 눌러주세요.\n저는 맞춰보겠습니다.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else: 
            taxmin = quyi
        javob = input(f"{taxmin}를 생각하셨조?\n정답(네)\n"
                          f"정답은 {taxmin}보다 크면 (+)를 눌러주셍요.\n{taxmin}보다 작으면 (-)를 눌러주세요.\n")
        if javob == "-":
                yuqori = taxmin - 1
        elif javob == "+":
                quyi = taxmin + 1
        else:
            break
        
    print(f"제가 {taxminlar}번만에 맞췄습니다.")
    return taxminlar

#natijalar
def play_kr(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop_kr(x)
        taxminlar_pc = sontop_pc_kr(x)
        
        if taxminlar_user>taxminlar_pc:
            print(f"제가 {taxminlar_pc}번만에 맞춰서 제가 이겼습니다!.")
        elif taxminlar_user<taxminlar_pc:
            print(f"제가 생각햇던 숫자를 {taxminlar_user}번만에 맞춰서 이겻습니다!")
        else:
            print(f"우리 둘다 {taxminlar_pc}번만에 맞춰서 이긴 사람 없습니다!")
            
        yana = input("게임 다시 하시겠어요?\n네(yes)\n아니요(no):")
        if yana.lower() == 'yes':
            yana = 1
        elif yana.lower() == 'no':
            yana = 0
        else:
            print("선택 가능한 'yes' 또한 'no' 중에 하나를 선택해주세요.")


# Foydalanuvchining tanloviga qarab mos funksiyani chaqirish
if til.lower() == "en":
    play_en()
elif til.lower() == "uz":
    play_uz()
elif til.lower() == "kr":
    play_kr()
else:
    print("Invalid choice. Please choose a valid language.")
