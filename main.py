import wave
import struct
import math

# Open the music file for 8bit converter
music_file = wave.open("music.wav", "r")


# Create a list of values from a variable name of sound file wave.open("","r")
def list_values(sound_file):
    value_list = []
    for i in xrange(0, get_length(sound_file)):
        noise_frames = sound_file.readframes(1)
        value = struct.unpack("<h", noise_frames)
        value_list.append(int(value[0]))
    return value_list


# Get the length of the sound_file variable has to be wave.open("","r")
def get_length(sound_file):
    sample_length = sound_file.getnframes()
    return sample_length


# Get the value at a certain position, Accepts a list of values and the position.
def get_sample_value_at(sound, sample_number):
    for i in xrange(0, sound.__len__()):
        if i + 1 == sample_number:
            return sound[i]


# Set the value at a certain position, Accepts a list, the position, and the value to change it to.
def set_sample_value_at(sound, sample_number, value):
    for i in xrange(0, sound.__len__()):
        if i + 1 == sample_number:
            sound[i] = value


# Get the volume for pure tones
def get_volume(sound, volume):
    new_sound = volume * sound * 40000
    return new_sound


# This function creates an average of two tones and returns the value
def merge_waves(sound1, sound2, sound3, sound4, total):
    merged_sound = ((sound1 + sound2 + sound3 + sound4) / total)
    return merged_sound


# This function creates a pure tone
def pure_tone(frequency, time):
    tone = math.sin(2 * math.pi * frequency * time)
    return tone


# Add one sound file into an other, has to be the same length. sound1 and 2 are variables storing sound files.
def add_sound_into(sound1, sound2):
    for sample_nmr in range(0, get_length(sound1)):
        sample1 = get_sample_value_at(sound1, sample_nmr)
        sample2 = get_sample_value_at(sound2, sample_nmr)
        sample3 = sample1 + sample2
        set_sample_value_at(sound2, sample_nmr, sample3)


# Add join two lists together. Accepts two lists.
def add_sounds_together(sound1, sound2):
    return_sound = sound1
    for i in xrange(0, sound2.__len__()):
        return_sound.append(sound2[i])
    return return_sound


# Takes a list and creates a sound file. Example output_sound(values,"values.wav") will create a file values.wav.
def output_sound(sound, sound_name):
    sound_file = wave.open(sound_name, "w")
    sound_file.setparams((1, 2, 44100, sound.__len__(), 'NONE', 'not compressed'))
    sound_output = []
    for i in xrange(0, sound.__len__()):
        packaged_value = struct.pack("<h", sound[i])
        sound_output.append(packaged_value)
    sound_string = "".join(sound_output)
    sound_file.writeframes(sound_string)
    sound_file.close()


# Creates a sin wave.
def sine_wave(freq, amplitude):
    build_sin = []
    sampling_rate = 44100
    interval = 1.0 / freq
    samples_per_cycle = interval * sampling_rate
    max_cycle = 2 * math.pi
    for pos in xrange(0, 44100):
        raw_sample = math.sin((pos / samples_per_cycle) * max_cycle)
        sample_val = int(amplitude * raw_sample)
        build_sin.append(sample_val)
    return build_sin


