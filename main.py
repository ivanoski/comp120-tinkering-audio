import wave
import struct
import math
import winsound
Sound= wave.open("noise2.wav","r")
Sound_out= wave.open("noise3.wav","w")
Final_round = wave.open("final_round.wav","r")
# Final_round_offset = wave.open("final_round_offset.ogg","w")
# Final_round_echo = wave.open("final_round_echo.ogg","w")
# Read_params = Sound.getparams()
# print Read_params
SAMPLE_LENGTH = 88200
SAMPLE_WIDTH = float(44100)
Sound_out.setparams((1, 2, SAMPLE_WIDTH, SAMPLE_LENGTH, 'NONE', 'not compressed'))

print Final_round.getparams()

# This function adjusts the volume of the tone
def listValues(sound_file):
    valueList = []
    for i in xrange(0, getLength(sound_file)):
        noiseFrames = sound_file.readframes(1)
        value = struct.unpack("<h", noiseFrames)
        valueList.append(int(value[0]))
    return valueList
def getLength(sound):
    sampleLenght = sound.getnframes()
    return sampleLenght
def getSampleValueAt(sound,sample_number):
    for i in xrange(0, sound.__len__()):
        if i+1 == sample_number:
            return sound[i]
def setSampleValueAt(sound,sample_number,value):
    for i in xrange(0,sound.__len__()):
        if i+1 == sample_number:
            sound[i] = value




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

def addSoundInto(sound1,sound2):
    for sampleNmr in range(0,getLength(Final_round)):
        sample1 = getSampleValueAt(sound1,sampleNmr)
        sample2 = getSampleValueAt(sound2,sampleNmr)
        sample3 = sample1+sample2
        setSampleValueAt(sound2,sampleNmr,sample3)

def addSoundsTogether(sound1,sound2):
    returnSound = sound1
    for i in xrange(0,sound2.__len__()):
        returnSound.append(sound2[i])
    return returnSound
def outputSound(sound,sound_name):
    soundfile = wave.open(sound_name, "w")
    soundfile.setparams((1, 2, 44100, sound.__len__(), 'NONE', 'not compressed'))
    soundOutput = []
    for i in xrange(0,sound.__len__()):
        packaged_value = struct.pack("<h", sound[i])
        soundOutput.append(packaged_value)
    sound_string = "".join(soundOutput)
    soundfile.writeframes(sound_string)
    soundfile.close()
outputSound(addSoundsTogether(listValues(Final_round),listValues(Sound)),"testfile.wav")

# frames = []
# for i in xrange(0, nframes):
#     noiseFrames = Sound.readframes(1)
#     frameValue = struct.unpack("<h", noiseFrames)
#     frames.append(int(frameValue[0]))
# current_max = 0
# current_max = 0
# current_min = 0
# for volume in frames:
#     if volume > current_max:
#         current_max = volume
#     if volume < current_min:
#         current_min = volume


# values = []
#
# for j in range(0, SAMPLE_LENGTH):
#
#     # This is the time in seconds
#     TIME = float(j / SAMPLE_WIDTH)
#
#     # Here two tones are created using a given frequency
#     tone1 = pureTone(600, TIME)
#     tone2 = pureTone(150, TIME)
#
#
#     # Here we merge two tones to created a new tone
#     tone = merge2Waves(tone1, tone2)
#
#     # Here we adjust the volume, using a value from 0 to 1
#     tone = getVolume(tone, 0.5)
#     packaged_value = struct.pack("<h", tone)
#     values.append(packaged_value)
#
# value_str = "".join(values)
#
# Sound_out.writeframes(value_str)
# Sound_out.close()