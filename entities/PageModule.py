class Page:
    def __init__(self, url):
        self.url = url

    hasTls = False
    loadingTime = float(0)
    hasAltRatio = float(0)
    #TODO check outboundLinks 200 ok and Ratio for scoring & PDF
    outboundLinks = []
    hasH1 = False
    hasMetaDescription = False
    imagesSizeRatio = float(0)
    #TODO !!!
    wordEfficiencyRatio = float(0)
    wordFrequencyRatio = float(0)

    boneUsCopyPasteAwareness = ""
    boneUsMobileFriendlyAccesibility = ""





