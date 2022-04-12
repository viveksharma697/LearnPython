# get the domain name using an IP address

def get_domain_name(ip_address):
  import socket
  result=socket.gethostbyaddr(ip_address)
  return list(result)[0]
print("Domain name using PTR DNS:")
print(get_domain_name("8.8.8.8"))