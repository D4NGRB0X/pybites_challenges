import random
import string

def gen_key(parts: int = 4, chars_per_part: int =8)-> str:
    chars = string.ascii_uppercase + string.digits
    blocks = []
    while len(blocks) < parts:
        block = ''.join([random.choice(chars) for item in range(chars_per_part)])
        blocks.append(block)

    generated_key = '-'.join(blocks)
    
    return generated_key