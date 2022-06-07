# Importing Libraries
import serial
import time
import base64
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    num = input("numara giriniz: ") # Taking input from user
    value = write_read(num)
    print("kartın içindeki şifrelenmemiş veri: ",value)
    s = "Ahmet-Ali-Suzen"
    b = s.encode("UTF-8")
    e = base64.b32encode(b)
    s1 = e.decode("UTF-8")
    print("şifrelenmiş veri: ", s1)
    b1 = s1.encode("UTF-8")
    d = base64.b32decode(b1)
    s2 = d.decode("UTF-8")
    print("şifresi çözülmüş veri: ",s2)