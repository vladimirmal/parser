class Check(object):
    Values = {
        'title': {'max': 0, 'stop': 1},
        'keywords': {'max': 250, 'stop': 1},
        'description': {'max': 250, 'stop': 0},
        'h1': {'max': 50, 'stop': 1},
        'h2': {'max': 90, 'stop': 1}
    }

    def check(self, tag, value):
        length = self.Values[tag]['max']
        stop = self.Values[tag]['stop']
        if len(value) > length:
            #return str(len(value)) + '>' + str(length)
            return value

        elif stop is 1:

            if '!' in value or ',' in value or '.' in value:
                return 'Stop symvols'
        else:
            return self.Values[tag]['max']
