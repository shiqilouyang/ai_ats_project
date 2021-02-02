import time
from kafka import KafkaProducer
import json

# 实例化一个KafkaProducer示例，用于向Kafka投递消息
producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
     bootstrap_servers='10.31.210.18:9093')


def send_message_one():

    import time
    time.sleep(1)
    a = time.time()
    time.sleep(1)
    s = str(a)[0:10]
    data = {"msgId":"3a9cab70bb1db8f70e5621f5aaa8aada",
            "batchSize":1,"objectType":"LO_MAP",
            "action":"UPDATE",
            "data":[{
                "loMapName":"向量章节测试",
                "loMapCode":"test26_pre_map",
                "loMapLearnType":"loMap",
                "loMapType":"PRE_MAP",
                "loMap":{"a":["b"],"b":["c"],"c":[]
                         },"utime":s}],
            "totalSize":1,
            "traceId":s}  # traceId 相同代表 校验不过 不能上传图服务
    print(data)
    producer.send('ALE_CMS_LO_MAP', data)
    time.sleep(3)

def send_message_two():

    import time
    time.sleep(1)
    a = time.time()
    time.sleep(1)
    s = str(a)[0:10]
    data = {"msgId":"7c967170d23fd6b95de355ca0e5d3785",
            "batchSize":1,"objectType":"COURSE_LO_MAP",
            "action":"UPDATE","data":[{
            "courseId":9908,"loMapCode":"test25_pre_map",
            "atlasCode":"test25","loMapLearnType":"loMap",
            "loMapType":"PRE_MAP","tags":{"loScene":"RECOMMEND"},"utime":s}]}

    print(data)
    producer.send('ALE_CMS_COURSE_LO_MAP', data)
    time.sleep(3)

def get_message_one():
    from kafka import KafkaConsumer
    # topic
    consumer = KafkaConsumer('ALE_CMS_LO_MAP', bootstrap_servers=['10.30.31.88:9093,10.30.31.89:9093,10.30.31.90:9093'])
    while 1:
        for msg in consumer:
            print(msg.value)
            recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
            print(recv)


def get_message_two():
    from kafka import KafkaConsumer
    # topic
    consumer = KafkaConsumer('ALE_CMS_COURSE_LO_MAP', bootstrap_servers=['10.30.31.88:9093,10.30.31.89:9093,10.30.31.90:9093'])
    while 1:
        for msg in consumer:
            print(msg.value)
            recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
            print(recv)

# get_message_one()
# get_message_two()