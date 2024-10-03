import re
from rest_framework import serializers

def validate_phone_number(value):
    pattern = r'^998[0-9]{9}$'
    if not re.match(pattern, value):
        raise serializers.ValidationError("Telefon raqam noto'g'ri formatda. Raqam 998 bilan boshlanishi va keyin 9 xonali bo'lishi kerak.")
    return value


def validate_email(value):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
        raise serializers.ValidationError("Elektron pochta noto'g'ri formatda.")
    return value
