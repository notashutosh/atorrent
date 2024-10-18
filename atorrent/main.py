import argparse
import bencodepy
import urllib.parse
import socket
import struct


def parse_torrent_file(file_path):
    with open(file_path, 'rb') as file:
        torrent_data = bencodepy.decode(file.read())
    return torrent_data


def get_announce_url(torrent_data):
    return torrent_data[b'announce'].decode()


def get_peers(announce_url):
    parsed_url = urllib.parse.urlparse(announce_url)
    ip = socket.gethostbyname(parsed_url.hostname)
    port = parsed_url.port or 80

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)

    connection_id = 0x41727101980
    transaction_id = 12345

    packet = struct.pack('>QII', connection_id, 0, transaction_id)
    sock.sendto(packet, (ip, port))
    action, transaction_id, connection_id = struct.unpack(
        '>IIQ', sock.recvfrom(16)[0])
    print(connection_id)


def main():
    parser = argparse.ArgumentParser(
        description='A command line tool for managing torrents.')
    parser.add_argument('action', choices=[
                        'start', 'stop', 'status'], help='Action to perform')
    parser.add_argument('file', help='Path to the torrent file')
    args = parser.parse_args()

    if args.action == 'start':
        print("Starting torrent:", args.file)
        torrent_data = parse_torrent_file(args.file)
        announce_url = get_announce_url(torrent_data)
        get_peers(announce_url)

    elif args.action == 'stop':
        print("Stopping torrent...")
    elif args.action == 'status':
        print("Torrent status...")


if __name__ == '__main__':
    main()
