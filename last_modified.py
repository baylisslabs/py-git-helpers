from core import run
import dateutil.parser as parser
from datetime import date

if __name__=="__main__":
    filenames = run(["git","ls-tree","-r","--name-only","HEAD"],capture_output=True)
    for filename in filenames.split("\n"):
        if filename:
            modification_time = parser.parse(run(["git","log","-1",'--format="%ad"',"--",filename],capture_output=True).strip(),fuzzy=True)
            if modification_time.date() >= date(2020,1,1):
                print(f"{modification_time} {filename}")
