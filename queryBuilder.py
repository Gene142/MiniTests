# userange == 0,1,2,3 as in GetRatingFilter or GetDateFilter
# also in and notin are determined by number of userange == 4 and 5
class GetIdFilter:
    def __init__(self):
        self.filterid = None

    def build_filter(self, userange, first_id=None, second_id=None):
        if userange == 0:
            self.filterid = "(id = " + first_id + ")"
        elif userange == 1:
            self.filterid = "(id < " + first_id + ")"
        elif userange == 2:
            self.filterid = "(id > " + first_id + ")"
        elif userange == 3:
            self.filterid = "(" + first_id + " < id < " + second_id + ")"
        elif userange == 4:
            self.filterid = "(id in list)"
        elif userange == 5:
            self.filterid = "(id notin list)"
        else:
            self.filterid = None  # error handling


# userange == 0 for equal to, == 1 for <, == 2 for >, == 3 for < rating <
class GetRatingFilter:
    def __init__(self):
        self.filterrating = None

    def build_filter(self, userange, first_rating, second_rating=None):
        if userange == 0:
            self.filterrating = "(rating = " + first_rating + ")"
        else:
            if userange == 1:
                self.filterrating = "(rating < " +first_rating + ")"
            else:
                if userange == 2:
                    self.filterrating = "(rating > " + first_rating + ")"
                else:
                    if userange == 3 and second_rating is not None:
                        self.filterrating =  "(" + first_rating + " < rating < " + second_rating + ")"
                    else:
                        self.filterrating = None  # (human) error handling goes here


# if no parameter, then the url filter is not enabled
class GetUrlFilter:
    def __init__(self):
        self.filterurl = None
    def build_query(self, filter):
        if filter is None:
            return
        else:
            self.filterurl = "(" + "url = " + filter + ")"


class GetDateFilter:
    def __init__(self):
        self.filterdate = None

    def build_filter(self, userange, first_date, second_date=None):
        if userange == 0:
            self.filterdate = "(date = " + first_date + ")"
        else:
            if userange == 1:
                self.filterdate = "(date <" + first_date + ")"
            else:
                if userange == 2:
                    self.filterdate = "(date >" + first_date + ")"
                else:
                    if userange == 3 and second_date is not None:
                        self.filterdate = "(" + first_date + " < date < " + second_date + ")"
                    else:
                        self.filterdate = None  # (human) error handling goes here


class QueryBuilder:
    def __init__(self):
        self.date_filter = GetDateFilter()
        self.url_filter = GetUrlFilter()
        self.rating_filter = GetRatingFilter()
        self.id_filter = GetIdFilter()
        self.output = ""

    def output_query(self):
        if self.date_filter.filterdate is not None:
            self.output = self.output + self.date_filter.filterdate
        if self.rating_filter.filterrating is not None:
            if self.output is not None:
                self.output = self.output + " and " + self.rating_filter.filterrating
            else:
                self.output = self.rating_filter.filterrating
        if self.id_filter.filterid is not None:
            if self.output is not None:
                self.output = self.output + " and " + self.id_filter.filterid
            else:
                self.output = self.id_filter.filterid
        if self.url_filter.filterurl is not None:
            if self.output is not None:
                self.output = self.output + " and " + self.url_filter.filterurl
            else:
                self.output = self.url_filter
        print self.output


QB = QueryBuilder()
QB.date_filter.build_filter(0, "1 Jan 2016")
QB.id_filter.build_filter(5)
QB.rating_filter.build_filter(2, "45")
QB.output_query()





