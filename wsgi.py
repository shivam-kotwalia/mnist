import subprocess
import os
import sys
tefla_path = os.path.join(os.getcwd(), 'app', 'tefla')
print(tefla_path)

#comment this if ruuning locally
subprocess.check_output(["pip", "install","-e", tefla_path])
sys.path.append(tefla_path)
print(sys.path)

from app.app import app

if __name__ == "__main__":
    app.run()