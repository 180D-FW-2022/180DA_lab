from subprocess import run
from time import sleep

for i in range(10):
  print("hellooooooo test")
  run('vcgencmd display_power 0', shell=True)
  sleep(1)
  #run('xrandr --output HDMI-1 --auto', shell=True)
  run('vcgencmd display_power 1', shell=True)
  sleep(1)
