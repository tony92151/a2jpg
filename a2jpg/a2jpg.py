import time
import sys, os
from concurrent.futures import ThreadPoolExecutor
import argparse
from pathlib import Path
import subprocess
toolbar_width = 40

def roll_output(proc, file=None):
    # https://www.endpoint.com/blog/2015/01/28/getting-realtime-output-using-python
    while True:
        output = proc.stdout.readline()
        if proc.poll() is not None:
            break
        if output:
            if file is None:
                print(output.decode('utf-8').splitlines()[0])
            else:
                f = open(file, "a")
                f.write(output + "\n")
                f.close()

    rc = proc.poll()
    print("End output, PID : {}".format(proc.pid))

def command_run(command, result=False):
    #print("\n $ {}".format(command))
    #print("\n")
    proc = subprocess.Popen(
        command, shell=True,
        stdout=subprocess.PIPE)
    if result:
        roll_output(proc)
    proc.wait()
    
# def run_command():
#     with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#         future_to_url = {executor.submit(get_content, url): url for url in URLS}
#         for future in concurrent.futures.as_completed(future_to_url):


# for i in range(toolbar_width):
#     time.sleep(0.1) # do real work here
#     print("({}/{})\t{}".format(i,toolbar_width), end="\r")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help="input image or path.", type=str, default=None)
    parser.add_argument('-f', help="image format (Default: *.ARW)", type=str, default="*.ARW")
    parser.add_argument('-c', help="quality in % (Default: 100)", type=int, default=100)
    parser.add_argument('-w', help="number of worker (Default: 2)", type=int, default=2)
    args = parser.parse_args()

    # search
    img_path = os.path.abspath(args.i)
    img_list = list(Path(img_path).glob(args.f))

    img_convert_list = [[str(i.absolute()), os.path.join(os.path.dirname(i), "jpg", i.name.replace(args.f.split(".")[-1], "jpg"))]for i in img_list]

    # print(img_convert_list)
    for i,v in enumerate(img_convert_list):
        os.makedirs(os.path.dirname(v[1]), exist_ok=True)
        command = "sips -s format jpeg {} --out {}".format(v[0], v[1])
        command_run(command)
        if i == len(img_convert_list)-1:
            print(" ({}/{})\t{}".format(i+1, len(img_convert_list), v[1]))
        else:
            print(" ({}/{})\t{}".format(i + 1, len(img_convert_list), v[1]), end="\r")


    # if not args.w == 1:
    #     with ThreadPoolExecutor(max_workers=args.w) as executor:






    # if not args.w == 1:
    #     executor.shutdown(True)



    

