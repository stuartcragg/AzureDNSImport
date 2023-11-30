# Set the path to the folder containing the zone files
$zoneFilesFolder = "C:\DNS-ZONE\Output"

# Set the Azure resource group name
$resourceGroupName = "change-to-your-resource-group"

# Get all .zone files from the folder
$zoneFiles = Get-ChildItem -Path $zoneFilesFolder -Filter "*.zone"

foreach ($file in $zoneFiles) {
    $zoneName = $file.BaseName
    $filePath = $file.FullName

    # Import the zone file into Azure DNS
    az network dns zone import -g $resourceGroupName -n $zoneName -f $filePath
}

Write-Host "DNS record import completed."
