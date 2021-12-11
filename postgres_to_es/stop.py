from consumer import ETLConsumer
from producer import ETLProducer


if __name__ == '__main__':
    ETLProducer().stop()
    ETLConsumer().stop()
