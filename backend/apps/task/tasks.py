from celery import shared_task
from apps.account.models import PasswordResetToken

@shared_task
def delete_password_reset_token(object_id):
    try:
        token = PasswordResetToken.objects.get(pk=object_id)
        token.delete()
    except PasswordResetToken.DoesNotExist:
        pass  # 如果令牌不存在，则无需删除
