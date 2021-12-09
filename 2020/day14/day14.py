from itertools import combinations_with_replacement

#Part 1 solution:
def convert_to_binary(value_string, current_mask):
    bin_value = str(bin(int(value_string))[2:])
    while len(bin_value) < len(current_mask):
        bin_value = "0" + bin_value
    return bin_value

def convert_to_integer(bin_string):
    integer_value = int(bin_string, base=2)
    return integer_value

def mask_bin_value(bin_value, current_mask):
    masked_value = []
    for i in range(len(current_mask)):
        if current_mask[i] == "X":
            masked_value.append(bin_value[i])
        else:
            masked_value.append(current_mask[i])
    return "".join(masked_value)

def unpack_instructions(text):
    memory = {}
    current_mask = ""
    result = 0
    with open(text, "r") as f:
        instructions = f.read()
    
    for line in instructions.split("\n"):
        instruction = line.split(" = ")
        
        if instruction[0] == "mask":
            current_mask = instruction[1]
            continue

        elif "mem" in instruction[0]:
            mem_bit = instruction[0][instruction[0].find("[")+1:instruction[0].find("]")]
            memory[mem_bit] = convert_to_integer(mask_bin_value(convert_to_binary(instruction[1], current_mask),current_mask))
        else:
            pass
    
    for i in memory.values():
        result += i

    return result

#part1 answer: print(unpack_instructions("input.txt"))

#Part 2 solution:

def convert_to_binary(mem_bit_string, current_mask):
    bin_value = str(bin(int(mem_bit_string))[2:])
    while len(bin_value) < len(current_mask):
        bin_value = "0" + bin_value
    return bin_value

def mask_bin_value(bin_mem_bit, current_mask):
    masked_value = []
    x_values = 0
    for i in range(len(current_mask)):
        if current_mask[i] == "X":
            x_values += 1
            masked_value.append(current_mask[i])
        elif current_mask[i] == "1" or bin_mem_bit[i] == "1":
            masked_value.append("1")
        else:
            masked_value.append("0")
    return "".join(masked_value), x_values

def check_floating_bits(bin_mem_bit, x_values):
    if x_values != 0:

        one_list = ["1" for _ in range(2**x_values-1)]
        zero_list = ["0" for _ in range(2**x_values-1)]
        bit_variation_list = one_list + zero_list
    for i in bit_variation_list:
        var_list2.append(i)
