import json
import time
from codelab_adapter_mqtt_client import AdapterMQTTNode
from codelab_adapter_mqtt_client.topic import *
from loguru import logger


class HelloWorldMQTTNode(AdapterMQTTNode):
    def __init__(self, *args, **kwargs):
        kwargs["logger"] = logger
        kwargs["external_message_processor"] = self.external_message_processor
        super().__init__(*args, **kwargs)
        self.EXTENSION_ID = "eim"

    def external_message_processor(self, topic, payload):
        self.logger.debug(payload)
        # 反转
        content = payload["zmq_payload"]["content"]
        if type(content) == str:
            content_send_to_scratch = content[::-1]
            payload["zmq_payload"]["content"] = content_send_to_scratch
            self.publish(payload)

if __name__ == "__main__":
    node = HelloWorldMQTTNode()
    try:
        node.client.on_message = node.mqtt_on_message
        node.run()
    except KeyboardInterrupt:
        print('Control-C detected. See you soon.')
        node.clean_up()