LIMIT = 1000000

def gen_CollatzSeq(num):
    while num > 1:
        if num % 2 == 1:
            num = (3 * num) + 1
        elif num % 2 == 0:
            num = num/2
        yield int(num)

max_length_num = 0
max_length = 0
for num in range(LIMIT):
    print("processing number %s" % str(num))
    length = 0
    for CollatzSeqNum in gen_CollatzSeq(num):
        length += 1
    if length > max_length:
        max_length = length
        max_length_num = num

print(
    f"""Max sequence length: {max_length}
starting value: {max_length_num}"""
)