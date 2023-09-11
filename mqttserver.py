import http.server
import socketserver
import paho.mqtt.client as mqtt

# MQTT-Server-Konfiguration
mqtt_server = "localhost"  # Der MQTT-Server-Hostname oder die IP-Adresse
mqtt_port = 1883  # Der MQTT-Server-Port

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/send_message"):
            query = self.path.split("?")[1]
            params = dict(param.split("=") for param in query.split("&"))
            if "topic" in params and "message" in params:
                mqtt_topic = params["topic"]
                mqtt_message = params["message"]
                client = mqtt.Client()
                client.connect(mqtt_server, mqtt_port)
                client.publish(mqtt_topic, mqtt_message)
                client.disconnect()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(f"Message '{mqtt_message}' published to topic '{mqtt_topic}'".encode())
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write("Bad Request: 'topic' and 'message' parameters are required".encode())
        else:
            super().do_GET()

# HTTP-Server erstellen
port = 85
httpd = socketserver.TCPServer(("", port), RequestHandler)

print(f"HTTP-Server gestartet auf Port {port}")
httpd.serve_forever()
