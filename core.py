import subprocess

def run(args,capture_output=False,success=[0],input=None):
    #print(args)
    status = subprocess.run(args,capture_output=capture_output,text=True,input=input)
    if status.returncode not in success:
        raise Exception(f"process return non-zero result: {status.returncode} {status.stderr}")
    return status.stdout

def readFile(filename):
    with open(filename,"r") as f:
        return f.read()
