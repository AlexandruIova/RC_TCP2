#!/usr/bin/env python3

from http.server import CGIHTTPRequestHandler, HTTPServer

def main():
	httpd = HTTPServer(('',5556),CGIHTTPRequestHandler)
	print( "Starting webserver ...")
	httpd.serve_forever()
	print("Error in server!")    


if __name__ == "__main__":
	main()
