
Controlling the Device with LAN/Ethernet (HTTP and TELNET Protocols):

Communication with the device by Ethernet can be via either static, or dynamic IP Address. 
Factory default is Dynamic IP Address using TCP/IP Port 80 for HTTP Protocol and Port 23 for Telnet Protocol.

Dynamic IP: Device is assigned the local Subnet mask, network gateway and a valid local IP address by 
the network server each time it is connected to the network. the only parameters the user can control in this mode are

1. HTTP Port - The TCP/IP Port the device will use to communicate with the network when operating via HTTP control.
   May be set by user to desired value.

Note:  If HTTP PORT is other than 80 it must be included in every HTTP command, see example below.
       Telnet Port is 23 and can not be changed.

2. Password - a Password (up to 20 characters) can be used to secure commands to the device. 
Factory default is not to use a password.


Static IP: All parameters must be specified by the user using the USB Interface:

1. IP Address - The IP Address of the device - must be a legal and unique IP in the local Network.
2. Subnet Mask - The Subnet Mask of your Local Network.
3. Network Gateway - The Network Gateway of your Firewall.

Tip: In Windows the Subnet Mask and Network Gateway can be found by running the command "IPConfig".

4. HTTP Port - The TCP/IP Port the device will use to communicate with the network when operating via HTTP control.
May be set by user to desired value in the 1-255 range.

Note:  If HTTP PORT is other than 80 it must be included in every HTTP command, see example below.
       Telnet Port is 23 and can not be changed.

5. Password - a Password (up to 20 characters) can be used to secure commands to the device.
Factory default is not to use a password.

Note: clicking on on the arrow between the Dynamic and static IP configurations will copy the current
Dynamic configuration to the static configuration.


Clicking on the "Store..." Button will store all the Ethernet parameters in the device and reset the 
devise allowing the parameters to come into effect immediatly.



Communication With the Device with HTTP Protocol:

Communication with the device is done by Sending HTTP commands (Get/Post HTTP).
Get/Post HTTP is very common and simple to implement in almost any Programming Langauge.
Internet Browser may be used as a console/tester.

every command will start with "http://DeviceIP/"
If the PORT is other than 80 then the HTTP will have to start with: "http://DeviceIP:PORT/"
(80 is the default HTTP PORT and can be ommited).

the second part of the HTTP command can be:
1. COMMAND/QUERY (example: SETATT=15.25  will set Attenuation to 15.25 dB , above inserssion loss). 
2. PWD=[Password]. 

Example of typical HTTP command for Setting Attenuation to 15.25 dB:

1. When Password is not used and port=80 :
http://10.0.100.100/SetAtt=15.25  ( case insensitive )
2. When PORT=800
http://10.0.100.100:800/SetAtt=15.25
3. When PORT=800, Password is required and is 1234
http://10.0.100.100:800/PWD=1234;SetAtt=15.25

if the device recieves the http command then it will return a result.

Example of a typical HTTP command for sending a Query to the device.
1. When Password is not used and port=80 :
http://10.0.100.100/ATT?
2. When PORT=800
http://10.0.100.100:800/ATT?
3. When PORT=800, Password is required and is 1234
http://10.0.100.100:800/PWD=1234;ATT?

if the device recieve the http command then it will return the answer in Ascii text format.



Communication With the Device with Telnet Protocol:

Communication with the device started by creating a Telnet Connection and receiving LF (Line feed) from the Device.
if Password is required then the first command that must be sent is: PWD=[Password].
any legal command can be send in Telnet and must be followed by LF (Line Feed).


