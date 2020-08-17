# HTTP to Rabbit

This is a generic RabbitMQ publisher taking HTTP requests.

## Env Vars

| Name | Description |
| :--- | :--- |
| `APP_HOST` | Required string |
| `APP_PORT` | Required string |
| `APP_DEBUG` | 0 or 1, enabling will print debug logs |
| `AMQP_CONN_STRING` | Required string |
| `AMQP_QUEUE` | Required string, also known as routing key |
