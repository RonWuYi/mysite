from werkzeug.security import generate_password_hash, check_password_hash
my_string = b'\x80\x03c__main__\nProcessData\nq\x00)\x81q\x01}q\x02X\x04\x00\x00\x00dataq\x03X\x0b\x00\x00\x00ABCDEFGHIJKq\x04sb.'
hash = generate_password_hash(my_string)


print(hash)

print(check_password_hash(hash, my_string))
