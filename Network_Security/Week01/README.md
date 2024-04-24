# **Research ways**
- IEEE,ACM
    - doi (unique code)

- Letter
    - new topic, important topic
    - 4 weeks (reply)

- Magazine
    - For outsider

- Transactions
    - More complicate, more formular, more theory

- Top & Conferece
    - Info con(5k->1k), Global, NDSS

- sci-hub
    - paste doi code to search 

- topic arxiv
    - open db

# **DHCP & DDoS**

- DHCP attack
    - VM with bridge mode, DHCP server, VM and others target devices in same network
    - Bridge mode sees VM as a normal host from outsider, VM will have it's own IP address different from HOST
    - When target device wants to get IP address from DHCP server, it will get from the nearest DHCP server
    - So the target device will get from the VM cause it is in the same network(more near), then it will access to Internet through VM, but VM does not act as router so the target device won't able to access to Internet

- DNS
    - 有送有回,封包解析度(0~255),DDoS
    - DNS server is a server that if you request then it will reply
    - We can send DNS request (packet) to DNS servers and acting as the target device(IP,MAC address)
    - After DNS server get the DNS request it will reply to the target device cause it see the IP&MAC address inside the packet and send to it
    - target device will get the packets from DNS servers as much as we sent

- CDN
    - Put db to others local area network, so that when client request data will able to get it faster, also for load balancing(all client don't have get data from root server)

- online ipscanf tools
    - https://search.censys.io