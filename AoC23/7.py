from collections import Counter

with open("7.input", "r") as fp:
    data = fp.read().splitlines()

TABLE = "AKQJT98765432"
TABLE2 = "AKQT98765432J"

TABLE = TABLE[::-1]
TABLE2 = TABLE2[::-1]


def get_kind(hand):
    d = Counter(hand)

    vals = list(d.values())
    vals.sort()
    if vals[-1] == 5:
        val = 7
    elif vals[-1] == 4:
        val = 6
    elif vals[-1] == 3 and vals[-2] == 2:
        val = 5
    elif vals[-1] == 3:
        val = 4
    elif vals[-1] == 2 and vals[-2] == 2:
        val = 3
    elif vals[-1] == 2 and vals[-2] == 1:
        val = 2
    else:
        val = 1

    val *= 10**12
    return val


def get_lex(hand, table=TABLE):
    val = 0
    for i, c in enumerate(hand):
        val += table.find(c) * len(table) ** (5 - i)
    return val


def evaluate(hand):
    return get_kind(hand) + get_lex(hand)


def evaluate2(hand):
    if "J" in hand:
        hand1 = hand.replace("J", "")
        if len(hand1) == 0:
            max_k = [TABLE2[-1]]
        else:
            c = Counter(hand1)
            max_c = c.most_common(1)[0][1]
            max_k = [key for key in c if c[key] == max_c]
            max_k.sort(key=lambda x: TABLE2.find(x))

        return get_kind(hand.replace("J", max_k[-1])) + get_lex(hand, table=TABLE2)
    else:
        return get_kind(hand) + get_lex(hand, table=TABLE2)


data = [line.split(" ") for line in data]
data.sort(key=lambda x: evaluate2(x[0]))

res = 0
for rank, (hand, bid) in enumerate(data):
    res += (rank + 1) * int(bid)

print(res)
