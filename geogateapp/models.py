from __future__ import unicode_literals

import os
from django.db import models
from django.utils.text import slugify

HARVESTING_TYPE = (
    ('OGC:CSW', 'OGC Catalog Service for the Web'),
    ('OGC:WMS', 'OGC Web Map Server'),
    ('OGC:SOS', 'OGC Sensor Observation Service'),
)

class Catalog(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Catalog, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'{}'.format(self.name)


class Node(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    baseurl = models.URLField(blank=True, null=True)
    harvesting_url = models.URLField(blank=True, null=True)
    harvesting_type = models.CharField(
        max_length=10,
        choices=HARVESTING_TYPE
    )
    catalog = models.ForeignKey(Catalog)

    @property
    def local_csw_url(self):
        return os.path.join('http://geogate.sp7.irea.cnr.it', 
                            'catalog', 
                            self.catalog.name, 
                            'csw')

    @property
    def local_api_url(self):
        return os.path.join('http://geogate.sp7.irea.cnr.it', 
                            'catalog', 
                            self.catalog.name, 
                            'api')


        
