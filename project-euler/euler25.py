from utils import fib

curr_len = 0
prev_len = 0
i = 3000 #heuristic start

num_digits = 1000

while not(curr_len == num_digits and prev_len < num_digits):
    i += 1
    prev_len = curr_len
    curr_len = len(str(fib(i)))
    print(i, prev_len, curr_len)