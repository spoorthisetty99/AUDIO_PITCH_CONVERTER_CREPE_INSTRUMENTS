# AUDIO_PITCH_CONVERTER_CREPE_intruments

Crepe is a deep learning-based system that can be used for pitch estimation from audio signals. It provides a convenient way to convert audio signals from musical instruments into corresponding pitch values. The pitch estimation is a crucial task in music analysis, transcription, and other applications involving audio processing.

It's important to note that Crepe is just one of many pitch estimation methods available. Depending on your specific needs, there may be alternative approaches or libraries that could also be suitable for your task. However, Crepe has gained popularity due to its accuracy and ease of use.

in this repo, you need audio samples in form of .wav format using which ull be converting it into a .csv where frequency,time and confidence of the corresponsing audio will be saved. this will be done using crepe
the main aim of this repo is to comapre two audios and compare the frequences, keeping the first audio as reference , giving user the changes to be done for getting the original output back.
this helps a musician to practice his peice according to another. 


install crepe:

pip install crepe

get a csv file from wav file:

crepe ~/audio_sample.csv

another method to get csv file is from python code which is given above as "crepe_original" , have to input audio name as well as the csv file that will be created.


crepe_original_piano.py will have the second audio u will want to compare,this will as well create another csv file

finally piano_compare will be the file which will compare both these audios and give output comparing and giving comment to the user


OUTPUTS:

![guitar_flute](https://github.com/spoorthisetty99/AUDIO_PITCH_CONVERTER_CREPE_intruments/assets/117083687/a36f132a-a96e-4e02-a17f-e34be1a6466f)
![Screenshot from 2023-07-10 20-29-53](https://github.com/spoorthisetty99/AUDIO_PITCH_CONVERTER_CREPE_intruments/assets/117083687/1d74142c-fc95-4103-b64c-7535a652d043)
