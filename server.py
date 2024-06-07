import os
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import requests

class CustomRequestHandler(SimpleHTTPRequestHandler):
    valheimIsOnline = False
    vrisingIsOnline = False
    enshroudedIsOnline = False
    palworldIsOnline = False

    # updating path flags when on local machine versus remote server
    debug = True

    try:
        if debug:
            IP_PATH = '/home/jpforbes/workspace/github.com/jpforbes5151/discordHooks/current_ip.txt'
        else:
            IP_PATH = '/home/jserver/workspace/discordHooks/current_ip.txt'
        with open(IP_PATH, 'r') as file:
            public_ip = file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found. check your path and permissions.")

    
 
    def do_GET(self):
        self.render_html_template()
        # starting valheim server
        if self.path == '/start_valheim/':  # Define the endpoint /run_script
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # running a specified script
            import subprocess
            subprocess.run(['sh', '/home/jserver/valheim_server/valheim_start.sh'])

            # Send a response to the client
            self.valheimIsOnline = True
            self.render_html_template()
            # kinda jank but makes a better looking response page
            self.wfile.write(b'''
                <html>
                <head>
                    <meta http-equiv="refresh" content="4;url=/serverlist/">
                    <link href="/index.css" rel="stylesheet">
                </head>
                <body>
                    <p>The Valheim Server is spinning up. Try to connect to the Server in ~2 minutes, as the container can take a short while to spin up.</p>
                    <br>       
                    <br>
                    <p>You will be redirected to the Containers page in ~3 seconds.</p> 
                    <br>        
                    <br>
                    <p>If the page doesn't automatically redirect, <a href="/serverlist/">click here</a>.</p>
                </body>
                </html>
            ''')

        elif self.path == '/start_vrising/':  # Define the endpoint /run_script
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # running a specified script
            import subprocess
            subprocess.run(['sh', '/home/jserver/vrising_server/vrising_start.sh'])

            # Send a response to the client
            self.vrisingIsOnline = True
            self.render_html_template()
            self.wfile.write(b'''
                <html>
                <head>
                    <meta http-equiv="refresh" content="4;url=/serverlist/">
                    <link href="/index.css" rel="stylesheet">
                </head>
                <body>
                    <p>The VRising Server is spinning up. Try to connect to the Server in ~2 minutes, as the container can take a short while to spin up.</p>
                    <br>       
                    <br>
                    <p>You will be redirected to the Containers page in ~3 seconds.</p> 
                    <br>        
                    <br>
                    <p>If the page doesn't automatically redirect, <a href="/serverlist/">click here</a>.</p>
                </body>
                </html>
            ''')   

        elif self.path == '/start_enshrouded/':  # Define the endpoint /run_script
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # running a specified script
            import subprocess
            subprocess.run(['sh', '/home/jserver/enshrouded_server/enshrouded_start.sh'])

            # Send a response to the client
            self.enshroudedIsOnline = True
            self.render_html_template()
            self.wfile.write(b'''
                <html>
                <head>
                    <meta http-equiv="refresh" content="4;url=/serverlist/">
                    <link href="/index.css" rel="stylesheet">
                </head>
                <body>
                    <p>The Enshrouded Server is spinning up. Try to connect to the Server in ~2 minutes, as the container can take a short while to spin up.</p>
                    <br>       
                    <br>
                    <p>You will be redirected to the Containers page in ~3 seconds.</p> 
                    <br>        
                    <br>
                    <p>If the page doesn't automatically redirect, <a href="/serverlist/">click here</a>.</p>
                </body>
                </html>
            ''')
        
        elif self.path == '/start_palworld/':  # Define the endpoint /run_script
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # running a specified script
            import subprocess
            subprocess.run(['sh', '/home/jserver/palworld_server/palworld_start.sh'])

            # Send a response to the client
            self.palworldIsOnline = True
            self.render_html_template()
            self.wfile.write(b'''
                <html>
                <head>
                    <meta http-equiv="refresh" content="4;url=/serverlist/">
                    <link href="/index.css" rel="stylesheet">
                </head>
                <body>
                    <p>The Palworld Server is spinning up. Try to connect to the Server in ~2 minutes, as the container can take a short while to spin up.</p>
                    <br>       
                    <br>
                    <p>You will be redirected to the Containers page in ~3 seconds.</p> 
                    <br>        
                    <br>
                    <p>If the page doesn't automatically redirect, <a href="/serverlist/">click here</a>.</p>
                </body>
                </html>
            ''')

        else:
            # If the requested path is not recognized, serve files as usual
            return super().do_GET()
    
    def render_html_template(self):
        if self.debug:
            html_file_path = '/home/jpforbes/workspace/github.com/jpforbes5151/homeServer/public/serverlist/index.html'
        else:
            html_file_path = '/home/jserver/workspace/homeServer/public/serverlist/index.html'
        # Read the HTML template file
        with open(html_file_path, 'r') as file:
            html_content = file.read()

        # This gets pretty gross, but I didn't want to make more logic to replace specific pieces
        replacements = {
            '<p><b> Valheim Server Status </b></p><p><div style="color: #bf0622; display: inline;">OFFLINE</div></p>': '<p><b> Valheim Server Status </b></p><p><div style="color: #276e0d; display: inline;"><b>ONLINE</b></div></p>' if self.valheimIsOnline else '<p><b> Valheim Server Status </b></p><p><div style="color: #bf0622; display: inline;">OFFLINE</div></p>',
            '<p><b> VRising Server Status </b></p><p><div style="color: #bf0622; display: inline;">OFFLINE</div></p>': '<p><b> VRising Server Status </b></p><p><div style="color: #276e0d; display: inline;"><b>ONLINE</b></div></p>' if self.vrisingIsOnline else '<p><b> VRising Server Status </b></p><p><div style="color: #bf0622; display: inline;">OFFLINE</div></p>',
            '<p><b> Enshrouded Server Status </b></p><p><div style="color: #bf0622; display: inline;">OFFLINE</div></p>': '<p><b> Enshrouded Server Status </b></p><p><div style="color: #276e0d; display: inline;"><b>ONLINE</b></div></p>' if self.enshroudedIsOnline else '<p><b> Enshrouded Server Status </b></p><p><div style="color: #bf0622; display: inline;">OFFLINE</div></p>',
            '<p><b> Palworld Server Status </b></p><p><div style="color: #bf0622; display: inline;">OFFLINE</div></p>': '<p><b> Palworld Server Status </b></p><p><div style="color: #276e0d; display: inline;"><b>ONLINE</b></div></p>' if self.palworldIsOnline else '<p><b> Palworld Server Status </b></p><p><div style="color: #bf0622; display: inline;">OFFLINE</div></p>',
            '{{ ip }}' : self.public_ip if self.public_ip else 'no public IP has been assigned'
        }

        # Perform the replacements in the HTML content
        for old_text, new_text in replacements.items():
            html_content = html_content.replace(old_text, new_text)

        # Write the modified HTML content back to the file
        with open(html_file_path, 'w') as file:
            file.write(html_content)


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
