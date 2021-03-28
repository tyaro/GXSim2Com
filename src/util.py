import psutil
def getGXSimPortNum():
    for p in psutil.process_iter(attrs=["pid", "name"]):
        if p.info["name"] == "QnUDSimRun2.exe" or p.info["name"] == "QnXSimRun2.exe":
            pid_num = p.info["pid"]
            break
    port_num = [conn.laddr.port for conn in psutil.net_connections() if conn.pid == pid_num]
    return port_num[0]