while ($true) {
    Clear-Host
    $filePath = "C:\Users\alexg\VirtualBox VMs\AGRp2_default_1697985729502_73988\generic-ubuntu2204-virtualbox-disk001.vmdk"  # Replace with the actual file path
    
    $file = Get-Item $filePath
    $size = "{0:N2} GB" -f ($file.Length / 1GB)
    Write-Host ("File Size: $size")
    # Adjust the interval (in seconds) as needed
    Start-Sleep -Seconds 5
}
