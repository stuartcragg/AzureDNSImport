import os

input_folder_path = r'C:\DNS-ZONE\Output'
output_file_path = r'C:\DNS-Terraform\main.tf'

with open(output_file_path, 'w') as f:
    f.write('provider "azurerm" {\n  features {}\n}\n\n')
    f.write('resource "azurerm_resource_group" "example" {\n  name     = "example-resources"\n  location = "West Europe"\n}\n\n')

    for filename in os.listdir(input_folder_path):
        if filename.endswith('.zone'):
            zone_name = filename[:-5]  # Remove the '.zone' extension
            dns_resource_name = zone_name.replace('.', '_')  # Replace '.' with '_' for a valid Terraform resource name
            f.write(f'resource "azurerm_dns_zone" "{dns_resource_name}" {{\n')
            f.write(f'  name                = "{zone_name}"\n')
            f.write('  resource_group_name = azurerm_resource_group.example.name\n}\n\n')
