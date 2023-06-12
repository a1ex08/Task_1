import time

def count_sym(line):
    for sym in set(line):
        counter = 0
        for sub_sym in line:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)

start_time = time.time()
count_sym('abcdefgh'*1000000)
end_time = time.time()
print(end_time-start_time)