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



2. How to run each scenario

All 4 scenarios are in the same file jupyter lab file. If you run the cells in the given order, everything should be fine.

For all scenarios:
- use the template image provided. It should be placed in the same folder as the file.
- each scenario has in its cell the path-to-files.
- you only need to modify the "ground_truth_answers_path" and "images" path
- output file is ./dumitriu_andrei_taski.txt, i = 1..4, based on scenario
- if the output file does not exist, it will be created. If it exists, data in it will be completely overwritten

Scenario 1:
- assumes the file names are "number_scanned_OptionVariant.jpg". Example: "01_scanned_F1.jpg"
- output: ./dumitriu_andrei_task1.txt


Scenario 2:
- assumes the file names are "number_rotated_OptionVariant.jpg" or "number_perspective_OptionVariant.jpg". Example: "001_rotated_F1.jpg" and "001_perspective_F1.jpg"
- output: ./dumitriu_andrei_task2.txt

Scenario 3:
- assumes the file names are "number.jpg". Example: "01.jpg"
- output: ./dumitriu_andrei_task3.txt

Scenario 4:
- assumes the file names are "number_hw.jpg". Example: "25_hw.jpg"
- output: ./dumitriu_andrei_task4.txt



Your project should include a README file containing the following information:

1. the libraries required to run the project including the full version of each library

Example:

numpy==1.15.4
opencv_python==4.1.1.26
scikit_image==0.15.0
tensorflow_gpu==1.12.0
Pillow==7.0.0
scikit_learn==0.22.1
skimage==0.0
tensorflow==2.1.0

2. how to run each scenario and where to look for the output file.

Example:

Scenario 1: 
script: scenario_1.py
function: predict_grades(input_folder_name), where input_folder_name is the path to the folder containing the scanned images
output: the output file is results/grades_scanario_1.txt

Scenario 2: ...

Scenario 3: ...

Scenario 4: ...

