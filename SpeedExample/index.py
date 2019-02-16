speed = 1

def motorPower():
    return speed * 2

while (True):
    if(speed < 10):
        speed = motorPower()
    else: speed -= 0.1*(speed-10)
    print(speed)