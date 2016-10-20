from system.core.controller import *

class Maps(Controller):
    def __init__(self, action):
        super(Maps, self).__init__(action)

    def index(self):
        return self.load_view('index.html')

    def get_directions(self):
        origin = request.form['from']
        destination = request.form['to']
 # package the post data from our form into a dictionary
        data = {'origin':origin, 'destination':destination}
 # we then use the urlencode function to format our data to be passed through a query string
 # to the google maps api
        url = "https://maps.googleapis.com/maps/api/directions/json?"+urlencode(data)+"&sensor=false"
 # again we use the request.get function to send the request
        response = requests.get(url).content
 # we return the response to our client that sent the initial post request
        return response