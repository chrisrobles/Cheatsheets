# HTTP Requests

> Hypertext Transfer Protocol
> > Structure requests and responses over the internet between servers and browsers

The internet is a web of resources (HTML, stylesheets, scripts, media files) hosted on different servers.

Your web browser requests servers for resources, and then displays the response. 

HTTP is the command language that both sides of a connection must follow in order to communicate. Without a standardized protocol, they wouldnt know how to talk to or listen to each other.


## TCP | Transfer

> Transmission Control Protocol
> > The transfer of resources

Manages the channels between the browser and the server

## The HTTP & TCP Process

1. You type an address into your browser (<http:/www.codecademy.com>)
2. Browser extracts the http to recognize the network protocol to use
3. Takes the domain name from the URL and asks the internet DNS (Domain Name Server) to return an IP (Internet Protocol)
4. Commands the browser to open a TCP channel to the server at the IP address using the network protocol
5. The client (web browser) sends a HTTP GET request to the server
    ```text
    GET / HTTP/1.1
    Host: www.codecademy.com
    
    // TypeOfRequest Path Protocol
    // Address of the server
    // (optional) extra data from browser
    ```
6. The server sends a response
   - HTTP HEADER
    ```text
    HTTP/1.1 200 OK
    Content-Type: text/html

    // ProtocolFromClient HTTPStatusCode
    // TypeOfContentSent
    // WebpageResources
    ```
   - The webpage resources (html, js css, etc.)
7. Server closes the TCP connection

## HTTP Methods

### GET

### POST

### PUT

### DELETE

## HTTPS

> HTTP Secure
> > Encrypt data sent and received

HTTP request can be read by anyone

So its not good for sensitive data

Up to the servers to support the HTTPS protocol. Servers need to apply for a certificate form a Certificate Authority