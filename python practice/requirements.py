import subprocess

def install_dependencies():
    try:
        subprocess.call(["pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully.")
    except Exception as e:
        print(f"Error installing dependencies: {e}")

install_dependencies()
    
