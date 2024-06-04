import sys
import geocoder
import folium
import io
import codecs
import optparse
import time


# def getting_input():
#     object_parse = optparse.OptionParser()
#     object_parse.add_option("-i", "--ip", dest="ip", help="ip to change,if you want to search your ip, just type `me`")
#     return object_parse.parse_args()

def main(ip):
    # [user_input,arguements] = getting_input()

    try:

        g = geocoder.ip(ip) 

        myaddress = g.latlng
        time.sleep(1)
        
        print(myaddress)
        coords = ''
        for addr in myaddress:
            coords += str(addr)
        map = folium.Map(location=myaddress,zoom_start=3)
        folium.CircleMarker(location=myaddress,radius=50,popup="Yorkshire").add_to(map)

        folium.Marker(location=myaddress,popup="Yorkshire").add_to(map)
        data = io.BytesIO()
        map.save(data, close_file=False)

        return data, coords
    except:
        print("can not find the location of your IP!!!")
