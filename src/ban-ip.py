#!/usr/bin/env python

USAGE = """
ban-ip.py [-h] [-i 11.22.3.4] [-f file-with-ip-per-line]
"""

import sys, getopt, subprocess

class F2bException(Exception):
    pass


def runCommand(quadIP):
    '''
    Run the firewall-cmd command to ban a remote ip.
    :param quad-ip:
    '''
    richrule = "rule family='ipv4' source address='" + quadIP + "' reject"
    fwcmd =  '--add-rich-rule="' +  richrule  + '"'   
    subprocess.check_output(["echo", "Hello World!"])
    subprocess.check_output(["echo", "firewall-cmd", "--permanent", fwcmd])
    try:
        subprocess.check_output(["firewall-cmd", "--permanent", fwcmd])
    except subprocess.CalledProcessError:
        raise F2bException("s p error")
    subprocess.check_output(["echo", "Hello World2!"])
    

def main(argv=None):
    """Run from command line according to USAGE."""
    if argv is None:
        argv = sys.argv

    if (len(argv) < 2 and not (('-h' in argv) or ('--help' in argv))):
        raise F2bException('Bad args')
    try:
        opts, argv = getopt.getopt(argv[1:], 'hi:f',
          ['help', 'ip=', 'filename='])
    except getopt.GetoptError as opt_error:
        msg, bad_opt = opt_error
        raise F2bException("%s error: Bad option: %s, %s" % (argv[0], bad_opt, msg))

    quadIP = ""
    fname = ""
    for opt, val in opts:
        if opt   in ('-h', '--help'):     print(USAGE); sys.exit()
        elif opt in ('-i', '--ip4'): quadIP = val
        elif opt in ('-f', '--file'): fname = val
        else:
            raise F2bException(USAGE)

    # option = argv[1]
    #with open(fname) as words:
    #    words = list(words)
    #    for word in words:
    if quadIP != "":
        runCommand(quadIP)
        return

    if fname == "":
        return
    with open(fname) as f:
        print("using " +  fname)
        for line in f:
            quadIP = line
            runCommand(quadIP)
    return 


if __name__ == '__main__':
    resp = main(sys.argv)

