import subprocess
def powcor(a,b):
    comand = "Import-Module ./"+a+";correos -a "+b
    subprocess.run(["powershell","-ExecutionPolicy","Unrestricted","-Command",comand,"-ErrorAction SilentlyContinue"],capture_output=False)
    