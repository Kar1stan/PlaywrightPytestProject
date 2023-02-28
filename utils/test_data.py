
import random
import string


class Data:

    signup_name = ''.join(random.sample(string.ascii_lowercase, 8))
    signup_email = ''.join(random.sample(string.ascii_lowercase, 8)) + "@gmail.com"
    signup_password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8))
    zipcode = str(random.randint(0, 9000))

    login_email = "foloxov@gmail.com"
    login_password = "XYa86BTWmJi6n4Z"
    incorrect_login_email = "bulbozvon@gmail.com"
    incorrect_login_password = "5555"
    search_product = "men"
