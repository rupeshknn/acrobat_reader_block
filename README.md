# acrobat_reader_block
## Block Adobe Acrobat Pro from accessing the internet using py and ps.
Note : I am assuming you already have python installed and know how to run python scripts

# Instructions
------------------------------------------------------------------------
step1: 
open adober.py in notepad and verify the adobe install directories

step2:
run the python script adober.py 

step3:
upon running the script a new text file named "Adobe_Blocklist.txt" will be created with list of all .exe files in the adobe directories inclusing their path.

step4:
open adober.ps1 using notepad and edit the path to Adobe_blocklist.txt with the path in your PC

step5:
open powershell with administrator access

step6:
execute "Set-ExecutionPolicy -RemoteSigned" followed by "A" (Yes to all)

step7:
execute "./adober.ps1" in powershell

------------------------------------------------------------------------
I have left a sample blocklist which is from my PC for reference
