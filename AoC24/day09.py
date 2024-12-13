import numpy as np

with open("input.01.day09", "r") as fp:
    data = fp.read()

blocks = data[::2]
empties = data[1::2]

blocks_len = [int(c) for c in blocks]
empties_len = [int(c) for c in empties]
print(blocks_len)
print(empties_len)

ranges = np.cumsum([int(c) for c in data])
print(ranges)

checksum = 0
is_in_set_memory = True
curr_range = 0
compact_len = sum(blocks_len)
back_id = len(blocks_len) - 1
for i in range(compact_len):
    while ranges[curr_range] == i:
        is_in_set_memory = not is_in_set_memory
        curr_range += 1
    if is_in_set_memory:
        id = curr_range // 2
    else:
        id = back_id
        blocks_len[back_id] -= 1
        if blocks_len[back_id] == 0:
            back_id -= 1

    print(i, id, is_in_set_memory, ranges[curr_range])

    checksum += i * id

print(checksum)


curr_idx = 0
is_filled = True
id = 0
filled_blocks = []
empty_blocks = []
for c in data:
    if is_filled:
        filled_blocks.append((curr_idx, int(c), id))
        id += 1
    else:
        empty_blocks.append((curr_idx, int(c)))
    curr_idx += int(c)
    is_filled = not is_filled


def find_right_most_free(empty_blocks, block_len):
    assert block_len > 0
    for i in range(len(empty_blocks)):
        assert empty_blocks[i][1] >= 0
        if empty_blocks[i][1] >= block_len:
            return i
    return -1


filled_blocks_new = []
for block in filled_blocks[::-1]:
    id = find_right_most_free(empty_blocks, block[1])
    if id != -1 and empty_blocks[id][0] < block[0]:
        filled_blocks_new.append((empty_blocks[id][0], block[1], block[2]))
        empty_blocks[id] = (
            empty_blocks[id][0] + block[1],
            empty_blocks[id][1] - block[1],
        )
    else:
        filled_blocks_new.append(block)

checksum = 0
for block in filled_blocks_new:
    for i in range(block[0], block[0] + block[1]):
        checksum += i * block[2]
print(checksum)
