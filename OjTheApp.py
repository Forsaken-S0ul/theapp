import subprocess
import os
import json

def run_flask_app(app_path, port):
    return subprocess.Popen(['python3', app_path], cwd=app_path, env={'FLASK_RUN_PORT': str(port)})

#know the path to the program
path_to_directroy = os.getcwd()
 #path to the dir where the path.json file will be created and where the apps are
path_to_file = os.path.join(path_to_directroy , 'Rabbit_hole')

process1 = run_flask_app(path_to_file, 5000) 
process1.wait()
    
process2 = run_flask_app(path_to_file, 5001)
process2.wait()

process3 = run_flask_app(path_to_file,  5002)
process3.wait()  

