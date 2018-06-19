#!/usr/bin/env python

USAGE = """
ban-ip.py [-h] [-i 11.22.3.4] [-f file-with-ip-per-line]
"""
import click

import subprocess

class F2bException(Exception):
    pass

@click.command()
@click.option('--ip', default="none", help='quad IP')
@click.option('--filename', default="none",
              help='The file containing quad IP\'s, one per line.')

def main(ip, filename):
    """Run from command line according to USAGE."""

    if ip != "none":
        runCommand(ip)
        return

    if filename == "none":
        return
    with open(filename) as f:
        print("using " +  filename)
        for line in f:
            ip = line
            runCommand(ip)
    return 

def runCommand(quadIP):
    '''
    Run the firewall-cmd command to ban a remote ip.
    :param quad-ip:
    '''
    richrule = "rule family='ipv4' source address='" + quadIP + "' reject"
    fwcmd =  '--add-rich-rule="' +  richrule  + '"'   
    subprocess.check_output(["echo", "Hello World!"])
    print( "here are the args firewall-cmd" + " --permanent --zone=FedoraWorkstation " + fwcmd)
    try:
        #subprocess.check_output(["firewall-cmd", "--permanent --zone=FedoraWorkstation", fwcmd])
    except subprocess.CalledProcessError:
        raise F2bException("s p error")
    subprocess.check_output(["echo", "Hello World2!"])

if __name__ == '__main__':
    main()

