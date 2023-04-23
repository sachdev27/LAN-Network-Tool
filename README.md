<p align="center">
  <a href="" rel="noopener">
 <img width=500px height=200px src="https://user-images.githubusercontent.com/54627871/233844044-12d0dc04-502a-4183-af38-3e97ed3ea9bd.png" alt="Project logo"></a>
</p>

<h3 align="center">Python Networking Toolbox</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---


## Description

This Python script is a collection of modules that allows you to perform various networking tasks, including device scanning, speed testing, DOS attacks, and Internet connection diagnostics. The script uses the Scapy library for scanning and DOS attacks, the speedtest-cli library for speed testing, and the built-in Python libraries for Internet connection diagnostics.

## Screenshots




## Requirements

To run this script, you will need the following:

- Python 3.6 or higher
- Scapy library
- speedtest-cli library


## Usage

To use this script, simply run the main.py file. You will be prompted to choose which task you want to perform. Follow the on-screen instructions to complete the task.

The directory consist of a Virtual Environment, which is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.

Enter into the Virtual Environment by running the following command:

```bash
source network/bin/activate
```

## Modules

1. Device Scanner
This module uses Scapy to scan for devices on the network. It sends an ARP request to the broadcast address and listens for responses. The module returns a list of devices with their IP and MAC addresses.

2. Speed Test
This module uses the speedtest-cli library to test the download and upload speed of your Internet connection. It returns the download and upload speed in Mbps.

3. DOS Attack
This module uses Scapy to launch a DOS attack on a target device. It sends a large number of packets to the target device, overwhelming it and causing it to crash or become unresponsive. This module should only be used for testing purposes on a network that you own.

4. Traceroute module: This module uses the CMDLine to perform a traceroute analysis of the network. It identifies the exact hop at which the packet is being dropped and provides the necessary information to diagnose the issue.


## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Programming Language
- [Scapy](https://scapy.net/) - Packet Manipulation
- [speedtest-cli](https://pypi.org/project/speedtest-cli/) - Internet Speed Testing


## ✍️ Authors <a name = "authors"></a>

- [Benedikt Waldvogel](https://github.com/bwaldvogel) - Idea & Initial work


