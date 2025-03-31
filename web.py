from http.server import HTTPServer,BaseHTTPRequestHandler

content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lenovo ThinkPad E16 Specifications</title>
    <style>
        body {
            font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;
            background-color: rgb(244, 244, 249); 
            padding: 20px;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: rgb(255, 255, 255);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            border-radius: 12px;
        }
        .title {
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            color: rgb(13, 255, 0); 
            background-color: rgb(255, 255, 255);
            margin-bottom: 20px;
            padding: 15px;
            text-transform: uppercase;
            letter-spacing: 1px;
            border-radius: 8px; 
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }

        th, td {
            padding: 15px;
            font-size: 16px;
        }

        th {
            background-color: aqua; 
            color: rgb(255, 255, 255); 
            font-weight: bold;
            text-transform: uppercase;
            text-align: left;
        } 

        tr:hover {
            background-color: rgb(200, 240, 240); 
        }

        td {
            border-bottom: 1px solid rgb(200, 200, 200); 
            text-align: left;
        }
      
    </style>
</head>
<body>
    <div class="container">
        <div class="title">💻Lenovo ThinkPad E16 Specifications💻</div>
        <hr border="2" >
        <table>
                <tr>
                    <th st>Feature</th>
                    <th>Specification</th>
                </tr>
                <tr style="background-color: rgb(224, 255, 255);">
                    <td>Processor</td>
                    <td>Intel Core i5-1340P / AMD Ryzen 7 7730U</td>
                </tr>
                <tr style="background-color: rgb(240, 255, 255)">
                    <td>Display</td>
                    <td>16.0" WUXGA (1920 x 1200), IPS, Anti-Glare</td>
                </tr>
                <tr style="background-color: rgb(224, 255, 255);">
                    <td>Integrated Graphics</td>
                    <td>Intel Iris Xe / AMD Radeon Graphics</td>
                </tr>
                <tr style="background-color: rgb(240, 255, 255)">
                    <td>Discrete Graphics</td>
                    <td>Optional NVIDIA GeForce RTX 2050</td>
                </tr>
                <tr style="background-color: rgb(224, 255, 255);">
                    <td>Memory</td>
                    <td>Up to 32GB DDR4</td>
                </tr>
                <tr style="background-color: rgb(240, 255, 255)">
                    <td>Storage</td>
                    <td>Up to 1TB SSD</td>
                </tr>
                <tr style="background-color: rgb(224, 255, 255);">
                    <td>Operating System</td>
                    <td>Windows 11 Pro</td>
                </tr>
                <tr style="background-color: rgb(240, 255, 255)">
                    <td>Weight</td>
                    <td>Starting at 1.78kg (3.92 lbs)</td>
                </tr>
                <tr style="background-color: rgb(224, 255, 255);">
                    <td>Battery Life</td>
                    <td>Up to 10 hours </td>
                </tr>
                <tr style="background-color: rgb(240, 255, 255)">
                    <td>Ports</td>
                    <td>USB-C, USB 3.2, HDMI, Ethernet, Audio Jack</td>
                </tr>
        </table>
    </div>
</body>
</html>

'''


class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver")
server_address = ('',8000)
httpd = HTTPServer(server_address,Myserver)
httpd.serve_forever()
