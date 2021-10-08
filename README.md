# pingtest
## Description
A personal project for testing internet stability, intended for use in Linux and Windows. While testing download/upload speed or one-time ping data is great, this tool can send many pings per second and generates a graph to illustrate the ping times in order to indicate the stability of the connection. Inspired by `packetlosstest.com`.

This program now includes GUI functionality. See Usage for more details.
## Setup
This script is written in Python3.

The requirements can be installed with the following commands in Linux:
```
sudo apt install python3-tk &&
sudo apt install traceroute &&
pip install matplotlib &&
pip install numpy
```
Modify as needed depending on your package manager. For Windows, `tracert` is used instead of `traceroute`, and it should already be installed. Tkinter also might be installed with Python3, I'm not entirely sure as I've seen it both ways.

On Linux, clone the repository and either run `pingtest` file with Python3, or use the command `chmod a+x pingtest` to make the program executable as a script.

On Windows, clone the repository and run `pingtest` file with Python3.
## Usage
NOTE: On Linux, if threading isn't used, requires sudo privileges due to small intervals used in the `ping` command. If you run the program with neither sudo nor threading, it may prompt you for your password during runtime.

NOTE: On Windows, if threading isn't used, the maximum interval between pings is just one second. This nearly defeats the purpose of the program, so utilizing the `-T` flag to enable threading is highly recommended, as this allows for more than one ping per second.

After following Setup notes, run with `./pingtest` or `python3 pingtest` on Linux, or `python pingtest.py` on Windows, followed by any desired flags.

The program now uses command line flags/arguments to set the parameters of the test. Help can be displayed with `./pingtest -h`:
```
usage: pingtest [-h] [-G] [-a <address>] [-d <seconds>] [-f <pings/second>] [-t <milliseconds>] [-T]

 ____ ____  ____    ____  ______    ___  _____ ______ 
|    \    ||    \  /    ||      |  /  _]/ ___/|      |
|  o  )  | |  _  ||   __||      | /  [_(   \_ |      |
|   _/|  | |  |  ||  |  ||_|  |_||    _]\__  ||_|  |_|
|  |  |  | |  |  ||  |_ |  |  |  |   [_ /  \ |  |  |  
|  |  |  | |  |  ||     |  |  |  |     |\    |  |  |  
|__| |____||__|__||___,_|  |__|  |_____| \___|  |__|  
                                                      
Pingtest program by mire
https://github.com/itsonlyMiRE/pingtest

optional arguments:
  -h, --help         show this help message and exit
  -G                 use GUI (all other flags are ignored if this is used)
  -a <address>       address to ping (or use '-a F' to use first hop router)
  -d <seconds>       duration of test (DEFAULT: 10)
  -f <pings/second>  frequency in pings per second (DEFAULT: 50, but 1 on Windows unless using threading)
  -t <milliseconds>  threshold of acceptable ping time (DEFAULT: 60)
  -T                 enable threading approach (highly recommended for Windows users)
```
Please note that either the -a or -G flag must be used. If the -G flag is used to launch the GUI, all other flags are ignored.
## Notes
~~As written, this program can only be used in Linux. It could be implemented for Windows, but the `ping` command in Windows does not allow for extremely small interval times between pings, which is useful for getting accurate data.~~

Now supports Windows! Threading highly recommended.

Next is Mac, coming soon-ish.
