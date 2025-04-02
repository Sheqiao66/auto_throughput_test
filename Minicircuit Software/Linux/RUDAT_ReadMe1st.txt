Programming Instruction of using mini-circuits RS232/USB Digital Step Attenuator

The RUDAT (RS232/USB Digital Attenuator)  has 2 control options:

1. HID USB control.
2. RS232 Control. 

For option 1: using HID USB for communicate with the device:

Connect the USB socket to USB port in computer.

LINUX and Windows Programmers who familiar with open connection to
USB HID devices can easily communicate with this device.

To create a connection to the HID USB -  Vendor ID and Product ID are required:

Mini-Circuits Vendor ID is: 0x20CE
RUDAT Product ID is : 0x23


The communication with the device is done by USB Interrupt.
The Transmit and receive buffer size is 64 bytes.

Transmit Array should be 64 bytes
Receive  Array should be 64 bytes

the 1st byte of the Recieved array always will be the same value of the 1st byte as it was in the Trnsmit array.


commands:

1. Read Device Model Name:

To get the device model name you should send to the device code number 40 within the 1st byte of the 64 total.
and also the Frequency value for the correction cal factors. 
The Frequency is in MHz and Should be Integer Value split into 2 bytes (MSB and LSB)

1st byte=40 
2nd byte =0
3rd byte =0
.
.
.
#64 byte=0


The model name will be return in the receive array in ascii characters ending with 0.
1st byte=40
2nd byte to the byte with value=0 = [model name]


2. Get Device Serial Number
To get the device Serial Number , code number 41 should be send
1st byte=41
The Serial Number will be return in the receive array in ascii characters ending with 0.
1st byte=41
2nd byte to the byte with value=0 = Serial Number


3. Set Attenuation

1st byte is the code number should be send is as follows:
for Models: RUDAT-3000-50 , RUDAT-3000-60 code is 15.
for Models: RUDAT-6000-90", RUDAT-6000-60, RUDAT-6000-30  code is 19.

2nd byte is  the integer value of the required attenuation, for example for Attenuation of 55.25 the 2nd byte=55.
3rd byte to byte is the (RequiredAttenuation-2ndByte)*4. for example for Attenuation of 55.25 the 3rd byte=1.
The 64 returned array bytes will be as follows:
on success the 1st byte returned will be the same value of the 1st byte that was sent. 

4. Read the Current Attenuation
1st byte is the code number should be send is as follows:
for Models: RUDAT-3000-50 , RUDAT-3000-60 code is 16.
for Models: RUDAT-6000-90", RUDAT-6000-60, RUDAT-6000-30  code is 18.



5. Send SCPI Command
1st byte is 1 or '*'
2nd byte to byte 64 the ASCII of the SCPI command
on success the 1st byte returned will be the same value of the 1st byte that was sent.


codes supported by model: RC4DAT-6G-95:

1. Read 4 Channels Current Attenuation:

1st byte 18

The 64 returned array bytes will be as follows:
on success the 1st byte returned will be the same value of the 1st byte that was sent. 
1st byte 18
CHAN1Att = Byte2 + Byte3 / 4
CHAN2Att = Byte4 + Byte5 / 4
CHAN3Att = Byte6 + Byte7 / 4
CHAN4Att = Byte8 + Byte9 / 4

2. Set Channel Attenuation:
1st byte is 19
2nd byte is  the integer value of the required attenuation, for example for Attenuation of 55.25 the 2nd byte=55.
3rd byte to byte is the (RequiredAttenuation-2ndByte)*4. for example for Attenuation of 55.25 the 3rd byte=1.
4th byte is the Channel No
The 64 returned array bytes will be as follows:
on success the 1st byte returned will be the same value of the 1st byte that was sent. 





The 64 returned array bytes will be as follows:
on success the 1st byte returned will be the same value of the 1st byte that was sent.
for Models: RUDAT-3000-50 , RUDAT-3000-60 :
CurrentAttenuation = (2nd Byte)/2
for Models: RUDAT-6000-90", RUDAT-6000-60, RUDAT-6000-30 :
CurrentAttenuation = (2nd Byte) + (3rd Byte)/4

Example:

Compile:      
gcc -o mcl_RUDAT RUDAT.c libhid/*.c libusb/*.c


 
RUN :            
./mcl_RUDAT 



RS-232 - Programming:

Ceate a serial RS232 connection as follows:
Setup programming: Baud=9600, Parity=N, Data_Bits=8

Connect RS232 cable from 9 pin connector to the Computer RS232 port.
Connect to USB socket to PC or to 5Volt adaptor.

Comunication based on sending and recieving Ascii data over RS232 port.

1.  Getting the Device Model Name: Send the text "M"  
    The device will return [DeviceModelName].
       
2.  Getting the Device Serial Number: Send the text "S"  
    The device will return [DeviceSerialNumber].

3. Setting Attenuation: Send the Text as follows: "B[AttVal]E" For example: "B20.25E"
   The Device Will return "ACK"

4. Getting Current Attenuation: Send the Text "R"
   The device will return [Current Attenuation].
 





























