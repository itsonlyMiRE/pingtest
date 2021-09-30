# pingtest
## Description
A personal project for testing internet stability, intended for use in Linux. While testing download/upload speed or one-time ping data is great, this tool sends many pings per second and generates a graph to illustrate the ping times in order to indicate the stability of the connection. Inspired by `packetlosstest.com`.

This program now includes GUI functionality. See Usage for more details.
## Setup
This script is written in Python3 and requires the Python3 modules `numpy` and `matplotlib`. Clone the repository and use the command `chmod a+x pingtest` to make the program executable.
## Usage
NOTE: Requires sudo privileges due to small intervals used in the `ping` command. If you do not run the program with sudo, it may prompt you for your password during runtime.

After following Setup notes, simply run with `./pingtest`.

The program now uses command line flags/arguments to set the parameters of the test. Help can be displayed with `./pingtest -h`:
```
usage: pingtest [-h] [-G] [-a <address>] [-d <seconds>] [-f <pings/second>] [-t <milliseconds>]

Pingtest program by mire.

optional arguments:
  -h, --help         show this help message and exit
  -G                 use GUI (all other flags are ignored if this is used)
  -a <address>       address to ping (or use '-a F' to use first hop router)
  -d <seconds>       duration of test (DEFAULT: 10)
  -f <pings/second>  frequency in pings per second (DEFAULT: 50)
  -t <milliseconds>  threshold of acceptable ping time (DEFAULT: 60)
```
Please note that either the -a or -G flag must be used. If the -G flag is used to launch the GUI, all other flags are ignored.
## Notes
As written, this program can only be used in Linux. It could be implemented for Windows, but the `ping` command in Windows does not allow for extremely small interval times between pings, which is useful for getting accurate data.
