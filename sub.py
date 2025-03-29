import socket
import threading
import time
import logging

# Configure logging
logging.basicConfig(filename='subdomain_finder.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define target domains/IPs 
target_domains = ["example.com", "192.168.1.100", "192.168.1.101"] 
# You can add more targets here

# Define subdomain wordlist (example)
subdomains = ["www", "mail", "admin", "ftp", "secure", "blog", "shop"] 

def check_socket(domain_or_ip, subdomain):
    """
    Checks if a socket connection can be established to the given subdomain.

    Args:
        domain_or_ip (str): The target domain or IP address.
        subdomain (str): The subdomain to check.

    Returns:
        bool: True if connection successful, False otherwise.
    """
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        # Construct the full domain/IP
        host = f"{subdomain}.{domain_or_ip}" 
        # Attempt to connect
        s.connect((host, 80))  # Connect to port 80 (HTTP)
        s.close()
        logging.info(f"Found subdomain: {host}")
        return True
    except (socket.gaierror, socket.error) as e:
        # Handle connection errors (e.g., DNS resolution, connection refused)
        # logging.debug(f"Connection failed for {host}: {e}") 
        return False

def worker(domain_or_ip, subdomain_list):
    """
    Worker thread to check subdomains concurrently.

    Args:
        domain_or_ip (str): The target domain or IP address.
        subdomain_list (list): List of subdomains to check.
    """
    for subdomain in subdomain_list:
        if check_socket(domain_or_ip, subdomain):
            # Handle successful connection (e.g., store in a database, print to console)
            pass

if __name__ == "__main__":
    threads = []
    for target in target_domains:
        thread = threading.Thread(target=worker, args=(target, subdomains))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

print("Subdomain scan complete.") 


