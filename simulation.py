import time
import random

seed = random.randint(0, 1000000000)

print("Application start")
# time.sleep(600) # Do some processing, like a long simulation
start = time.time()
while (time.time() - start < 610):
    time.sleep(0.0001)


with open(f"results_{seed}", 'w') as result_file:
    result_file.write("Some data\n")

print("Application end")
