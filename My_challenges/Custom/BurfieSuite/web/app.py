from flask import Flask, render_template, request, jsonify
import socket
import re
import logging

app = Flask(__name__)

host = ""
ftphost = socket.gethostbyname("ftpy")
with open("/etc/hosts") as f:
    host = f.readlines()[-1].split("\t")[0]

@app.route('/')
def index():
    return render_template('index.html', host=host, ftphost=ftphost)

@app.route('/forward_request', methods=['POST'])
def forward_request():
    try:
        req_json= request.get_json()
        headers = req_json['headers']
        headers = headers.replace("\n", "\r\n")
        body = req_json['body']

        logging.error(f"[+] headers: {headers}")
        target_host, target_port = parse_host(headers)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((target_host, target_port))
        request_message = f"{headers}"

        client_socket.send(request_message.encode())

        response = b''
        while True:
            chunk = client_socket.recv(9216)
            logging.error(f"[+] chunk: {chunk}")
            if not chunk:
                break
            response += chunk

        
        client_socket.close()

        response_data = response.decode()

        return jsonify({'response': response_data})

    except Exception as e:

        return jsonify({'error': str(e)}), 500

@app.route('/socket', methods=['POST'])
def portmapper():

    HOST, PORT = "", request.form['port']
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        soc.bind((HOST, int(PORT)))
        
    except socket.error as message:
        return 'Bind failed. Error Code : ' + str(message[0]) + ' Message ' + message[1]
        sys.exit()

    print('Socket binding operation completed')
    soc.settimeout(10)
    soc.listen(9)

    try:
        conn, address = soc.accept()
        data = conn.recv(2048)
    except:
        data = "No data received"

    return jsonify({'Response': str(data)}), 200


def parse_host(http_headers):
    pattern = r"Host:\s+([^:]+)(?::(\d+))?"
    match = re.search(pattern, http_headers)
    if match:
        host = match.group(1)
        port = int(match.group(2)) if match.group(2) else 80
        return host, port
    else:
        return None, None


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, host="0.0.0.0", port=8000)
