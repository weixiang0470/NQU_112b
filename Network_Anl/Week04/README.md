# **DHCP**
- 自動分配，手動分配，動態分配（有時限）
- Steps
    - Server : 67/udp , Client : 68/udp
    1. DHCP Discover broadcast (client to server)
        - src:`0.0.0.0`,des:`255.255.255.255`
        - Cause device don't know the address of DHCP server
    2. DHCP OFFER broadcast (S to C)
    3. DHCP REQUEST broadcast (C to S)
    4. DHCP ACK broadcast (S to C)
- Standard : `RFC 2131` , `RFC 2939`

# **Extra**
- Screen Task : Screen sharing through network