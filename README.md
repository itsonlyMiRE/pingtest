# pingtest
## Description
A personal project for testing internet stability, intended for use in Linux. While testing download/upload speed or one-time ping data is great, this tool sends many pings per second and generates a graph to illustrate the ping times in order to indicate the stability of the connection. Inspired by `packetlosstest.com`.
## Setup
This script is written in Python3 and requires the Python3 modules `numpy` and `matplotlib`.
## Usage
NOTE: Requires sudo privileges due to the interval of 0.02s used in the `ping` command.

Running the program with `python3 pingtest.py` leads to the menu system of the program where the user can input the parameters they want to use for the ping test.

The program can also be used with command line arguments as follows:

```python3 pingtest.py [target IP or domain] [number of pings] [acceptable ping threshold in ms]```

In either use case, a graph will be generated after the ping test is done to display the ping times. A threshold of acceptable response time for the pings can be set, and will be shown on the graph.
## Notes
As written, this program can only be used in Linux. It could be implemented for Windows, but the `ping` command in Windows does not allow for extremely small interval times between pings, which is useful for getting accurate data.
