import subprocess, re, sys, numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
from time import time

# initialize strings
addr = ""
pings = ""
threshold = ""

# define regional IP addresses
west_ip = "144.34.177.76"
central_ip = "64.250.60.2"
east_ip = "52.128.196.134"

try:
    # check for arguments to use as ping parameters
    if len(sys.argv) == 4:
        addr = sys.argv[1]
        pings = sys.argv[2]
        threshold = sys.argv[3]

    # prompt user for parameters if improper args found
    else:
        print("\n> NOTE: you can enter command line arguments as follows:\n> python3 pingtest.py [target IP or domain] [number of pings] [acceptable ping threshold in ms]")
        addr = input("\n> enter IP or domain to test (W/C/E for U.S. regional tests; blank for google.com): ")
        pings = input("> enter number of pings (blank for 200): ")
        threshold = input("> enter acceptable ping in ms (blank for 60ms): ")

    # replace values for parameters
    if addr == "":
        addr = "google.com"
    elif addr == "W":
        addr = west_ip
    elif addr == 'C':
        addr = central_ip
    elif addr == 'E':
        addr = east_ip
    if pings == "":
        pings = "200"
    if threshold == "":
        threshold = "60"

    # begin pinging using chosen arguments
    print(f"\n> starting {pings} pings on {addr}...")
    start = time()
    output = str(subprocess.check_output(f"sudo ping {addr} -i 0.02 -c {pings}", shell=True))

    # extract ping summary from end of output and print
    times_summary = re.findall("rtt min/avg/max/mdev = .* ms", output)
    print(f"> ping summary: {times_summary[0]}")

    # extract ping data from output
    times = re.findall("time=\d+\.*\d* ms", output)
    for i in range(len(times)):
        times[i] = round(float(times[i].replace("time=", "").replace(" ms", "")))

    # set x and y values
    x=[]
    for i in range(1,len(times)+1):
        x.append(i)
    y = np.array(times)

    # define thresholds
    above_threshold = np.maximum(y - int(threshold), 0)
    below_threshold = np.minimum(y, int(threshold))

    # create bar graph using data
    try:
        fig, ax = plt.subplots()
        ax.bar(x, below_threshold, 0.35, color="g")
        ax.bar(x, above_threshold, 0.35, color="r",
                bottom=below_threshold)
        ax.axhline(int(threshold), color="gray")
    except ValueError:
        print("> OOPS! ValueError, something went wrong. Try again.\n")
        exit()

    # closing, show graph
    print("> time elapsed:", str(round(time() - start, ndigits=3)), "seconds")
    print("> showing charted results...\n")
    plt.show()

except KeyboardInterrupt:
    print("\n")
    exit()