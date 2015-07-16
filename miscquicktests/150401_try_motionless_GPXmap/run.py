from motionless import AddressMarker, LatLonMarker,DecoratedMap, CenterMap, VisibleMap
import xml.sax

class GPXHandler(xml.sax.handler.ContentHandler):
    
    def __init__(self,gmap):
        self.gmap = gmap
        self.first = True 
        self.prev = None

    def startElement(self, name, attrs):
        if name == 'trkpt': 
	    self.gmap.add_path_latlon(attrs['lat'],attrs['lon'])
            self.prev = (attrs['lat'],attrs['lon'])
            if self.first:
                self.first = False
                self.gmap.add_marker(LatLonMarker(attrs['lat'],attrs['lon'],color='green',label='S'))

    def endElement(self,name):
        if name == 'trk':
            self.gmap.add_marker(LatLonMarker(self.prev[0],self.prev[1],color='red',label='E'))
        
run = DecoratedMap(size_x=640,size_y=640,pathweight=8,pathcolor='blue')
parser = xml.sax.make_parser()
parser.setContentHandler(GPXHandler(run))
parser.feed(open('150328 Long run.gpx').read())

htmlPage = """
<html>
<body>
<h2>Run</h2>
<i>3/29/15 long run. 150328 Long run.gpx file from MotionX on my iphone.</i>
<p/>
<p/>
<img src="%s"/>
</body>
</html>	
""" % run.generate_url()


html = open("run.html","w")
html.write(htmlPage)
html.close()
print "run.html file created"