from django.db import connection
from ..models import UserTotal
import time
def add_money(account_id,value):
    user_total = UserTotal.objects.get(account_id=account_id)
    time.sleep(3)
    user_total.value = user_total.value + value
    user_total.save()
#    cursor = connection.cursor()
