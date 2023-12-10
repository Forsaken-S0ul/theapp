import subprocess

def run_flask_app(app_path, port):
    return subprocess.Popen(['python', app_path], cwd=app_path, env={'FLASK_RUN_PORT': str(port)})

if __name__ == '__main__':

    process1 = run_flask_app('/home/justanoj/ojtheapp/app.py', 5000)
    process1.wait()

    process2 = run_flask_app('/home/justanoj/ojtheapp/appTwo.py', 5001)
    process2.wait()

    process3 = run_flask_app('/home/justanoj/ojtheapp/TheFinalApp.py', 5002)
    process3.wait()  
