if( Test-Path env:VIRTUAL_ENV)
{
 Write-Host 'You are already in a virtual enviorment'
 $vnv= Read-Host 'Do you want to deactivate virtual env? y/n :'
 if($vnv -eq 'y')
 {
    deactivate
    Exit
 }
}
$set_env = Read-Host 'Do you want to Create a new virtual env? y/n :'
if($set_env -eq 'y')
{
    $env = Read-Host 'Name your virtual enviorment: '
    virtualenv $env 
}
Write-Host 'Activating your virtual enviorment'
$venv = Read-Host 'Enter your virtual enviorment name: '
$ready = Read-Host 'Do you want to activate virtual enviorment? y/n :'

if($ready -eq 'y')
{
    $getfile= Get-ChildItem | Where-Object {$_.Name -match "$venv"}
    $activate_Env = "$getfile/bin/activate.ps1"
    & $activate_Env
    if( Test-Path env:VIRTUAL_ENV)
    {
        Write-Host 'Installing requirements.txt'
        pip install -r requirements.txt
        
    }
}
elseif ($ready -eq 'n') 
{
 Exit
}