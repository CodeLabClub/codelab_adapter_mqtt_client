# codelab_adapter_mqtt_client
MQTT Client of [CodeLab Adapter](https://adapter.codelab.club/) v2.

# Install
```bash
# Python >= 3.6
pip install codelab_adapter_mqtt_client 
```

# Usage
```python
from codelab_adapter_mqtt_client import AdapterMQTTNode
```

# example
[monitor.py](https://github.com/Scratch3Lab/codelab_adapter_mqtt_client/blob/master/codelab_adapter_mqtt_client/tools/monitor.py)

# tools(for debugging)
```
codelab-mqtt-monitor # subscribes to all messages and print both topic and payload.
codelab-mqtt-trigger # pub the message in json file(`/tmp/message.json`).
```

`/tmp/message.json`:

```json
{
    "zmq_topic": "core/extensions/operate",
    "zmq_payload": { "content": "start", "extension_id": "extension_eim" }
}
```