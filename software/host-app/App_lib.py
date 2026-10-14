import pickle

uart_cfg_file = 'uart.cfg'
# 更新系统串口
def Update_Serial(ser, cbPort):
    cbPort.clear()
    ser.get_ports()
    for each in ser.ports:
        cbPort.addItem(each)

# 给定显示内容设置comboBox Index
def setCbIndex(text, cb):
    if cb.findText(text) == -1:
        cb.addItem(text)     
    for n in range(cb.count()):
        if cb.itemText(n) == text:
            cb.setCurrentIndex(n)

# 写串口配置参数到文件中 [port,baudrate,...]
def Save_Uart_Cfg(uart_cfg):
    with open(uart_cfg_file, 'wb') as pf:
        pickle.dump(uart_cfg, pf)

# 从配置文件读入上次uart参数配置
def Load_Uart_Cfg(cbUartPort):
    try:
        with open(uart_cfg_file, 'rb') as pf:
            uart_cfg = pickle.load(pf)
            print(uart_cfg)
            setCbIndex(uart_cfg[0], cbUartPort)
            if cbUartPort.findText(uart_cfg[1]) == -1: #系统无此串口
                setCbIndex("", cbUartPort)
            else:
                setCbIndex(uart_cfg[1], cbUartPort)
    except Exception as e:
        pass
