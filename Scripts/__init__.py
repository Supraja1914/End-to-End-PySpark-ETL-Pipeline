import paramiko

host, port, user, pwd = "test.rebex.net", 22, "suprajabhogineni", "asj@1419"
transport = paramiko.Transport((host, port))
transport.connect(username=user, password=pwd)
print("✅ Connection successful!")
transport.close()