# # setup.py
# import os
# import subprocess
# import sys
# from pathlib import Path


# def run_setup():
#     print("Starting Moffat Bay Resort setup...")
    
#     # Check Python version
#     if sys.version_info < (3, 9):
#         print("Python 3.9 or higher is required")
#         sys.exit(1)

#     # Create virtual environment
#     print("Creating virtual environment...")
#     subprocess.run([sys.executable, "-m", "venv", "venv"])

#     # Activate virtual environment
#     if os.name == 'nt':  # Windows
#         activate_script = "venv\\Scripts\\activate"
#     else:  # Unix/Linux
#         activate_script = "venv/bin/activate"

#     # Install requirements
#     print("Installing requirements...")
#     pip_cmd = "venv\\Scripts\\pip" if os.name == 'nt' else "venv/bin/pip"
#     subprocess.run([pip_cmd, "install", "-r", "requirements.txt"])

#     # Create .env file if it doesn't exist
#     if not os.path.exists(".env"):
#         print("Creating .env file from template...")
#         with open(".env.example", "r") as example:
#             with open(".env", "w") as env:
#                 env.write(example.read())
#         print("Please update the .env file with your database credentials")

#     # Run migrations
#     print("Running migrations...")
#     manage_cmd = "venv\\Scripts\\python" if os.name == 'nt' else "venv/bin/python"
#     subprocess.run([manage_cmd, "manage.py", "makemigrations"])
#     subprocess.run([manage_cmd, "manage.py", "migrate"])

#     # Collect static files
#     print("Collecting static files...")
#     subprocess.run([manage_cmd, "manage.py", "collectstatic", "--noinput"])

#     print("\nSetup complete!")
#     print("\nTo start the application:")
#     if os.name == 'nt':
#         print("1. .\\venv\\Scripts\\activate")
#     else:
#         print("1. source venv/bin/activate")
#     print("2. python manage.py runserver")

# if __name__ == "__main__":
#     run_setup()   