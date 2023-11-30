import dns.zone
import dns.rdatatype
import os
import glob

# Set your input and output folder paths here
input_folder_path = r'C:\DNS-BIND\Input'
output_folder_path = r'C:\DNS-ZONE\Output'

def parse_bind_file(file_path, output_folder):
    domain = os.path.basename(file_path).replace('.txt', '')
    zone = dns.zone.from_file(file_path, origin=domain, relativize=False)

    # Generate new zone file content
    new_zone_content = generate_zone_content(zone, domain)

    # Write new zone file
    output_file_path = os.path.join(output_folder, domain + '.zone')
    with open(output_file_path, 'w') as f:
        f.write(new_zone_content)

def generate_zone_content(zone, domain):
    # Standard SOA record template (you may need to adjust the values)
    soa_record = (
        f'$TTL 3600\n'
        f'$ORIGIN {domain}\n\n'
        f'; SOA Record\n'
        f'@ 3600 IN SOA ns1-01.azure-dns.com. azuredns-hostmaster.microsoft.com (\n'
        f'    1 ; serial\n'
        f'    3600 ; refresh\n'
        f'    300 ; retry\n'
        f'    2419200 ; expire\n'
        f'    300 ; minimum ttl\n'
        f')\n'
    )

    output = soa_record
    for name, node in zone.nodes.items():
        for rdataset in node.rdatasets:
            # Skip SOA and NS records
            if rdataset.rdtype in [dns.rdatatype.SOA, dns.rdatatype.NS]:
                continue
            for rdata in rdataset:
                record_name = str(name).rstrip('.').replace(domain+'.', '')  # Remove trailing dot and domain from record name
                if rdataset.rdtype == dns.rdatatype.CNAME:
                    # Format CNAME target without trailing dot
                    target = str(rdata.target).rstrip('.')
                    output += f"{record_name} {rdataset.ttl} IN CNAME {target}\n"
                else:
                    # Format other record types
                    output += f"{record_name} {rdataset.ttl} IN {dns.rdatatype.to_text(rdataset.rdtype)} {rdata}\n"
    return output

# Process each .txt file in the input folder
for file_path in glob.glob(os.path.join(input_folder_path, '*.txt')):
    parse_bind_file(file_path, output_folder_path)

print("Zone file conversion completed.")
