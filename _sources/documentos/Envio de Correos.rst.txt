Envio de correos
================

Esta herramienta está diseñada para el envío automático de correos. La cuenta que se utilizará para enviar correos
se debe colocar dentro de los archivos *pass.txt* y *mail.txt* dentro de la carpeta pass.

.. code-block:: powershell

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

La cuenta a la que se le mandará la información debe especificarse con el parametro *-MM*. **-MM example@example.com**
De esta manera enviaremos los archivos en .zip al destinatario especificado.