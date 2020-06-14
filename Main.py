from Client import Client
import time

client1 = Client()

#client1.kill()

client2 = Client()
client1.sendmsg("Hello")
client2.sendmsg("World")
client1.sendmsg("ELO")

client2.kill()
client1.kill()