'''主要配置了 Celery 的一些关键设置，包括消息代理、结果存储后端、时区、任务超时时间和重试次数等。'''
# Celery settings
CELERY_BROKER_URL = "amqp://localhost:5672//"  # RabbitMQ
CELERY_RESULT_BACKEND = "redis://localhost:9527/0"

CELERY_TIMEZONE = "Asia/Shanghai"

CELERY_TASK_SOFT_TIME_LIMIT = 20
CELERY_TASK_TIME_LIMIT = 15 * 60
CELERY_TASK_MAX_RETRIES = 3
