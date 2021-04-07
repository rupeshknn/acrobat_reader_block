import os
dir_path = os.path.dirname(os.path.realpath(__file__))

f = open(dir_path + "\Adobe_Blocklist.txt", "a")

#found the 1st directory by clicking 'open file location' on some adobe programs running in background from task manager

Adobe_dirs={"C:\\Windows\\Installer\\$PatchCache$\\Managed\\68AB67CA3301FFFF7706C0F070E41400\\15.7.20033","C:\Program Files (x86)\Common Files\Adobe","C:\Program Files (x86)\Adobe\Acrobat DC"}


for dirs in Adobe_dirs:
	for root, dirs, files in os.walk(dirs):
	    for file in files:
        	    if file.endswith(".exe"):
                	f.write(os.path.join(root, file))
                	f.write("\n")