# Takes a list of notes creates notes from A to G with the specified note length and pitch.
def keyboard(notes, note_length, pitch):
    full_song = []
    A = [440, 880, 1760]
    B = [494, 988, 1976]
    C = [523, 1046, 2093]
    D = [587, 1175, 2349]
    E = [659, 1319, 2637]
    F = [698, 1397, 2794]
    G = [784, 1568, 3136]

    for i in range(notes.__len__()):
        if notes[i] == "C":
            full_song = add_sounds_together(full_song, pure_tone_list(C[pitch], 0, 0, note_length, 0.5))
        elif notes[i] == "D":
            full_song = add_sounds_together(full_song, pure_tone_list(D[pitch], 0, 0, note_length, 0.5))
        elif notes[i] == "E":
            full_song = add_sounds_together(full_song, pure_tone_list(E[pitch], 0, 0, note_length, 0.5))
        elif notes[i] == "F":
            full_song = add_sounds_together(full_song, pure_tone_list(F[pitch], 0, 0, note_length, 0.5))
        elif notes[i] == "G":
            full_song = add_sounds_together(full_song, pure_tone_list(G[pitch], 0, 0, note_length, 0.5))
        elif notes[i] == "A":
            full_song = add_sounds_together(full_song, pure_tone_list(A[pitch], 0, 0, note_length, 0.5))
        elif notes[i] == "B":
            full_song = add_sounds_together(full_song, pure_tone_list(B[pitch], 0, 0, note_length, 0.5))
    return full_song


# Volume is from 0 to 1, frequency is normal frequency, length is in tenths of seconds
def pure_tone_list(frequency, frequency2, frequency3, length, volume):
    full_tone = []
    samples_per_second_1 = float(44100)
    samples_per_second_2 = 4410
    number_of_samples = (length * samples_per_second_2)
    for j in xrange(0, number_of_samples):

        # This is the current point in time in seconds
        time = float(j / samples_per_second_1)
        if frequency2 == 0 & frequency3 == 0:
            tone1 = pure_tone(frequency, time)
            tone = get_volume(tone1, volume)
        elif frequency3 == 0:
            tone1 = pure_tone(frequency, time)
            tone2 = pure_tone(frequency2, time)
            tone = merge_waves(tone1, tone2, 0, 0, 2)
        else:
            tone1 = pure_tone(frequency, time)
            tone2 = pure_tone(frequency2, time)
            tone3 = pure_tone(frequency3, time)
            tone = merge_waves(tone1, tone2, tone3, 0, 3)

        full_tone.append(tone)

    return full_tone


# Convert a 16bit integer into a 8bit integer, by dividing with the amount of 8bit integer possibilities
def eight_bit_int(value, volume):
    if 0 <= value:
        return value / 256 * volume
    else:
        return value / 256 * -volume


# Convert a sound file variable into an 8bit intiger wav file, volume has to be between 0 and 1
# Input Example convert_to_8bit(values,"values_8bit.wav",0.5)
def convert_to_8bit(sound_file, output_file_name,volume):
    values = list_values(sound_file)
    write_file = wave.open(str(output_file_name), "w")
    # The second variable has to be 1 for an 8 bit file.
    write_file.setparams((1, 1, 44100, values.__len__(), 'NONE', 'not compressed'))
    sound_output = []
    for frame in values:
        # We add 127 to offset the soundwaves in the center of the wave form Because an 8 bit intiger is 256 bit depth
        eight_bit_frame = 127 + eight_bit_int(frame, volume)
        # Format has to be <B for signed 8bit format.
        packaged_value = struct.pack('<B', int(eight_bit_frame))
        sound_output.append(packaged_value)
    sound_string = "".join(sound_output)
    write_file.writeframes(sound_string)
    write_file.close()


# Make a Song!!
# Song E,F,G,C,D,E,F,G,A,B,F,A,A,B,C,D,E,E,F,G,C,D,E,F,G,A,B,F,A,A,B,C,D,E,E,F,G,C,D,E,F,G,G,E,D,G,E,D,G,E,D,G,F,E,D,C

list_of_notes = raw_input("Input notes from A to G separated by commas! Example A,B,C,D,E,F,G): ")

# Note length is in tenths of a second, pitch is from 0 - 2, 0 being low frequency and 2 high
# Take the list of notes from raw input and split them on commas.
music = keyboard(list_of_notes.split(","), 4, 0)
# Output the sound
output_sound(music, "Music.wav")
# Convert the sound to 8 bit
print "Converting to 8bit Might take a second!"
convert_to_8bit(music_file, "Music_8bit.wav",0.5)

