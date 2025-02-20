from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')

def htop():
    fullName = "Shashank K N"
    Username = os.getenv("USER","Unknown")
    ISTtime = datetime.datetime.utcnow() + datetime.timedelta(hours=5,minutes=30)
    formTime = ISTtime.strftime('%Y-%m-%d %H:%M:%S')
    topOut = subprocess.getoutput("top -b -n 1 | head -10")

    return f"""
    <p>Name : {fullName}</p>
    <p>Username = {Username}</p>
    <p>Server Time (IST) : {formTime}</p>
    <pre>TOP Output: \n{topOut}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
