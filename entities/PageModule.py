class Page:
    def __init__(self, url):
        self.url = url

        self.hasTls = False
        self.loadingTime = float(0)
        self.hasAltRatio = float(0)
    #TODO check outboundLinks 200 ok and Ratio for scoring & PDF
        self.outboundLinks = []
        self.hasH1 = False
        self.hasMetaDescription = False
        self.imagesSizeRatio = float(0)
    #TODO !!!
        self.wordEfficiencyRatio = float(0)
        self.wordFrequencyRatio = float(0)

        self.boneUsCopyPasteAwareness = ""
        self.boneUsMobileFriendlyAccesibility = ""

    def __str__(self):
        return str(self.loadingTime)






