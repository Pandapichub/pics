import os
import time
def push():
    os.system('git add .')
    os.system('git commit -m \"test\" ')
    os.system('git push -u origin master')

if __name__ == "__main__":
    push()
    for i in range(10):
        print("suki")
        time.sleep(1)
    