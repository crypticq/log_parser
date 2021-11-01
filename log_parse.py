#!/usr/bin/env python3


##########################################
#Simple log parser created by Eng Yazeed:
#
#Usage python3 main.py acsess.log
##########################################

import sys

def main(filelog):
	print("##########################################")
	print("acsess log file parser")
	print("##########################################")

	ip = input("\nEnter ip address to search for:\n")

	file = open(filelog , 'r')
	for line in file.readlines():
		ip_lookup = line.split("-")[0]
		if ip_lookup == ip:
			print(line)


if __name__ == "__main__":
	filelog = sys.argv[1]
	main(filelog)
