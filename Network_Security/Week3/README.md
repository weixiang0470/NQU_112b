# **Steps of attack**
1. Search IP
    - Public
    - Private
2. Server or Service
    - ex: http
3. Choose "Attack Tools"
    - ex: "ab", in time limit how many people and connections
4. Hide in the Internet
    - MultiHop
        1. Australia -> USA -> UK -> ...
        2. Computer A -> Computer B -> ...
5. Attack

# **Network Security**
1. Confidentiality : 資料不會被人發現
2. Integrity : 資料不會被竄改
    - "Hash" : Sha256, Sha128, MD5, ...
3. Availability : 服務不中斷，通道是通順的，。。。
4. Authentication : 可追溯到聲明者的特性
5. Accountability : 可追溯到設備的資訊

# **Information Collection**
- User Information
- Network Information
    - IP, DNS, domain name...
    - DNS Lookup, whoami, `dig`
    - DNS record types
        - A : Ipv4 address record
        - NS : name server record
        - MX : Mail Exchange Record
        - SOA : 所有的DNS 區域都需要一個 SOA 紀錄才能符合 IETF 標準
        - CNAME : 別名,ex: `wwww.nqu.edu.tw`,`ftp.nqu.edu.tw`,`www.csie.nqu.edu.tw`

# **ARP attack**
- Broadcast ARP packet, to get **IP to MAC**, **Layer 2**
- Possible ways
    1. When the device(switch) just open, ARP table is empty, keep sending ARP packet (victim's IP is hacker's MAC) to switch 
    2. send 9999999 ARP packet to full ARP table and make target device(switch) renew ARP table
    3. Use DDoS attack to shutdown and restart device/server, will have new ARP empty table

# **Hide in the internet**
- IP Address
    - IP spoofing
- MAC Address:
    - 前三碼 : OUI （Organization Unique Identifier）
    - 後三碼 : NIC
    - MAC spoofing

# **NAT**
- Static
    - 1 to 1
    - `192.168.1.60` -> `172.20.10.6`
- Dynamic
    - range to range
    - `192.168.1.2~253` -> `172.20.10.2~253`, maybe randomly 
- Port address translation, PAT
    - Use same ip address but different port number
    - `192.168.1.5:2020`->`172.20.10.10:8018`
    - `192.168.1.5:4343`->`172.20.10.10:8188`

# **Tools**
1. termshark
    - GUI wireshark at terminal, will extract `.pcap` file at terminal
2. 10 Minute email