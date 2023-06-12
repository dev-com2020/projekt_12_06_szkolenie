import time

print("Czas: 12:00")
time.sleep(2)
print("Czas: 13:00")
t = time.localtime()
print("Aktualny Czas: %d:%d" % (t.tm_hour, t.tm_min))
print(time.strftime("Aktualny Czas: " + "%H:%M"))
print(time.strftime("Aktualny Czas: " + "%H:%M:%S"))
print(time.strftime("Aktualny Czas: " + "%H:%M:%S" + " data: %d.%m.%Y"))

CZAS = "01:00"
