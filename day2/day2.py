fileObject = open("input.txt", "r")
init_input = fileObject.readline()
init_input = list(map(int, init_input.split(',')))

for noun in range(0, 100):
    for verb in range(0, 100):
        input = init_input.copy()
        input[1] = noun
        input[2] = verb

        idx = 0
        opcode = input[idx]

        while opcode != 99:
            if opcode == 1:
                input[input[idx+3]] = input[input[idx+1]] + input[input[idx+2]]

            elif opcode == 2:
                input[input[idx+3]] = input[input[idx+1]] * input[input[idx+2]]

            idx += 4
            opcode = input[idx]

        if input[0] == 19690720:
            print(100* noun + verb)
