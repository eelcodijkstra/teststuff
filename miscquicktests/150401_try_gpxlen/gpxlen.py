#!/usr/bin/env python

# 4/1/15 - from https://github.com/pklaus/geocaching-tools

import sys
import math
import xml.dom.minidom

def getSegmentLength(segmentNode):
    t = 0.0
    oldLat = None
    oldLon = None

    for pt in segmentNode.getElementsByTagName("trkpt"):
        lat = float(pt.getAttribute("lat")) * math.pi/180.0
        lon = float(pt.getAttribute("lon")) * math.pi/180.0

        if oldLat != None:
            #t += math.acos(
            #    math.cos(lat) * math.cos(lon) * math.cos(oldLat) * math.cos(oldLon) +
            #    math.cos(lat) * math.sin(lon) * math.cos(oldLat) * math.sin(oldLon) +
            #    math.sin(lat) * math.sin(oldLat)
            #) * 6378100.0

            cosa = (math.sin(lat) * math.sin(oldLat) +
                math.cos(lat) * math.cos(oldLat) *
                math.cos(oldLon - lon))

            if cosa > 1.0: cosa = 1.0

            t += math.acos(cosa) * 6378100.0

        oldLat = lat
        oldLon = lon

    return t

def getTrackLength(trackNode):
    t = 0.0
    for seg in trackNode.getElementsByTagName("trkseg"):
        t = t + getSegmentLength(seg)

    return t

def main():
    import argparse

    parser = argparse.ArgumentParser(description='gpxloc calculates the length of each track in a GPX file')
    parser.add_argument('infilename', metavar='INPUTFILE', help='GPX file to analyze')
    args = parser.parse_args()

    dom = xml.dom.minidom.parse(args.infilename)
    gpxNode = dom.firstChild

    for track in gpxNode.getElementsByTagName("trk"):
        nameNode = track.getElementsByTagName("name")
        if nameNode != None:
            name = nameNode[0].firstChild.data
        else:
            name = "<no name>"

        sys.stdout.write("Track: %s, " % name)
        sys.stdout.write("length: %.3f\n" % getTrackLength(track))

    return 0

if __name__ == "__main__": sys.exit(main())
