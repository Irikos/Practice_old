import shutil
import os
import glob

base_folder = './images_renamed'
files = glob.glob(os.path.join(base_folder, "*.jpg"))


print(len(files))
for i in range(0, 1):
    print(files[i])
    image_type = files[i].split('/')[-1].split('_')[0]
    image_number = files[i].split('/')[-1].split('_')[1].split('.')[0]
    image_extension = files[i].split('/')[-1].split('_')[1].split('.')[1]
    print(image_type)
    print(image_number)
    print(image_extension)
    
    answers_file_name = base_folder + "/image_" + image_number + ".txt"
    
    answers_file = open(answers_file_name, "r")
    answers_data = answers_file.readlines()
    option = answers_data[0][0]
    variant = answers_data[0][2]
    new_name = ""
    # scenario 1, comment it for scenario 3
    if (image_type == "image"):
        new_name = image_number + "_scanned_" + option + variant 
    

    # scenario 2, comment it for scenario 3
    if (image_type == "perspective"):
        new_name = image_number + "_perspective_" + option + variant 

    if (image_type == "rotated"):
        new_name = image_number + "rotated" + option + variant 
    
    # scenario 3 ---- comment scenario 1 and 2, copy the entire initial images folder again and apply only scenario 3
    new_name =
    print(new_name)
    # print(files[i], " -> ", new_name)
    # shutil.move("./pics/" + files[key],"./pics/img" + str(key) + ".jpeg")