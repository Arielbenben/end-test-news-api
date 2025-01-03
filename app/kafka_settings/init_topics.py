import os
from dotenv import load_dotenv
from kafka import KafkaAdminClient
from kafka.admin import NewTopic


load_dotenv(verbose=True)


news_api_topic = os.environ['NEWS_API_TOPIC']


def init_topics():
    admin_client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
    topic_list = [
        NewTopic(
            name=news_api_topic,
            num_partitions=int(os.environ["NUM_PARTITIONS"]),
            replication_factor=int(os.environ["NUM_REPLICATION"])
        )
    ]

    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print("Topics created successfully!")
    except Exception as e:
        print(f"Error creating topics: {e}")
    finally:
        admin_client.close()
