import subprocess, os
from flask import Flask, request, render_template, send_file
import random, math


app = Flask(__name__)
digits = list("abcdef0123456789")

c = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compile', methods=['POST'])
def compile():
    code = request.form['code']
    global c
    
    c = c+1

    # Save the C code to a temporary file
    sfile = "".join([str(digits[math.floor(random.random() * 10)]) for i in range(10)])
    with open(f"outputs/{sfile}.c", 'w') as file:
        file.write(code)

    # Compile the C code using GDB
    compile_command = f'gcc -o outputs/{sfile} outputs/{sfile}.c'
    result = subprocess.run(compile_command, shell=True, stderr=subprocess.PIPE)

    # Check if the compilation was successful
    if result.returncode == 0:
        # Return the binary as a downloadable file
        resp = send_file(f'outputs/{sfile}', as_attachment=True, download_name='output')
        os.remove(f"outputs/{sfile}")
        os.remove(f"outputs/{sfile}.c")

        return str(c)
    else:
        error_message = result.stderr.decode('utf-8')
        return f"Compilation Error:\n{error_message}"

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8002)
