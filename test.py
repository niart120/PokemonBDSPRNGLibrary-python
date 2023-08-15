import os
import sys
import random

from bdsprnglib.restoreseed import PlayerBlinkInverter
from bdsprnglib.starterrng import MunchlaxInverter
from bdsprnglib.restoreseedmodule import PlayerBlink, blink_player
from bdsprnglib.rng import Xorshift

def playerblinkinvertertest():
    while True:
        state = [random.getrandbits(32) for _ in range(4)]
        inverter = PlayerBlinkInverter()
        rand = Xorshift(*state)

        restored = None
        while True:
            blink = blink_player(rand)
            inverter.add_blink(blink)

            print("- " if blink == PlayerBlink.Nothing else "s " if blink == PlayerBlink.Single else "d ", end="")

            restored = inverter.try_restore_state()
            if restored is not None:
                break
        print()
        print(f"expected: {state}")
        print(f"restored: {restored.get_state()}")
        print("Successfully restored." if state == restored.get_state() else "Failed...")

def munchlaxinvertertest():
    while True:
        state = [random.getrandbits(32) for _ in range(4)]
        inverter = MunchlaxInverter()
        rand = Xorshift(*state)

        restored = None

        while True:
            interval = rand.range_float(3.0, 12.0) + 0.285 + randomize()
            inverter.add_interval(interval)

            restored = inverter.try_restore_state()
            if restored is not None:
                break
        
        print()

        print(f"expected: {state}")
        print(f"restored: {restored.get_state()}")
        print("Successfully restored." if state == restored.get_state() else "Failed...")
        print(f"blink: {inverter.blinkcount} times")

def randomize():
    return (random.random()-0.5) * 0.07

if __name__ == "__main__":
    playerblinkinvertertest()
    #munchlaxinvertertest()