from utils import unit_frac_rep

d = 1001
l = []
for i in range(1,d):
    rep, seen_num = unit_frac_rep(i)
    rec_cycle_len = len(seen_num) - seen_num.index(seen_num[-1]) - 1
    l.append(rec_cycle_len)
    print(i, rec_cycle_len)

print(max(l))
