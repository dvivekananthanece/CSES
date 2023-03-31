received_input = input()
a = t = g = c = 0
result = []
for i in range(0, len(received_input)):
    if received_input[i] == 'A':
        a = a + 1
        result.append(a)
        t = g = c = 0
    if received_input[i] == 'T':
        t = t + 1
        result.append(t)
        a = g = c = 0
    if received_input[i] == 'G':
        g = g + 1
        result.append(g)
        t = a = c = 0
    if received_input[i] == 'C':
        c = c + 1
        result.append(c)
        t = g = a = 0
print(max(result))
