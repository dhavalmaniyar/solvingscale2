from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
class StaticViewSitemapIndex(Sitemap):
    changefreq = "weekly"
    priority = 1.0
    def items(self):
        return ['index']
    def location(self, item):
        return reverse(item)
class StaticViewSitemapConsulting(Sitemap):
    changefreq = "weekly"
    priority = 1.0 
    def items(self):
        return ['consulting']
    def location(self, item):
        return reverse(item)

class StaticViewSitemapTeam(Sitemap):
    changefreq = "weekly"
    priority = 0.5 
    def items(self):
        return ['team']
    def location(self, item):
        return reverse(item)

class StaticViewSitemapCareer(Sitemap):
    changefreq = "weekly"
    priority = 0.5 
    def items(self):
        return ['portfolio']
    def location(self, item):
        return reverse(item)

class StaticViewSitemapContact(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    def items(self):
        return ['contact']
    def location(self, item):
        return reverse(item)

class StaticViewSitemapCompany(Sitemap):
    changefreq = "weekly"
    priority = 1.0
    def items(self):
        return ['company']
    def location(self, item):
        return reverse(item)
