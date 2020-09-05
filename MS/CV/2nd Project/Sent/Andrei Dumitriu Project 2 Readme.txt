1. Libraries
cv2==4.2.0
numpy==1.18.1
glob
io
os=='Linux-4.4.0-177-generic-x86_64-with-debian-stretch-sid'
pickle=4.0
matplotlib==3.2.1
ipython==7.13.0
Pillow==7.1.1
imutils==0.5.3
skimage==0.16.2
pdb



2. How to run each scenario

All 4 scenarios are in the same file jupyter lab file. If you run the cells in the given order, everything should be fine.

For all scenarios:
- use the template image provided. It should be placed in the same folder as the file.
- each scenario has in its cell the path-to-files.
- you only need to modify the "ground_truth_answers_path" and "images" path
- if the output file does not exist, it will be created. If it exists, data in it will be completely overwritten

Scenario 1:
- needs the templates (from the lab) in the Templates folder
- input should be in ./training_data/Task1
- output file is ./andrei_dumitriu_407/Task1/*.txt

Scenario 2:
- input should be in ./training_data/Task2
- output file is ./andrei_dumitriu_407/Task2/*.txt

Scenario 3:
- input should be in ./training_data/Task3
- output file is ./andrei_dumitriu_407/Task3/*.txt

Scenario 4:
- input should be in ./training_data/Task4
- output file is ./andrei_dumitriu_407/Task4/*.txt



