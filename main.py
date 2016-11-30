import wave
import struct
import math

Sound= wave.open("noise2.wav","r")
Sound_out= wave.open("noise3.wav","w")
# Final_round = wave.open("final_round.wav","r")
# Final_round_offset = wave.open("final_round_offset.ogg","w")
# Final_round_echo = wave.open("final_round_echo.ogg","w")
# Read_params = Sound.getparams()
# print Read_params
SAMPLE_LENGTH = 88200
SAMPLE_WIDTH = float(44100)
Sound_out.setparams((1, 2, SAMPLE_WIDTH, SAMPLE_LENGTH, 'NONE', 'not compressed'))



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
def mergeWaves(sound1, sound2, sound3,sound4, total):
    mergedSound = ((sound1 + sound2 + sound3 + sound4)/total)
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


def sineWave(freq,amplitude):
    buildSin = []
    samplingRate = 44100
    interval = 1.0 / freq
    samplesPerCycle = interval * samplingRate
    maxCycle = 2 * math.pi
    for pos in xrange(0,44100):
        rawSample = math.sin((pos / samplesPerCycle) * maxCycle)
        sampleVal = int(amplitude * rawSample)
        buildSin.append(sampleVal)
    return buildSin

def envelopeWave(freq, amplitude, attack_time,
sustain_time, release_time):
    buildSin = []
    samplingRate = 44100
    interval = 1.0 / freq
    samplesPerCycle = interval * samplingRate
    maxCycle = 2 * math.pi
    for pos in xrange(0,44100):
        rawSample = math.sin((pos / samplesPerCycle) * maxCycle)
        if pos < attack_time:
            sampleVal = int((amplitude+4000) * rawSample)
        elif sustain_time > pos > attack_time:
            sampleVal = int(amplitude * rawSample)
        elif release_time > pos > sustain_time:
            sampleVal = int((amplitude*0+1) * rawSample)
        buildSin.append(sampleVal)
    return buildSin





def keyboard(notes,noteLength,pitch):
    fullSong = []
    A = [440,880,1760]
    B = [494,988,1976]
    C = [523,1046,2093]
    D = [587,1175,2349]
    E = [659,1319,2637]
    F = [698,1397,2794]
    G = [784,1568,3136]

    for i in range (notes.__len__()):
        if notes[i] == "C":
            fullSong = addSoundsTogether(fullSong, pureToneList(C[pitch],0,0,noteLength,0.5))
        elif notes[i]== "D":
            fullSong = addSoundsTogether(fullSong, pureToneList(D[pitch],0,0,noteLength, 0.5))
        elif notes[i]== "E":
            fullSong = addSoundsTogether(fullSong, pureToneList(E[pitch],0,0, noteLength, 0.5))
        elif notes[i]== "F":
            fullSong = addSoundsTogether(fullSong, pureToneList(F[pitch],0,0, noteLength, 0.5))
        elif notes[i]== "G":
            fullSong = addSoundsTogether(fullSong, pureToneList(G[pitch],0,0, noteLength, 0.5))
        elif notes[i]== "A":
            fullSong = addSoundsTogether(fullSong, pureToneList(A[pitch],0,0, noteLength, 0.5))
        elif notes[i]== "B":
            fullSong = addSoundsTogether(fullSong, pureToneList(B[pitch],0,0, noteLength, 0.5))
    return fullSong








# sineWave = envelopeWave(440,6000,4100,35000,5000)
# print sineWave
# outputSound(sineWave,"sineWave.wav")
#outputSound(addSoundsTogether(listValues(Final_round),listValues(Sound)),"testfile.wav")

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

# Volume is from 0 to 1, frequency is normal frequency, length is in tenths of seconds
def pureToneList(frequency,frequency2, frequency3,length,volume):
    fullTone = []
    samplesPerSecond1 = float(44100)
    samplesPerSecond2 = 4410
    numberOfSamples = (length * samplesPerSecond2)
    for j in xrange(0, numberOfSamples):

        # This is the current point in time in seconds
        time = float(j / samplesPerSecond1)
        print time
        if frequency2 == 0 & frequency3 == 0:
            tone1 = pureTone(frequency,time)
            tone = getVolume(tone1, volume)
        elif frequency3 == 0:
            tone1 = pureTone(frequency,time)
            tone2 = pureTone(frequency2, time)
            tone = mergeWaves(tone1, tone2,0,0,2)
        else:
            tone1 = pureTone(frequency, time)
            tone2 = pureTone(frequency2, time)
            tone3 = pureTone(frequency3, time)
            tone = mergeWaves(tone1, tone2, tone3,0,3)


        fullTone.append(tone)

    return fullTone


#Make a Song!!
notes = ["B","B","G","G","F","F","E","E","D","D","C"]

# note length is in tenths of a second, pitch is from 0 - 2, 0 being low frequency and 2 high
music = keyboard(notes,5,0)
outputSound(music,"music.wav")
