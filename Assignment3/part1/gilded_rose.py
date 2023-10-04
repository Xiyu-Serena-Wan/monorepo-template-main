# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items


    def update_quality(self):
        for item in self.items:
            self.handle_quality(item)

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                self.handle_quality_sell_in(item)

    def handle_quality_sell_in(self, item):
        if item.name == "Aged Brie":
            self.increase_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item.quality = 0
        elif item.quality > 0:
            self.decrease_quality_not_sulf(item)

    def handle_quality(self, item):
        if item.name == "Aged Brie":
            self.increase_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.increase_quality_backstage(item)
        elif item.quality > 0:
            self.decrease_quality_not_sulf(item)

    def increase_quality_backstage(self, item):
        self.increase_quality(item)
        if item.sell_in < 11:
            self.increase_quality(item)
        if item.sell_in < 6:
            self.increase_quality(item)

    def decrease_quality_not_sulf(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.quality = item.quality - 1

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def get_item_sell_in(self, item):
        return item.sell_in

    def get_item_quality(self, item):
        return item.quality
