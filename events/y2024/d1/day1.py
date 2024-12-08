def part1():
    inputs_collumn1 = []
    inputs_collumn2 = []

    with open('./events/y2024/d1/inputs.txt', 'r') as inputs_file:
        for line in inputs_file:
            inputs_collumn1.append(line.split('   ')[0])
            inputs_collumn2.append(line.split('   ')[1].replace("\n", ""))

    inputs_collumn1.sort()
    inputs_collumn2.sort()

    total_distance = 0

    for i in range(0, inputs_collumn1.__len__()):
        total_distance += abs(int(inputs_collumn2[i]) - int(inputs_collumn1[i]))

    print(total_distance)

def part2():
    inputs_collumn1 = []
    inputs_collumn2 = []

    with open('./events/y2024/d1/inputs.txt ', 'r') as inputs_file:
        for line in inputs_file:
            inputs_collumn1.append(line.split('   ')[0])
            inputs_collumn2.append(line.split('   ')[1].replace("\n", ""))
    inputs_collumn1.sort()

    similarity_score = 0
    for i in range(0, inputs_collumn1.__len__()):
        for j in range(0, inputs_collumn2.__len__()):
            if inputs_collumn1[i] == inputs_collumn2[j]:
                similarity_score = similarity_score + int(inputs_collumn1[i])
    
    print(similarity_score)


