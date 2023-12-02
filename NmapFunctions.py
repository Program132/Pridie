def basicNmapScan(sc):
    TargetIP = str(input("Enter the target IP : "))
    TargetPort = str(input("Enter the port(s) : "))
    Speed = str(input("Speed of the scan (1-5) : "))

    if Speed != "1" and Speed != "2" and Speed != "3" and Speed != "4" and Speed != "5":
        print("You did not give a valid speed, the default will be 3.")
        Speed = 3

    print(f"Running scan on {TargetIP} {TargetPort}")
    sc.scan(TargetIP, TargetPort, arguments=f"-T{Speed}")
    result = sc[TargetIP]['tcp']
    print("Opened ports : ")
    for i in result.keys():
        print(f"- {i}, {result[i]['name']}")
