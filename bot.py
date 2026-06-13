def handle_bot(message):
    message = message.strip()

    if message == "/start":
        return """سلام بفرمایید

1️⃣ آیدی مالک
2️⃣ آیدی لیدر
3️⃣ ثبت سفارش
4️⃣ ثبت تبلیغ
5️⃣ ثبت نام در کلن
"""

    elif message == "آیدی مالک":
        return "@N8Abmin"

    elif message == "آیدی لیدر":
        return "لیدر خوابه 😴"

    elif message == "ثبت سفارش":
        return "به این پیام دهید:\n@N8Abmin"

    elif message == "ثبت تبلیغ":
        return "برای تبلیغات به آیدی زیر پیام دهید\n@N8Abmin"

    elif message == "ثبت نام در کلن":
        return "برای ثبت نام 👇\n@N8Abmin"

    else:
        return "دستور نامعتبر است."
