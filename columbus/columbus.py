import sys
import os
import optparse
import logging
from controller import discover_software_container

IMG_WORKSPACE = "/Users/nagowda/Documents/columbus/imgworkspace"
DISCOVERY_OPTIONS = ['bin_names', 'file_paths', 'func-names',
                     'docker_history', 'pack_manager']


def main():
    logging.basicConfig(filename='./columbus.log', level=logging.INFO,
                        format='%(asctime)s %(message)s')

    usage = ("usage: python %prog -f <config_file> {--list | --discover } "
             "--route {bin_names | file_paths | func_names | docker_history "
             "| pack_manager}} <image_path>")
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-l", "--list",  action="store_true", dest="listop",
                      default=False, help="list all the layers")
    parser.add_option("-d", "--discover",  action="store_true", dest="discover", default=True, help="Discover software from \
    the image.")
    parser.add_option(
        "-r", "--route",  action="store", dest="route", default=None,
        help="specify discovery technique. \
        Choose from {bin-names, file-paths, func-names, docker-history, "
        "pack-manager}")
    parser.add_option("-f", action="store", dest="systagfile",
                      help="System tag file")

    opts, args = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")

    systagfile = opts.systagfile
    listop = opts.listop
    discover = opts.discover
    route = opts.route
    imgpath = args[0]

    if not systagfile:
        parser.error("No config file specified")
    if route and route not in DISCOVERY_OPTIONS:
        parser.error("incorrect discovery mode specified")
    if not listop and not discover:
        parser.print_help()

    columbus(imgpath, systagfile, route=route,
             listop=listop, discover=discover)


def columbus(imgpath, systagfile, route=None, listop=False, discover=True):
    if not route:
        route = DISCOVERY_OPTIONS[0]

    if not os.path.exists(IMG_WORKSPACE):
        os.makedirs(IMG_WORKSPACE)

    if not os.path.exists(imgpath):
        print("Invalid image\n")
        sys.exit(1)

    discover_software_container('eureka', imgpath, route, systagfile)
    # process = psutil.Process(os.getpid())
    # print "Memory Used %0.2f"%(float(process.get_memory_info().rss)/1000000)


if __name__ == "__main__":
    main()
