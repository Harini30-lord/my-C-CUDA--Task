import subprocess
import sys
import os

def create__virtual_env(env_name):
    try:
        subprocess.run([sys.executable, '-m', 'venv', env_name])
        print(f"Virtual environment '{env_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to create the virtual environment. {e}")

def activate__virtual_env(env_name):
    try:
        activate_script = os.path.join(env_name, 'Scripts' if os.name == 'nt' else 'bin', 'activate')
        subprocess.run([activate_script], shell=True)
        print(f"Activated virtual environment '{env_name}'.")
    except FileNotFoundError:
        print(f"Error: Virtual environment '{env_name}' not found.")

def deactivate__virtual_env():
    try:
        subprocess.run(['deactivate'], shell=True)
        print("Deactivated the virtual environment.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to deactivate the virtual environment. {e}")

def install_package(env_name, package_name):
    try:
        subprocess.run([f'{env_name}/bin/pip', 'install', package_name])
        print(f"Installed '{package_name}' in '{env_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to install the package. {e}")

def upgrade_package(env_name, package_name):
    try:
        subprocess.run([f'{env_name}/bin/pip', 'install', '--upgrade', package_name])
        print(f"Upgraded '{package_name}' in '{env_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to upgrade the package. {e}")

def uninstall_package(env_name, package_name):
    try:
        subprocess.run([f'{env_name}/bin/pip', 'uninstall', '-y', package_name])
        print(f"Uninstalled '{package_name}' from '{env_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to uninstall the package. {e}")

def list_installed_packages(env_name):
    try:
        result = subprocess.run([f'{env_name}/bin/pip', 'list'], capture_output=True, text=True)
        print(f"Installed packages in '{env_name}':\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to list installed packages. {e}")


env_name = "_virtual_env"
package_name = "numpy"

create__virtual_env(env_name)
activate__virtual_env(env_name)
install_package(env_name, package_name)
list_installed_packages(env_name)
upgrade_package(env_name, package_name)
list_installed_packages(env_name)
uninstall_package(env_name, package_name)
list_installed_packages(env_name)
deactivate_virtual_env()
