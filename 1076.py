data_character = input()

# a ~ z = 97 ~ 122
for i in range(97, ord(data_character)+1):
    print(chr(i))