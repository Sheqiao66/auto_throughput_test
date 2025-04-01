
import os

def run_ixchariot(runpath,ip_send, ip_recv, send_count, recv_count, end_time, protocol_type):
    runpath = 'cd/d '+runpath+' && '
    tool = 'IxChariotCommand_mp.exe'
    command = tool + ' ' + ip_send + ' ' + ip_recv + ' ' + str(send_count) + ' ' + str(recv_count) + ' ' + str(end_time) + ' ' + str(protocol_type)

    re = os.popen(runpath + command)
    print(command)
    # sleep(15)

    text = re.readlines()
    strtext = ''.join(text)
    print(strtext)

    # 按行分割字符串
    lines = strtext.strip().split('\n')

    # 找到起始和结束行的索引
    start_index = next((i for i, line in enumerate(lines) if 't_ixchariot_result' in line), None)
    end_index = next((i for i, line in enumerate(lines) if 't_ixchariot_finish' in line), None)

    result_dict = {}
    if start_index is not None and end_index is not None:
        # 截取有效部分
        useful_lines = lines[start_index:end_index + 1]
        for line in useful_lines:
            line = line.strip()
            if ':' in line:
                key, value = line.split(': ')
                try:
                    value = float(value)
                except ValueError:
                    pass
                result_dict[key] = value

        # 可以通过键来访问值
    else:
        print("未找到起始或结束字符串。")

    output_list = [
        result_dict.get('throughput_average_speed'),
        result_dict.get('throughput_average_speed_send'),
        result_dict.get('throughput_average_speed_recv')
    ]
    return output_list