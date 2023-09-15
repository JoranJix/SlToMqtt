# SlToMqtt
A small python server to send data from SecondLife to MQTT
Your brokers IP!
This is basicly a POC that it is possible to transmit data to MQTT.
# Usage

You could use this to feed databases or control you IOT from within secondlife.
Make your own SecurityOrb and make it turn off or on a light any time someone enters your parcel.
There are countless ideas.

# Installation and Autostart

Copy the pythonfile to a directory you have access to.

Create a file:

        sudo nano /etc/systemd/system/mqtt_http_server.service

Paste: 

        [Unit]
        Description=MQTT HTTP Server
        After=network.target
        
        [Service]
        ExecStart=/usr/bin/python3 /path/to/your/mqttserver.py
        WorkingDirectory=/path/to/your/script_directory
        Restart=always
        User=your_username
        Group=your_groupname
        
        [Install]
        WantedBy=multi-user.target

Run:

        sudo systemctl daemon-reload
        sudo systemctl enable mqtt_http_server.service

The server will be started every time you start your system. You can run or restart the server manually

        sudo systemctl start mqtt_http_server.service
        sudo systemctl status mqtt_http_server.service
        sudo systemctl stop mqtt_http_server.service

To test your server you can run:

        curl "http://localhost:85/send_message?message=Hello%2C%20MQTT%21"

You can call the lsl script from any other script by llMessageLinked(); on channel 255;

        llMessageLinked(LINK_SET,255,"Hello MQTT!","/test/topic");
