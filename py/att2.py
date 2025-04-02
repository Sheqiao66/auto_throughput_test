import clr
# import sys
# from System import String

# 指定 DLL 的路径
dll_path = r'C:\Windows\SysWOW64\mcl_RUDAT64.dll'

# 加载 .NET DLL
clr.AddReference(dll_path)
# print("DLL 加载成功")

# 导入命名空间中的 USB_RUDAT 类
from mcl_RUDAT64 import USB_RUDAT
# print("成功导入 USB_RUDAT 类")

# 创建 USB_RUDAT 对象实例
device = USB_RUDAT()
print("USB_RUDAT 对象创建成功，类型：", type(device))

# 使用 StrongBox 创建一个 String 类型的对象，用于接收序列号列表
sn_list = "123"  # 尝试直接传 String
result = device.Get_Available_SN_List(sn_list)
print("返回值:", result)
print("获取的序列号列表:", sn_list)

#Disconnect from Attenuator  RC4DAT-6G-95
device.Disconnect()

#Get USB Address
device.Get_Address()

#Get USB Connection Status
device.GetUSBConnectionStatus()

#Set Attenuation - All Channels
Att=15
device.SetChannelsAtt(Att, 1,1,1,1)


result = device.Get_Available_SN_List("1")
print("返回值:", result)
