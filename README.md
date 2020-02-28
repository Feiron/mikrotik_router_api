# mikrotik_router_api

**Based on routeros_api**
- https://wiki.mikrotik.com/wiki/Manual:API
- https://github.com/socialwifi/RouterOS-api

**Settings**
- settings.ini
- user = Login
- password = Password

#router host
- host = 172.20.10.4
- port = 8728
- #default if you dont want to use it in command line
- device = ether10

**Unix** 
- ./api.py [enable|disable] [ether10]

**Windows**
- python api.py [enable|disable] [ether10]
