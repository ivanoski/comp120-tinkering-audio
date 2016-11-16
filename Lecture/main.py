import wave
import struct
import math
# Sound= wave.open("noise2.wav","r")
Sound_out= wave.open("noise3.wav","w")
FREQUENCY = 108
VOLUME = 0.5
SAMPLE_RATE = FREQUENCY*2
# Read_params = Sound.getparams()
# print Read_params
SAMPLE_LENGHT = 88200
SAMPLE_WIDTH = float(44100)
Sound_out.setparams((1,2,SAMPLE_WIDTH, SAMPLE_LENGHT, 'NONE', 'not compressed'))

# frames = []
# for i in xrange(0, nframes):
#     noiseFrames = Sound.readframes(1)
#     frameValue = struct.unpack("<h", noiseFrames)
#     frames.append(int(frameValue[0]))
# current_max = 0
# current_min = 0
# for volume in frames:
#     if volume > current_max:
#         current_max = volume
#     if volume < current_min:
#         current_min = volume


values = []

for j in range(0,SAMPLE_LENGHT):
    something = float(j / SAMPLE_WIDTH)
    value = math.sin( 2.0 * math.pi * FREQUENCY * something *(VOLUME * 3000))
    value2 = value * 5000
    packaged_value = struct.pack("<h", value2)

    #for k in xrange(0,1):
    values.append(packaged_value)

value_str = "".join(values)

Sound_out.writeframes(value_str)
Sound_out.close()