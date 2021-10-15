# RabbitMQ Example in Python

1. Start RabbitMQ Service `docker run -d --hostname my-rabbit -p 15672:15672 -p 5672:5672 --name rabbit-server -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-management`
2. check local management at http://localhost:15672 with `user` and `password`
3. start `telegram_bot.py` as receiver
3. start `sender.py` as sender


## Further reading
* What is an exchange? What are routing keys and bindings? How are exchanges and queues associated with each other? When should I use them and how? This article explains the different types of exchanges in RabbitMQ and scenarios for how to use them.
  * https://www.cloudamqp.com/blog/part4-rabbitmq-for-beginners-exchanges-routing-keys-bindings.html
* https://betterprogramming.pub/introduction-to-message-queue-with-rabbitmq-python-639e397cb668