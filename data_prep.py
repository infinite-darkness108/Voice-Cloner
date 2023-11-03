#!/usr/bin/python3

import os
import subprocess


# Define the directory paths
directories = ['data/dev', 'data/train', 'data/test']

# Create the directories if they do not exist
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)


##### create wav.scp,utt2spk and spk2utt, spk2gender,text files for all train-dev-test ; 70%-15%-15%

# Since we work for one speaker only; name : 'FSI'
spkr_id='FSI'

c_text = './complete_text'
with open (c_text,'r') as f:
     sentences=f.readlines()

# all the .wav files are stored as 1.wav, 2.wav, etc..,.
wavs_directory='/home/ananth/Downloads/wavs-20231101T160410Z-001/wavs'
wavs = os.listdir(wavs_directory)

# choosing uttids 108 to 162 for test (one-words)
# choosing the rest for train-dev
# 1 to 107 + 163 to 311 for train
# 312 to 365 for dev

count=0
while count<108:
   with open ('data/train/wav.scp','a') as f1:
      with open('data/train/utt2spk','a') as u1:
        with open('data/train/text','a') as w1:
         w1.write('{:03}'.format(int(count+1))+" "+sentences[count]) 
         u1.write('{:03}'.format(int(count+1))+" "+spkr_id+"\n")
         f1.write('{:03}'.format(int(count+1))+" "+wavs_directory+"/"+'{:03}'.format(int(count+1))+'.wav'+"\n")
         count+=1
    
while count<163:
   with open ('data/test/wav.scp','a') as f2:
     with open('data/test/utt2spk','a') as u2:
       with open('data/test/text','a') as w2:
         w2.write(str(count+1)+" "+sentences[count]) 
         u2.write(str(count+1)+" "+spkr_id+"\n")
         f2.write(str(count+1)+" "+wavs_directory+"/"+str(count+1)+'.wav'+"\n")
         count+=1        
             
while count<310:
   with open ('data/train/wav.scp','a') as f1:
     with open('data/train/utt2spk','a') as u1:
       with open('data/train/text','a') as w1:
         w1.write(str(count+1)+" "+sentences[count]) 
         u1.write(str(count+1)+" "+spkr_id+"\n")
         f1.write(str(count+1)+" "+wavs_directory+"/"+str(count+1)+'.wav'+"\n")
         count+=1 
             
while count<365:
   with open ('data/dev/wav.scp','a') as f3:
     with open('data/dev/utt2spk','a') as u3:
       with open('data/dev/text','a') as w3:
         w3.write(str(count+1)+" "+sentences[count]) 
         u3.write(str(count+1)+" "+spkr_id+"\n")
         f3.write(str(count+1)+" "+wavs_directory+"/"+str(count+1)+'.wav'+"\n")
         count+=1    
         
         
# Run the command for spk2utt files generation and handling sorting issues

#subprocess.call("sort -k1,1 -o data/train/wav.scp data/train/wav.scp", shell=True)
#subprocess.call("sort -k1,1 -o data/train/utt2spk data/train/utt2spk", shell=True)
subprocess.call("./utils/utt2spk_to_spk2utt.pl ./data/train/utt2spk > ./data/train/spk2utt", shell=True) 
subprocess.call("./utils/utt2spk_to_spk2utt.pl ./data/dev/utt2spk > ./data/dev/spk2utt", shell=True)         
subprocess.call("./utils/utt2spk_to_spk2utt.pl ./data/test/utt2spk > ./data/test/spk2utt", shell=True) 


with open('data/train/spk2gender','a') as g1:
 with open('data/dev/spk2gender','a') as g2:
   with open('data/test/spk2gender','a') as g3:
     g1.write(spkr_id+" "+"f"+"\n")
     g2.write(spkr_id+" "+"f"+"\n")
     g3.write(spkr_id+" "+"f"+"\n")
             
