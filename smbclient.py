from impacket.smbconnection import SMBConnection


def runNoPassWordEnumerationShare(target_ip: str):
    conn = SMBConnection(target_ip, target_ip)
    conn.login("", "")  # No credentials so void

    shares = conn.listShares()

    for share in shares:
        print(share['shi1_netname'][:-1])  # Show the name

    conn.close()
