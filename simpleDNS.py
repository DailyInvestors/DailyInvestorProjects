import dns.resolver

def dns_lookup(domain):
  try:
    answers = dns.resolver.query(domain, 'A')
    for rdata in answers:
      print(rdata)
  except dns.resolver.NXDOMAIN:
    print(f"No such domain: {domain}")
  except Exception as e:
    print(f"An error occurred: {e}")

# Get domain from user
domain = input("Enter domain name: ")

# Perform DNS lookup
dns_lookup(domain)

