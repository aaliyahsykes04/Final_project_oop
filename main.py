# entry point 
# simply calls the run() function from the CLT

from ui.cli import run 

# means 'onlt run this if we are running main.py directly 
if __name__ == '__main__':
    run()