#Es necesario agregar las carpetas que se vayan utilizando en este archivo para obtener un buen hasheo de archivos
param(  
    [array]$TargetFolder=@(".","./__pycache__","./archivos","./API_KEY","./modulos","./.vscode"),
    [string]$ResultFile="hash\baseline.txt"
)
try {
    foreach ($i In $TargetFolder){
        Get-ChildItem $TargetFolder | Get-FileHash -ErrorAction SilentlyContinue -Algorithm SHA512 | Select-Object -Property Hash, Path | Format-Table -HideTableHeaders | Out-File $ResultFile -Encoding ascii
    }
}
catch {
    
}



