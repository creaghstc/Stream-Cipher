def LFSR(seed, taps):
    stream, next = seed, 0
    key = [] #initialise the key stream
    while(1): #while period not reached

    	for t in taps:
    		next += int(stream[t-1]) #xor the tap elements of stream

    	if(next%2 == 0.0): #decide if 1 or 0 ( mod 2)
    		next = 0
    	else:
    		next = 1

    	stream = str(next) + stream[:-1] #shift stream to right and add next element
    	next = 0 #reset next for next cycle
    	key.append(stream) #append current stream to the end key stream
    	
    	if(stream == seed): #when period reached, break
    		break

    return "".join(key) #return the key stream

print(LFSR("01100100", (8,6,5,4)))
input("Any Key to close")
