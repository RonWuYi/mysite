import subprocess

def run_code(code):
    output = subprocess.check_output(['python', '-c', code],universal_newlines=True)
    return output

code = """print('Test code')"""
code1 = """import os \r\nprint(os.getcwd())"""
code1 = """import os \r\nos.system('ssh -T git@github.com')"""
print(run_code(code1))