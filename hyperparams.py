# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
By kyubyong park. kbpark.linguist@gmail.com. 
https://www.github.com/kyubyong/dc_tts
'''
class Hyperparams:
    '''Hyper parameters'''
    # pipeline
    lang = "ru"
    prepro = True  # if True, run `python prepro.py` first before running `python train.py`.
    
    # signal processing
    sr = 22050  # Sampling rate.
    n_fft = 2048  # fft points (samples)
    frame_shift = 0.0125  # seconds
    frame_length = 0.05  # seconds
    hop_length = int(sr * frame_shift)  # samples. =276.
    win_length = int(sr * frame_length)  # samples. =1102.
    n_mels = 80  # Number of Mel banks to generate
    power = 1.5  # Exponent for amplifying the predicted magnitude
    n_iter = 50  # Number of inversion iterations
    preemphasis = .97
    max_db = 100
    ref_db = 20

    # Model
    r = 4 # Reduction factor. Do not change this.
    dropout_rate = 0.05
    e = 128 # == embedding
    d = 256 # == hidden units of Text2Mel
    c = 512 # == hidden units of SSRN
    attention_win_size = 3

    # data
    # data = "/data/private/voice/LJSpeech-1.0"
    data = "ru_RU/by_book/male/minaev/oblomov"
    # data = "/data/private/voice/kate"
    # test_data = 'harvard_sentences.txt'
    test_data = 'bot_sentences.txt'
    if lang=="ru":
        vocab = u'''␀␃ !',-.:;?PE êАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё—'''
        max_N, max_T = 569, 988
    else:
        vocab = "PE abcdefghijklmnopqrstuvwxyz'.?" # P: Padding, E: EOS.

    # training scheme
    lr = 0.001 # Initial learning rate.
    logdir = "logdir/minaev"
    sampledir = 'samples'
    B = 24 # batch size
    num_iterations = 2000000
