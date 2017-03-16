import sys
from thredds_crawler.crawl import Crawl
from owslib.csw import CatalogueServiceWeb
from lxml import etree

def harvest_csw_base(src_url, dest_url, resourcetype='http://www.opengis.net/cat/csw/2.0.2'):
    src = CatalogueServiceWeb(src_url)
    dest = CatalogueServiceWeb(dest_url)
    dest.harvest(source=src_url, resourcetype=resourcetype)

def harvest_thredds(src_url, dest_url):
    c = Crawl(src_url)
    return c

def harvest_csw(src_url, dest_url):
    stop = 0
    flag = 0
    maxrecords = 10

    src = CatalogueServiceWeb(src_url)
    dest = CatalogueServiceWeb(dest_url)

    while stop == 0:
        if flag == 0:  # first run, start from 0
            startposition = 0
        else:  # subsequent run, startposition is now paged
            startposition = src.results['nextrecord']

        src.getrecords2(esn='full', startposition=startposition, maxrecords=maxrecords)
        
        print(src.results)

        if src.results['nextrecord'] == 0 \
           or src.results['returned'] == 0 \
           or src.results['nextrecord'] > src.results['matches']:  # end the loop, exhausted all records
            stop = 1
            break

        
        # harvest each record to destination CSW
        for i in list(src.records):
            print "insert", i
            src.getrecordbyid(id=[i], outputschema='http://www.isotc211.org/2005/gmd')
            md = src._exml.find('{http://www.isotc211.org/2005/gmd}MD_Metadata')
            f = open('/tmp/a.xml', 'w')
            f.write(etree.tostring(md))
            f.close()
            dest.transaction(ttype='insert', typename='gmd:MD_Metadata', record=open("/tmp/a.xml").read())

        flag = 1
