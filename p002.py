LIMIT = 4000000

def fibonacci(limit):
    sequence = [0, 1] # first 2 are assumed
    while sequence[-1] < limit:
        _next = sequence[-1] + sequence[-2]
        sequence.append(_next)
        
    return sequence

f_seq = fibonacci(LIMIT)
sum_even_sequence = 0
for n in f_seq:
    if n % 2 == 0:
        sum_even_sequence += n

print(sum_even_sequence)