#!/usr/bin/env python
import subprocess

blocklist=["src/Terminal/Terminal/Bootstrapping/ServiceRegistration.cs"]

def rejectCommit(msg):
    print(msg)
    exit(-1)

if __name__=="__main__":
    status = subprocess.run(["git","diff","--name-only","--cached"],capture_output=True,text=True)
    if status.returncode not in [0]:
        raise Exception(f"process return non-zero result: {status.returncode} {status.stderr}")
    staged = [s for s in status.stdout.split("\n") if s]

    for blocked in blocklist:
        if any(s==blocked for s in staged):
            rejectCommit(f"did you mean to commit the file: {blocked}")

