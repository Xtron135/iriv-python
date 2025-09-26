import paho.mqtt.client as mqtt

# MQTT Broker Settings
BROKER = "192.168.1.XX"  # Replace with your MQTT broker's IP/ IRIV PiControll IP Address
PORT = 1883

# Topics to subscribe
TOPICS = [("sensor/temperature", 0), ("sensor/humidity", 0)]

# Callback when connected to broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    # Subscribe to multiple topics
    client.subscribe(TOPICS)

# Callback when message is received
def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()

    if topic == "sensor/temperature":
        print(f"Temperature: {payload} °C")
    elif topic == "sensor/humidity":
        print(f"Humidity: {payload} %")
    else:
        print(f"{topic}: {payload}")

# Create MQTT client and assign callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect and loop forever
client.connect(BROKER, PORT, 60)
client.loop_forever()
