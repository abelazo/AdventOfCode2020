
def get_instruction(instruction):
    return instruction[0:3]

def get_number(instruction):
    return int(instruction.split(' ')[1])

def execute(instruction, counter, offset):
    # Debug
    #print("Executing {}: {}".format(offset, instruction))
    if get_instruction(instruction) == 'nop':   # nop
        offset += 1
    elif get_instruction(instruction) == 'acc': # acc
        counter += get_number(instruction)
        offset += 1
    else:                                       # jmp
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
    last_offset = 0
    executed_instructions = set()
    while not has_been_executed(executed_instructions, offset) and offset < len(program):
        instruction = program[offset]
        last_offset = offset
        offset, counter = execute(instruction, counter, offset)
        
    if (last_offset + 1 != len(program)):
        execution_result = False
        print("Endless loop found. Counter value: {}".format(counter))        
    else:
        execution_result = True
        print("Program finished succesfully. Counter value: {}".format(counter))
    return execution_result


def replace(program, offset, new_instruction):
    program_copy = program.copy()
    program_copy[offset] = new_instruction
    return program_copy


def solve_2(program):
    for i in range(len(program)):
        instruction = program[i]
        if get_instruction(instruction) == 'nop':
            new_instruction = instruction.replace('nop', 'jmp')
            if solve_1(replace(program, i, new_instruction)):
                return
        elif get_instruction(instruction) == 'jmp':
            new_instruction = instruction.replace('jmp', 'nop')
            if solve_1(replace(program, i, new_instruction)):
                return
    
if __name__ == '__main__':
    with open('Instructions.txt') as f:
        program = [line.strip() for line in f.readlines()]

    solve_1(program)
    solve_2(program)

# if __name__ == '__main__':
#     program = ['nop +0',
#                'acc +1',
#                'jmp +4',
#                'acc +3',
#                'jmp -3',
#                'acc -99',
#                'acc +1',
#                'jmp -4',
#                'acc +6']
#
#     solve_1(program)
#     solve_2(program)
 
