import socket
from common_ports import ports_and_services



#
# Function: validate_ip_address
# Determine valid IpV4 address
#
def validate_ipV4_address(address):
    parts = address.split(".")

    if len(parts) != 4:
        #print("IP address {} is not valid".format(address))
        return False

    for part in parts:
        if not isinstance(int(part), int):
            #print("IP address {} is not valid".format(address))
            return False

        if int(part) < 0 or int(part) > 255:
            #print("IP address {} is not valid".format(address))
            return False
 
    print("IP address {} is valid".format(address))
    return True


# 
# Function: get_open_ports()
# Usage: get_open_ports("209.216.230.240", [440, 445])
#        get_open_ports("www.stackoverflow.com", [79, 82])
# Description:
#  This function takes a target argument and a port_range argument. 
#  target can be a URL or IP address. port_range is a list of 
#  two numbers indicating the first and last numbers of the range 
#  of ports to check.
#
def get_open_ports(target, port_range, desc = False):
  open_ports = []
  
  desc_results = ""
  
  if validate_ipV4_address(target):
    # hmm, is it an URL
    desc_results += "Open ports for {}\n".format(target)
  else:
    try:
      IP = socket.gethostbyname(target);
      print("Target {} is ({})".format(target, IP))
      desc_results += "Open ports for {} ({})\n".format(target, IP)
    except:
      return "Error: Invalid IP address"

  desc_results += "{}     {}\n".format("PORT", "SERVICE")
  
  client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  for p in range(port_range[0], port_range[1]):
    try:
      print("Connecting {}, port {} ...".format(target, p))
      # client_sock.settimeout(10.0)
      client_sock.connect((target, p))
      if desc:
        try:
          if ports_and_services[p] != None:
            print(p, '->', ports_and_services[p])
            desc_results += "{}     {}\n".format(target, ports_and_services[p])
        except KeyError:
          #print("Key does not exist in common_ports")
          pass
      else:
        open_ports.append(p)      
      
      # client_sock.settimeout(None)
      client_sock.close()
    except:
      client_sock.close()
      # pass
      
  if desc:
    print(desc_results)
    return desc_results
  else:
    return(open_ports)

# if '__name__' == '__main__':
#print(get_open_ports("www.stackoverflow.com", [79, 443], True))