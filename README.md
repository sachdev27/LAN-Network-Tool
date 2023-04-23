<p align="center">
 <img width=500px height=200px src="https://user-images.githubusercontent.com/54627871/233844044-12d0dc04-502a-4183-af38-3e97ed3ea9bd.png" alt="Project logo">
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
- traceroute


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

<div align=center>
<img width=500px height=200px src="https://user-images.githubusercontent.com/54627871/233844044-12d0dc04-502a-4183-af38-3e97ed3ea9bd.png" alt="Project logo">

<img width=400px height=200px src="https://user-images.githubusercontent.com/54627871/233844760-7250da76-5c02-4249-bd47-38fb9f74b079.png">
 </div>


2. Speed Test
This module uses the speedtest-cli library to test the download and upload speed of your Internet connection. It returns the download and upload speed in Mbps.

<div align=center>
<img width=500px height=300px src="https://user-images.githubusercontent.com/54627871/233844825-cd04e0e3-0e9a-4c63-a69b-a8bab43913b5.png">
 </div>

3. DOS Attack
This module uses Scapy to launch a DOS attack on a target device. It sends a large number of packets to the target device, overwhelming it and causing it to crash or become unresponsive. This module should only be used for testing purposes on a network that you own.

<div align=center>
<img width=500px height=300px src="https://user-images.githubusercontent.com/54627871/233844965-9213e40f-64a8-48d8-9ba3-002226ce3651.png">
<img width=500px height=400px src="https://user-images.githubusercontent.com/54627871/233844999-5073508d-0eef-4dc4-ad32-41246c070d27.png">
 </div>


4. Traceroute module: This module uses the CMDLine to perform a traceroute analysis of the network. It identifies the exact hop at which the packet is being dropped and provides the necessary information to diagnose the issue.

- Connection Type: The first condition that is checked is whether the user is connected to a Wi-Fi or Ethernet network. This can be important because different types of connections can have different bandwidths, latency, and reliability characteristics that may affect the user's ability to access the internet.
- Gateway Connection: The next condition that is checked is whether the user can connect to the gateway, which is the device that connects the user's network to the internet. If the user is unable to connect to the gateway, it may indicate a problem with the user's network configuration or hardware.
- Packet Loss: The third condition that is checked is whether the user's packets are getting dropped within the internet. This can be caused by various factors, such as network congestion, routing issues, or faulty network hardware. If packets are getting dropped, it may result in slow or inconsistent internet performance.
- Internet Access: The final condition that is checked is whether the user is able to access the internet. This includes checking whether websites or online services can be accessed, and whether internet-based applications are able to function properly. If the user is unable to access the internet, it may indicate a problem with the user's network, service provider, or the internet as a whole.

<div align=center>
<!-- <img width=400px height=400px src="https://user-images.githubusercontent.com/54627871/233845280-2dc98a2c-f613-48d8-a13e-2a9345f7a727.png"> -->
<img width=600px height=200px src="https://user-images.githubusercontent.com/54627871/233845290-49512371-be4a-4b81-98e5-ed0a075142a1.png">
<img width=600px height=200px src="https://user-images.githubusercontent.com/54627871/233845297-918cc3db-559f-40a6-9a7d-1ad2d29e9e16.png">
<img width=600px height=200px src="https://user-images.githubusercontent.com/54627871/233845300-86db7cb5-deaf-43c4-b2fd-647cb1b84045.png">
 </div>



## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Programming Language
- [Scapy](https://scapy.net/) - Packet Manipulation
- [speedtest-cli](https://pypi.org/project/speedtest-cli/) - Internet Speed Testing


## ✍️ Authors <a name = "authors"></a>

- [Benedikt Waldvogel](https://github.com/bwaldvogel) - Idea & Initial work


