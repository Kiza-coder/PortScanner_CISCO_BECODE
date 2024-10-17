# Port Scanner
*Cristian, Kiza*  
*17/10/2024*

---

## **1. Introduction**

Create a Port Scanner.

- **Objective:** Create a port scanner in python. Test it on VM on a local network.
Improve the knowlegde of python, networking and hypervisor.

- **Scope:** This project cover a networking part and a programming part

- **Technologies Used:** VirtualBox, Linux, Python.

---

## **2. Project Setup and Environment** 


- **Virtual Machine (VM):** 
  - **VM Software:** VirtualBox
- **Steps to Install the OS:** 
  - List step-by-step instructions for setting up the OS.
  - Include screenshots if needed.
  
---



## **3. Code/Script Section**
.

- **Code Explanation:**

  - Class:
    - **Filename:**: PortScanner.py  
    - **Purpose:** This is the class which takes care of attempting a connection to the port of a host and takes care of displaying the result

  - Class:
    - **Filename:**: InvalidPortRangeError.py  
    - **Purpose:** This is the class that takes care of handling special exceptions with custom message

    Class:
    - **Filename:**: SocketTcp.py  
    - **Purpose:** This is the class who represent connexion socket. It's here for change the actual state of this socket.

     Class:
    - **Filename:**: main.py  
    - **Purpose:** This is the class with main the main logic of our program



