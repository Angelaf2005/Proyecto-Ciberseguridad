using module Send-MailKitMessage;
function credencial {
    $credenciales = Get-Credential
    return $credenciales
}
function correo($cred) {
    Send-MailKitMessage -SMTPServer smtp.gmail.com -Port 587 -From "angel.alvflopia@gmail.com" -Recipientlist "adrian.alvflo201@gmail.com" -Subject tema -TextBody texto -Credential $cred;
}
$c = credencial
correo($c)