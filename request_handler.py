import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views.metal_requests import get_all_metals, get_single_metal, create_metal, update_metal
from views.order_requests import delete_order, get_all_orders, get_single_order, create_order, update_order
from views.size_requests import get_all_sizes, get_single_size, create_size
from views.style_requests import get_all_styles, get_single_style, create_style

# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple
    # Here's a class function
    # Here's a class function

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        """Handles GET requests to the server """
        self._set_headers(200)

        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        if resource == "metals":
            if id is not None:
                response = get_single_metal(id)

            else:
                response = get_all_metals()
        
        if resource == "styles":
            if id is not None:
                response = get_single_style(id)

            else:
                response = get_all_styles()

        if resource == "sizes":
            if id is not None:
                response = get_single_size(id)

            else:
                response = get_all_sizes()

        if resource == "orders":
            if id is not None:
                response = get_single_order(id)

            else:
                response = get_all_orders()

        self.wfile.write(json.dumps(response).encode())
        print(self.path)

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        response = None

        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        if resource == "metals":
            response = create_metal(post_body)

        # Encode the new animal and send in response

        # Add a new location to the list. Don't worry about
        # the orange squiggle, you'll define the create_location
        # function next.
        if resource == "orders":
            response = create_order(post_body)

        # Encode the new location and send in response

        # Add a new employee to the list. Don't worry about
        # the orange squiggle, you'll define the create_employee
        # function next.
        if resource == "size":
            response = create_size(post_body)

        if resource == "style":
            response = create_style(post_body)

        # Encode the new employee and send in response
        self.wfile.write(json.dumps(response).encode())
    # A method that handles any PUT request.
    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "metals":
            success = update_metal(id, post_body)
        # rest of the elif's

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_DELETE(self):
            # Set a 204 response code
            self._set_headers(204)

            # Parse the URL
            (resource, id) = self.parse_url(self.path)

            # Delete a single animal from the list
            if resource == "orders":
                delete_order(id)

            # Encode the new animal and send in response
            self.wfile.write("".encode())
# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
