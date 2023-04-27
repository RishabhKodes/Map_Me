import googlemaps
from datetime import datetime
from geocoder import get_coords
from geopy import Nominatim

gmaps = googlemaps.Client(key="MY_KEY")

def getStart(starting):
    geolocator = Nominatim(user_agent="GCP PROJECT NAME")
    location = geolocator.geocode(starting)
    coord01 = location.latitude
    coord02 = location.longitude
    coordFinal = str(coord01) + "," + str(coord02)

    print(coordFinal)
    return str(coordFinal)


def getDest(dest):
    geolocator = Nominatim(user_agent="GCP PROJECT NAME")
    location = geolocator.geocode(dest)
    coord03 = location.latitude
    coord04 = location.longitude

    coordFinal = str(coord03) + "," + str(coord04)

    print(coordFinal)
    return str(coordFinal)


def getDirections(start, dest):
    try:

      if start != dest:

        coords_0 = getStart(start)
        coords_1 = getDest(dest)

        # Init client
        # Request directions
        now = datetime.now()
        print(now)
        directions_result = gmaps.directions(coords_0, coords_1, mode="driving", departure_time=now, avoid='tolls')
        print(directions_result)

        legs = directions_result[0].get("legs")
        x = 0
        leg = legs[0]
        steps = leg.get('steps')
        final_string = ""

        for x in range (len(steps)-1):
            value = steps[x].get('html_instructions')
            distan = steps[x].get('distance')
            distan = distan.get('text')
            distan = str(distan)
            value = str(value.replace('<div style="font-size:0.9em">',''))
            value = str(value.replace('/<wbr/>',' '))
            value = str(value.replace('</div>',''))


            newvalue = value.replace("<b>", "")
            newvalue = newvalue.replace("</b>", "")
            newvalue = str(newvalue)
            firstword = newvalue[0:4]
            if firstword == "Head":
                final_string = final_string + str(x+1) + ". " + newvalue + " For " + distan + "\n"
            else:
              final_string = final_string + str(x+1) + ". " + "In " + str(distan) +" " +  str(newvalue) + "\n"

            x = x + 1

        y = len(steps)
        value = steps[x].get('html_instructions')
        distan = steps[x].get('distance')
        distan = distan.get('text')
        distan = str(distan)
        value = str(value.replace('<div style="font-size:0.9em">',''))
        value = str(value.replace('/<wbr/>',' '))
        value = str(value.replace('</div>',''))


        newvalue = value.replace("<b>", "").replace("</b>", "")
        newvalue = str(newvalue)
        firstword = newvalue[0:4]
        if firstword == "Head":
            final_string = final_string + str(y) + ". " + newvalue + " For " + distan + "\n"
        else:
            final_string = final_string + str(y) + ". " "In " + str(distan) +" " +  str(newvalue) + "\n"

        final_string = "\n" + final_string + "\n" + "You have arrived at your specified destination, thank you for using MapMe"

        return final_string

      else:
        return "You reached your destination"

    except:
      return "Unable to find Location, Please enter a Valid address( Full ) or a well known POI nearby to your location."