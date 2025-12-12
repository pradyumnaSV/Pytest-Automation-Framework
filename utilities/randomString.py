# import random
# import string

# def random_string_generator(size = 5, chars = string.ascii_lowercase+string.digits):

#     return ''.join(random.choice(chars) for x in range(size))


# print(random_string_generator())


# ----------------------------
# using time stamp
# import time

# def generate_timestamp_email():
#     # time.time() gives seconds since 1970. We convert to int to remove decimals.
#     timestamp = int(time.time()) 
#     return f"test_{timestamp}@gmail.com"

# print(generate_timestamp_email())
# # Output example: test_1715629482@gmail.com


# ---------------
# using test and random number
# import random
# import string

# def generate_test_email():
#     # This generates 5 random numbers
#     random_nums = ''.join(random.choices(string.digits, k=5))
#     return f"test_{random_nums}@gmail.com"

# print(generate_test_email())
# # Output example: test_82931@gmail.com

# --------------------


from faker import Faker

def faker_generate_test_email():
    fake = Faker()

    return fake.email()