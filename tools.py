from numpy import array, sqrt, sum, power

def vector(p1, p2, key):
    magnitude = sqrt( sum( power(p1.features[key] - p2.features[key],2) )  )

    hat = (p1.features[key] - p2.features[key])/magnitude

    return magnitude, hat
