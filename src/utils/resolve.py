# If dnslib is not installed
# run the "pip install dnslib" command to install
import dnslib

def resolveHostname(targetName):
    resolver = dnslib.Resolver
    try:
        result = resolver.req(targetName, qtype="A")
        return result.rrset[0].rdata
    except:
        return None
