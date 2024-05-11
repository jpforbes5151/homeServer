import os
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # starting valheim server
        if self.path == '/start_valheim/':  # Define the endpoint /run_script
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Run your shell script here
            # Replace 'your_script.sh' with the name of your shell script
            import subprocess
            subprocess.run(['sh', '/home/jserver/valheim_start.sh'])

            # Send a response to the client
            self.wfile.write(b'Valheim Server is spinning Up.')

        elif self.path == '/start_vrising/':  # Define the endpoint /run_script
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Run your shell script here
            # Replace 'your_script.sh' with the name of your shell script
            import subprocess
            subprocess.run(['sh', '/home/jserver/vrising_start.sh'])

            # Send a response to the client
            self.wfile.write(b'Vrising Server is spinning up.')

        else:
            # If the requested path is not recognized, serve files as usual
            return super().do_GET()


def run(
    server_class=HTTPServer,
    handler_class=CustomRequestHandler,
    port=69420,
    directory=None, # forces the server to only display files that it should. default is set to None.
):
    if directory:  # Change the current working directory if directory is specified
        os.chdir(directory)
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on http://localhost:{port} from directory '{directory}'...")
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Server")
    parser.add_argument(
        "--dir", type=str, help="Directory to serve files from", default="."
    )
    parser.add_argument("--port", type=int, help="Port to serve HTTP on", default=42069)
    args = parser.parse_args()

    run(port=args.port, directory=args.dir)
