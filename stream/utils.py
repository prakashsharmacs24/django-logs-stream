BLOCK_SIZE = 1024
def get_last_lines( f, lines=10 ):
    f.seek(0, 2)
    block_end_byte = f.tell()
    temp_line = lines
    block_number = -1
    blocks = [] 
    while temp_line > 0 and block_end_byte > 0:

        if (block_end_byte - BLOCK_SIZE > 0):
            f.seek(block_number*BLOCK_SIZE, 2)
            blocks.append(f.read(BLOCK_SIZE).decode())
        else:
            f.seek(0,0)
            blocks.append(f.read(block_end_byte).decode())

        lines_found = blocks[-1].count('\n')
        temp_line -= lines_found
        block_end_byte -= BLOCK_SIZE
        block_number -= 1
    res = ''.join(reversed(blocks))
    return res.splitlines()[-lines:]