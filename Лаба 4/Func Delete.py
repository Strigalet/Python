print("""
        ===================================================================
                              ЛАБОРАТНОРНА РОБОТА №4
                     ПРОГРАМУВАННЯ З ВИКОРИСТАННЯМ ФУНКЦІЙ
                                (РОБОТА З РЯДКАМИ)
                     АВТОР: КАСІЧ БОГДАН, КМ-83 (6 ВАРІАНТ)    
        ===================================================================
Добрий день! Дана програма дозволить вам ввести своє речення , а потім ви зможете
видалити звідти певний підрядок, який забажаєте. Програма зроблена за допомогою 
функції Delete(s,n,l), де s - ваше речення , n - стартова позиція , l - довжина підрядка
                                                                                      """)

import re
def Delete(s,n,l):
    if n < 0 and abs(n) < l:
        b=len(s)+n
        return (s[:b]+s[l+b:])
    else:
        return (s[:n] + s[l+n:])
    
        
    
def valid_position():
    position = input("Type integer starting position of your substring: ")
    while not re.match(pattern_int,position):
        position = input("Type integer only please:  ")
    position=int(position)
    while position >= len(sentence) or abs(position) > len(sentence):
        position = input("value of position must not exceed the length of your sentence:  ")
        while not re.match(pattern_int,position):
            position = input("Type integer only please: ")
        position=int(position)
        
    return position

def valid_length():
    length = input("Type the positive integer length of your substring: ")
    while not re.match(pattern_int,length):
        length=input("Print INTEGER POSITIVE number please: ")
    length=int(length)
    while length <= 0:
        length=input("Print integer POSITIVE number please: ")
        while not re.match(pattern_int,length):
            length=input("Print INTEGER POSITIVE number please: ")
        length=int(length)
    return length
    
            
            
pattern_int = r"^[-\d]\d*$"             
        
        
        
    
        
        
      
sentence=input("Print your sentence: ")
position= valid_position()
length= valid_length()
print(Delete(sentence,position,length))

answer=input("print 'stop' if u want to stop the prog:  ")
while answer!="stop":
    change_everything=input("print '1' if u want to change everything: ")
    if change_everything=='1':
        sentence=input("Print your sentence: ")
        position= valid_position()
        length= valid_length()
        print(Delete(sentence,position,length))
        answer=input("print 'stop' if u want to stop the prog:  ")
    else:
        change_length=input("print '2' if u want to change length: ")
        change_position=input("print '3' if u want to change position: ")
        change_sentence=input("print '4' if u want to change sentence: ")
        if change_length=='2' and change_position=='position' and change_sentence=='sentence':
            print("You could achieve the same just by typing '1' earlier...")
            sentence=input("Print your sentence: ")
            position= valid_position()
            length= valid_length()
            print(Delete(sentence,position,length))
            answer=input("print 'stop' if u want to stop the prog:  ")
        elif change_length=='2' and change_position=='3' and change_sentence!='4':
            position= valid_position()
            length= valid_length()
            print(Delete(sentence,position,length))
            answer=input("print 'stop' if u want to stop the prog:  ")    
        elif change_length!='2' and change_position=='3' and change_sentence=='4':
            sentence=input("Print your sentence: ")
            position= valid_position()
            print(Delete(sentence,position,length))
            answer=input("print 'stop' if u want to stop the prog:  ")
        elif change_length!='2' and change_position=='3' and change_sentence!='4':
            position= valid_position()
            print(Delete(sentence,position,length))
            answer=input("print 'stop' if u want to stop the prog:  ")   
        elif change_length=='2' and change_position!='3' and change_sentence=='4':
            sentence=input("Print your sentence: ")
            while len(sentence) <= position or len(sentence) < abs(position):
                sentence=input("the length of your sentence must not be less than value of position: ")
            length= valid_length()
            print(Delete(sentence,position,length))
            answer=input("print 'stop' if u want to stop the prog:  ")
        elif change_length=='2' and change_position!='3' and change_sentence!='4':
            position= valid_length()
            print(Delete(sentence,position,length))
            answer=input("print 'stop' if u want to stop the prog:  ")
        elif change_length!='2' and change_position!='3' and change_sentence=='4':
            sentence=input("Print your sentence: ")
            while len(sentence) <= position or len(sentence) < abs(position):
                sentence=input("the length of your sentence must not be less than value of position: ")
            print(Delete(sentence,position,length))
            answer=input("print 'stop' if u want to stop the prog:  ")
        else:
            answer=input("You have not changed anything, which means that the result will be the same. \nBut if you want to stop the prog print 'stop': ")
        
    
        
        
        
            
