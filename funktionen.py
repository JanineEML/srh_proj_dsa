import random

def wuerfelprobe(talent, wert):
    w1 = random.randint(1, 20)
    w2 = random.randint(1, 20)
    w3 = random.randint(1, 20)
    return f"Probe auf {talent} mit Wert {wert}: {w1}, {w2}, {w3}"
