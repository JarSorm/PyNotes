#1
List = [1, 2, 3 ,4 ,5]
print(List[0], List[2], List[0:3], sep="\n")
#2
Rost = ["Ростов", "+", "на", "-", "Дону"]
Rost[Rost.index("+")] = "-"
print(*Rost, sep= "")
#3
Let_Dig = ["a", "s", "1", "a", "32", "23"]
Let = []
Dig = []
for i in range(0, len(Let_Dig)):
    if Let_Dig[i].isdigit():
        Dig.append(Let_Dig[i])
    else:
        Let.append(Let_Dig[i])
#аналог с list comprehensions
letters = [l for l in Let_Dig if l.isalpha()]
digits = [d for d in Let_Dig if d.isdigit()]
#4
Let_Dig.pop()
Let_Dig.reverse()
#5
Let_Dig2 = ["a", "s", "1", "a", "32", "23"]
print(set(Let_Dig2))
#преобразование в множество: все элементы становятся уникальными, порядок - случайным