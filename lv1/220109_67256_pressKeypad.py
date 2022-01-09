
# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = "right"

# numbers= [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = "left"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"

pad = {1: [1, 1], 2: [1, 2], 3: [1, 3], 4: [2, 1], 5: [2, 2], 6: [2, 3], 7: [3, 1], 8: [3, 2], 9: [3, 3], 0: [4, 2]}

current_left = [4, 1]
current_right = [4, 3]

result = ''
for i in numbers:
    if pad[i][1] == 1:
        result += 'L'
        current_left = pad[i]
    elif pad[i][1] == 3:
        result += 'R'
        current_right = pad[i]
    else:
        d_left = abs(current_left[0]-pad[i][0]) + abs(current_left[1]-pad[i][1])
        d_right = abs(current_right[0]-pad[i][0]) + abs(current_right[1]-pad[i][1])
        if d_left > d_right:
            result += 'R'
            current_right = pad[i]
        elif d_left < d_right:
            result += 'L'
            current_left = pad[i]
        else:
            if hand == 'right':
                result += 'R'
                current_right = pad[i]
            else:
                result += 'L'
                current_left = pad[i]

print(result)
