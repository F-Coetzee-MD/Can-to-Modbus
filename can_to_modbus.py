import json
from time import sleep
from threading import Thread

# import settings

# define global variables
buffer = [];
t1_healthy = False
t2_healthy = False

# create thread that received usb can messages and stores it in buffer
def read_usb():
  while True:
    t1_healthy = True
    print("cool")

# create thread that takes oldest item in the buffer, converts it to modbus and sends it to the drive
def write_to_plc():
  while len(buffer) > 1:
    t2_healthy = True
    print("dude")

# create a function that checks the health of the threads above
def check_threads_health():
  while True:
    t1_healthy = False;
    t2_healthy = False;
    sleep(1)

    if not t1_healthy:
      print("can receiver failed")
      break

    if not t2_healthy:
      print("modbus client failed")
      break


# initiate application here
read_usb_thread = Thread(target = read_usb)
write_to_plc_thread = Thread(target = write_to_plc)

read_usb_thread.start();
write_to_plc_thread.start();

# detach threads 
read_usb_thread.daemon = True
write_to_plc_thread.daemon = True

check_threads_health(
  read_usb_thread,
  write_to_plc_thread
)