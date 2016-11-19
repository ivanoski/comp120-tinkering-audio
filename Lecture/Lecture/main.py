import wave
import struct
import math
# Sound= wave.open("noise2.wav","r")
Sound_out= wave.open("noise3.wav","w")
VOLUME = 20000
# Read_params = Sound.getparams()
# print Read_params
SAMPLE_LENGTH = 88200
SAMPLE_WIDTH = float(44100)
Sound_out.setparams((1, 2, SAMPLE_WIDTH, SAMPLE_LENGTH, 'NONE', 'not compressed'))


# This function adjusts the volume of the tone
def getVolume(sound,volume):
    newSound = volume * sound * 40000
    return newSound

# This function creates an average of two tones and returns the value
def merge2Waves(sound1, sound2):
    mergedSound = ((sound1 + sound2)/2)
    return mergedSound

# This function creates a pure tone
def pureTone(frequency, time):
    tone = math.sin(2 * math.pi * frequency * time)
    return tone





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

for j in range(0, SAMPLE_LENGTH):

    # This is the time in seconds
    TIME = float(j / SAMPLE_WIDTH)

    # Here two tones are created using a given frequency
    tone1 = pureTone(600, TIME)
    tone2 = pureTone(150, TIME)


    # Here we merge two tones to created a new tone
    tone = merge2Waves(tone1, tone2)

    # Here we adjust the volume, using a value from 0 to 1
    tone = getVolume(tone, 0.5)
    packaged_value = struct.pack("<h", tone)
    values.append(packaged_value)

value_str = "".join(values)

Sound_out.writeframes(value_str)
Sound_out.close()