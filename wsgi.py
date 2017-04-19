import subprocess, os, sys


tefla_path = os.path.join(os.getcwd(), 'app', 'tefla')

# comment this if running locally
subprocess.check_output(["pip", "install","-e", tefla_path])
sys.path.append(tefla_path)

from app.app import app

if __name__ == "__main__":
    app.run()
