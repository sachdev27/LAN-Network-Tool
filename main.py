from src import asset,neighbourhood,DOS
import sys

def perform_functions(args):
    args = args[0]
    if args[1:] == "s":
        asset.speed_test()
    elif args[1:] == "c":
        asset.main()
    elif args[1:] == "sn":
        neighbourhood.run()
    elif args[1:] == "d":
        target = input("Enter Target IP: ")
        ip = input("Enter Target port : ")
        DOS.main([target,ip])
    elif args[1:] == "h":
        print('''
              -s : Speedtest Internet Connection
              -c : Checking Internet Connection
              -sn : Scanning Local Network
              -d  : ddos attack
              -h  : help 
              ''')

if __name__ == "__main__":
    print("Network Tools\n")
    perform_functions(sys.argv[1:])

