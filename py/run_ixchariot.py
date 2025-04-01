import os


def run_ixchariot(runpath, ip_send, ip_recv, tp_count, end_time, protocol_type, bool_tx, bool_rx, bool_trx):
    runpath = 'cd/d ' + runpath + ' && '
    tool = 'IxChariotCommand_mp.exe'

    command_tx = tool + ' ' + ip_send + ' ' + ip_recv + ' ' + str(0) + ' ' + str(2*tp_count) + ' ' + str(end_time) + ' ' + str(
        protocol_type)
    command_rx = tool + ' ' + ip_send + ' ' + ip_recv + ' ' + str(2*tp_count) + ' ' + str(0) + ' ' + str(end_time) + ' ' + str(
        protocol_type)
    command_trx = tool + ' ' + ip_send + ' ' + ip_recv + ' ' + str(tp_count) + ' ' + str(tp_count) + ' ' + str(end_time) + ' ' + str(
        protocol_type)

    def get_throughput_average_speed(command):
        re = os.popen(runpath + command)
        print(command)
        text = re.readlines()
        strtext = ''.join(text)

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
        else:
            print("未找到起始或结束字符串。")
        return result_dict.get('throughput_average_speed', 0)

    speed_tx = get_throughput_average_speed(command_tx) if bool_tx else 0
    speed_rx = get_throughput_average_speed(command_rx) if bool_rx else 0
    speed_trx = get_throughput_average_speed(command_trx) if bool_trx else 0

    return [speed_tx, speed_rx, speed_trx]
    