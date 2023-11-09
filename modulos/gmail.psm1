function correos {
    param (
        [Parameter(Mandatory)]
        [string]
        $a
    )
    $correo = Get-Content -Path "./pass/mail.txt"
    $pass = Get-Content -Path "./pass/pass.txt"
    $credencial = New-Object System.Management.Automation.PSCredential -ArgumentList $correo,(ConvertTo-SecureString -String $pass -AsPlainText -Force)
    $texto = "La tarea ha finalizado si"
    $cuerpo = "El programa ha finalizado su ejecucion, se mandan los resultados"
    Send-MailMessage -From $correo -To $a -Subject $texto -Body $cuerpo -SmtpServer "smtp.gmail.com" -Credential $credencial -UseSsl -Port 587 -Attachments ".\pass\archivos.zip" -ErrorAction SilentlyContinue
}
