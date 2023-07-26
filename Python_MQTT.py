import paho.mqtt.publish as publish
import json

# MQTT broker information
broker_address = "broker.hivemq.com"                            # Broker domain
broker_port = 1883                                              # Port number
topic = "thingsboard/device1"                                   # Replace with your desired topic

msg = {
        "Temperature": 25,
        "Humidity":50
    }
jsonmessage = json.dumps(msg)                                   # Change message to JSON
print(jsonmessage)
publish.single(topic, jsonmessage, hostname=broker_address, port=broker_port)   # Send the jsonmessage to public broker