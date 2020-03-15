# Exercise One Part One (Create String)

# - Create a new string '1 Welcome Ring to Tyler' from the given string

msg='welcome to Python 101: Strings'

msg1 = msg[18] + ' ' + msg[:8] + msg[25:29] + ' ' + msg[8:11] + msg[8] + msg[12] + msg[2] + msg[1] + msg[25]

print(msg1.title())

one = msg[18]
welcome = msg[:7]
ring = msg[25:29]
to = msg[8:10]
tyler = msg[8] + msg[12] + msg[2] + msg[1] + msg[25]

msg2 = one + ' ' + welcome + ' ' + ring + ' ' + to  + ' ' + tyler

print(msg2.title())

# Excercise One Part Two (Reverse String)

# - Reverse the new string

msg2_reverse = msg2[::-1]

print(msg2_reverse.title())