# Introduction

DNS Zones exported from a DNS Provider in BIND format can be converted in a batch to Zone files accepted by Azure. The first script requires an input folder where the BIND files are stored in TXT format. The script will convert the files from the input folder and add them to the output folder in .zone format.
The second script will read in the zone files and create a main.tf Terraform file that will setup the DNS zones in Azure. 
The final script will read in each zone file and add the records to the associated DNS Zone on Azure. 

# Getting Started

1. The first script has two input variables change the input path between the '' for the variable input_folder_path. This is where the exported BIND files are stored.
2. Change the path in output_folder_path to the folder path where you want the converted zone files to be stored.
3. Run the 1.0.0_Convert_BIND_to_Zone.py script to convert all of the BIND files in the input folder and output them to the output folder.
4. On the 2.0.0_Create_Azure_DNS_Terraform.py script, change the input_folder_path variable to the output folder from the previous step.
5. On the 2.0.0_Create_Azure_DNS_Terraform.py script, change the output_file_path to the location where the Terraform main.tf will be outputted to. The path must end in "main.tf" instead of being a folder path.
6. Run 2.0.0_Create_Azure_DNS_Terraform.py script to create the main.tf Terraform file.
7. Adjust the main.tf code according to your requirements. Change the location and name of the Resource Group.
8. Run az login --tenant 'your tenant id' to login to Azure.
9. Apply the main.tf Terraform to setup your required zones in Azure.
10. Lastly on the 3.0.0_Add_Records_to_Zones.ps1 Powershell script, change the $zoneFilesFolder variable to the location of your converted DNS Zone files.
11. On 3.0.0_Add_Records_to_Zones.ps1 change the Resource Group name to the name of your Resource Group hosting the Azure DNS Zones.
12. Authenticate on Powershell using az login --tenant 'your tenant id' to login to Azure.
13. Run the 3.0.0_Add_Records_to_Zones.ps1 Powershell script to add all of the records to the Azure DNS Zones.
14. Repoint the name servers on your DNS Registrar to the Azure Nameservers after confirming that the records look correct.

# Notes

1. Best practice would be to start with one or two zones to test the process.
2. The script assumes that all of your Zone files are contained within one folder and that all DNS Zones on Azure will be deployed into the same Resource Group.
3. If you have multiple Azure subscriptions, you will need to use Set-AzContext -Subscription "xxxx-xxxx-xxxx-xxxx" so that Terraform and Powershell know where to add the resources.

# Disclaimer

The scripts and code provided in this repository are for educational and demonstration purposes only. They are not intended for use in a production environment and should be thoroughly tested in a controlled setting before any attempt to use them in such a manner.

By using or implementing these scripts and code snippets, you agree that they come with no warranty of any kind, either expressed or implied. I am not responsible for any damage, data loss, or costs incurred as a result of using or implementing these scripts, nor will I be held liable for any direct, indirect, incidental, special, exemplary, or consequential damages.

It is your responsibility to evaluate the accuracy, completeness, and usefulness of any information, opinion, advice, or other content provided in conjunction with these scripts. Please exercise caution and consult with your IT department or a professional IT consultant before executing or implementing these scripts in any environment.

Use of the provided scripts and code is entirely at your own risk, and any actions taken upon the information on this repository are strictly at your own discretion and risk.
