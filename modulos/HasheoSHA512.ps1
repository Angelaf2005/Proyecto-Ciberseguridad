#Es necesario agregar las carpetas que se vayan utilizando en este archivo para obtener un buen hasheo de archivos
param(  
    [array]$TargetFolder=@(".","./__pycache__","./archivos","./API_KEY","./modulos","./.vscode","./pass"),
    [string]$ResultFile="hash\baseline.txt"
)
try {
    Set-Content $ResultFile $null
    foreach ($i In $TargetFolder){
        Get-ChildItem $TargetFolder | Get-FileHash -ErrorAction SilentlyContinue -Algorithm SHA512 | Select-Object -Property Hash, Path  | Add-Content $ResultFile -Encoding ascii 
    }
}
catch {
    
}



