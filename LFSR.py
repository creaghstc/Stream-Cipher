def LFSR(seed, taps, size):
    stream, nextBit = seed, 0
    key = []  # initialise the key stream
    while 1:  # while period not reached

        for t in taps:
            nextBit += int(stream[t - 1])  # xor the tap elements of stream

        if nextBit % 2 == 0.0:  # decide if 1 or 0 ( mod 2)
            nextBit = 0
        else:
            nextBit = 1

        stream = str(nextBit) + stream[:-1]  # shift stream to right and add next element
        nextBit = 0  # reset next for next cycle
        key.append(stream)  # append current stream to the end key stream

        if len(key) == size:  # when period reached, break
            break

    return "".join(key)  # return the key stream

# print(LFSR("01100100", (8,6,5,4),8))
# input("Any Key to close")
