import time
import random

seed = random.randint(0, 1000000000)

print("Application start")
time.sleep(60) # Do some processing, like a long simulation

with open(f"results_{seed}", 'w') as result_file:
    result_file.write("Some data")

print("Application end")
