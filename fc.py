#!/usr/bin/env python

import time

import pigpio

GPIO=4

square = []

#                          ON       OFF    MICROS
square.append(pigpio.pulse(1<<GPIO, 0,       14))
square.append(pigpio.pulse(0,       1<<GPIO, 14))#delay in microseconds
#13us for getting 38khz
#14us for 36khz
pi = pigpio.pi()  #gpioInitialse
# connect to local Pi                                
#initialize the pi connection

pi.set_mode(GPIO, pigpio.OUTPUT)#gpioSetMode
#set a gpio mode

pi.wave_add_generic(square)#gpioWaveAddGeneric
#adds a series of of pulses to the waveform

wid = pi.wave_create()#gpioWaveCreate
#creates a waveform from the added data

if wid >= 0:
   pi.wave_send_repeat(wid)#gpioWaveChain
   #transmits the waveform repeatedly
   time.sleep(60)
   pi.wave_tx_stop()#gpioWaveTxStop
   #aborts the current waveform
   pi.wave_delete(wid)#gpioWaveDelete
   #deletes the waveform

pi.stop()#gpioTerminate
#stop the pi connection
