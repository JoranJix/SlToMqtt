# SlToMqtt
A small python server to send data from SecondLife to MQTT

# Installation and Autostart

Copy the pythonfile to a directory you have access to.

Create a file:

        sudo nano /etc/systemd/system/mqtt_http_server.service

Paste 

        [Unit]
        Description=MQTT HTTP Server
        After=network.target
        
        [Service]
        ExecStart=/usr/bin/python3 /path/to/your/python_script.py
        WorkingDirectory=/path/to/your/script_directory
        Restart=always
        User=your_username
        Group=your_groupname
        
        [Install]
        WantedBy=multi-user.target
