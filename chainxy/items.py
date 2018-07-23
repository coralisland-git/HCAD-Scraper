# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ChainItem(Item):

	property_address = Field()

	propert_zip = Field()

	owner_name = Field()

	mailing_address = Field()

	mailing_city = Field()

	mailing_zip = Field()

	mailing_state = Field()

	phone_number = Field()

	phone_number2 = Field()

  