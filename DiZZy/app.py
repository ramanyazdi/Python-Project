string = "T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24"

# Split a string into a list where each word is a list item
parts = string.split(" ")
# print(parts) 

answer = []
for i in parts:
    answer.append('*')
# print(answer)
for p in parts:
    c = p[0]
    i = int(p[1:])
    answer[i] = c
print(''.join(answer))


