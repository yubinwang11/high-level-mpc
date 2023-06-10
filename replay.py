# -*- coding: utf-8 -*-

import time
import numpy as np
import carla

def main():

        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)

        client.replay_file("/home/yubinwang/carla_saved/recording01.log", 0, 0, 0)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(' - Exited by user.')