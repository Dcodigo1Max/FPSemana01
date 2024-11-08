

"""    
Nomes (string) 
valores vida e nivel de três criaturas (int)

exemplo:
Dragao nivel 10 vida 300

fenix n 15 v 200

unicornio n 12 v 250 


[['dragao', (300, 10)]['fenix', (200, 15)]['unico', (250, 12)]]

fenix 
uni
dragao



personagens = ['Dragao', 'Fenix', 'Unicornio', ]
niveis =['10', '15', '12']
vida = [ '300', '200', '250']
"""
"""
Dragao = [str[(input{{"Character 1: "}}, int{}    ]] 
Fenix = []
Unicornio = []



array = [
    [Dragao, Fenix, Unicornio] 

]


print(array)


for i in range():
     


    print(personagens)
"""

x=0

while x==0:
    creatura1 = [str(input("Creatura 1: ")), int(input("vida: ")), int(input("Nivel 1: "))]
    creatura2 = [str(input("Creatura 2: ")), int(input("Vida: ")), int(input("Nivel 2: "))]
    creatura3 = [str(input("Creatura 3: ")), int(input("Vida: ")), int(input("Nivel 3: "))]
    break

else: print("Not assigned")

array = [
    [creatura1, creatura2, creatura3]
]

print (array)

if creatura1[2] > creatura2[2] >  creatura3[2]:
    print(creatura1[0])
    print(creatura2[0])
    print(creatura3[0])

elif creatura1[2] >  creatura3[2] > creatura2[2]:
    print(creatura1[0])
    print(creatura3[0])
    print(creatura2[0])

elif creatura2[2] >  creatura3[2] > creatura1[2]:
    print(creatura2[0])
    print(creatura3[0])
    print(creatura1[0])

elif creatura2[2] > creatura1[2] > creatura3[2]:
    print(creatura2[0])
    print(creatura1[0])
    print(creatura3[0])

elif creatura3[2] > creatura1[2] > creatura2[2]:
    print(creatura3[0])
    print(creatura1[0])
    print(creatura2[0])

elif creatura3[2] > creatura2[2] >creatura1[2]:
    print(creatura3[0])
    print(creatura2[0])
    print(creatura1[0])

else:
    print("Some of these values are equal. Cannot compute.")

