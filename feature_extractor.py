import re
import urllib.parse

def extract_features(url):

    features = []

    features.append(len(url))
    features.append(url.count("-"))
    features.append(url.count("."))
    features.append(url.count("/"))
    features.append(1 if "https" in url else 0)
    features.append(1 if "@" in url else 0)

    return features