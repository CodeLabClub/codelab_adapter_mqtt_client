import json
import time
from codelab_adapter_mqtt_client import AdapterMQTTNode
from loguru import logger
from codelab_adapter_mqtt_client.topic import *


class EIMMQTTNode(AdapterMQTTNode):
    def __init__(self, *args, **kwargs):
        kwargs["logger"] = logger
        super().__init__(*args, **kwargs)
        self.EXTENSION_ID = "eim"

    def run(self):
        self.client.loop_start()
        i = 0
        while self._running:
            payload = self.message_template()
            payload["zmq_payload"]["content"] = i
            self.publish(payload)
            i += 1
            time.sleep(1)

if __name__ == "__main__":
    node = EIMMQTTNode()
    try:
        node.run()
    except KeyboardInterrupt:
        print('Control-C detected. See you soon.')
        node.clean_up()