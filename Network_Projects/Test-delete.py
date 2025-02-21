import ipaddress as ip  # Imports the ipaddress library and aliases it as 'ip' for easier reference

print("\n\n Press 1: For find the Network ")  # Displays an initial prompt to the user for selecting the network option

UserInput = input("Please enter the Network (eg: 192.168.250.0/24)                    : ")  
# Prompts the user to input a network address in CIDR notation

Network_ID = ip.ip_network(UserInput, strict=False)  # Converts user input into a network object and allows non-strict mode, which corrects non-standard inputs
HostRange = list(ip.ip_network(Network_ID).hosts())  # Generates a list of all usable host IPs within the network
Broadcast_ID = list(ip.ip_network(Network_ID))  # Generates a list of all addresses in the network, including network and broadcast addresses
subnetmask = list(ip.IPv4Network(Network_ID).subnets(new_prefix=25))  # Divides the network into subnets with a /25 prefix length

print("\n#")  # Prints a separator for output readability
print(f'Please find the result of Network ID for the given Host            : {Network_ID} ')  # Displays the network ID for the given input

print(f'Please find the result of useasble IP address for the given Network: {len(HostRange)}')  # Displays the number of usable IP addresses in the network

print(f'Please find the result of Network Range for the given Host         : {HostRange[0]} - {HostRange[-1]} ')  # Shows the usable IP address range in the network by displaying the first and last usable IPs

print(f'Please find the result of Broadcast ID for the given Host          : {Broadcast_ID[-1]} ')  # Displays the broadcast address for the network

if HostRange[0].is_private:  # Checks if the first usable IP in the host range is a private IP address
    print(f'Please find the result of Address is for the given input           : Address is private ')    # Prints that the IP address is private if the check is true
else:   
    print(f'Please find the result of Address is for the given input           : Address is not private')       # Prints that the IP address is not private if the check is false
