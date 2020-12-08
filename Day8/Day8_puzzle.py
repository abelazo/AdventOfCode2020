
def get_instruction(instruction):
    return instruction[0:3]

def get_number(instruction):
    return int(instruction.split(' ')[1])

def execute(instruction, counter, offset):
    print("Executing {}: {}".format(offset, instruction))
    if get_instruction(instruction) == 'nop':
        offset += 1
    elif get_instruction(instruction) == 'acc':
        counter += get_number(instruction)
        offset += 1
    else:
        offset += get_number(instruction)
    return offset, counter

def has_been_executed(executed_instructions, offset):
    if offset in executed_instructions:
        return True
    else:
        executed_instructions.add(offset)
        return False

def solve_1(program):
    offset = 0
    counter = 0
    executed_instructions = set()
    while not has_been_executed(executed_instructions, offset):
        instruction = program[offset]
        next_offset,next_counter = execute(instruction, counter, offset)
        offset = next_offset
        counter = next_counter
    print(counter)
    

#def solve_2():
#    pass
    
    
if __name__ == '__main__':
    with open('Instructions.txt') as f:
        program = [line.strip() for line in f.readlines()]

    solve_1(program)
     #solve_2()

#if __name__ == '__main__':
#    program = ['nop +0',
#               'acc +1',
#               'jmp +4',
#               'acc +3',
#               'jmp -3',
#               'acc -99',
#               'acc +1',
#               'jmp -4',
#               'acc +6']
#    solve_1(program)
#
