import string
password = input()
errors = []
if len(password) != 8:
    errors.append("Длина пароля не равна 8")
if password == password.lower():
    errors.append("В пароле отсутствуют заглавные буквы")
if password == password.upper():
    errors.append("В пароле отсутствуют строчные буквы")
if not any(symbol.isdigit() for symbol in password):
    errors.append("В пароле отсутствуют цифры")
specials = "*-#"
if not any(symbol in specials for symbol in password):
    errors.append("В пароле отсутствуют специальные символы")
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + specials
if not all(symbol in allowed for symbol in password):
    errors.append("В пароле используются непредусмотренные символы")
if not errors:
    print("Надежный пароль")
else:
    for err in errors:
        print(err)
