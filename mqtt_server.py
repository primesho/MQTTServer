import paho.mqtt.client as mqtt

host = '127.0.0.1'
port = 1883
topic = 'tp1/sub1'
topic2 = 'tp1/sub2'


def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))
    # topicを複数登録してみた
    client.subscribe(topic)
    client.subscribe(topic2)


def on_message(client, userdata, msg):
    # topic QOS payloadを取得
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


if __name__ == '__main__':
    # Publisherと同様に v3.1.1を利用
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host, port=port, keepalive=60)
    # 待ち受け状態にする
    client.loop_forever()