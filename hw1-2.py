#    2. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# ⋀ - and ⋁ - or ¬ - not




print ("X Y Z   (¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z)")
for x in range(2):
        for y in range(2):
            for z in range(2):
                print(x, y, z, end="        ")
                print(not (x or y or z) == (not x and not y and not z))
                
