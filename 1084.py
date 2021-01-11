data_color_red, data_color_green, data_color_blue = map(int, input().split())
data_count = 0

for r in range(0, data_color_red):
    for g in range(0, data_color_green):
        for b in range(0, data_color_blue):
            print('{0} {1} {2}'.format(r, g, b))
            data_count += 1

print(data_count)
