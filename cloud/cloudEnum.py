import requests as req
import sys
import xml.etree.ElementTree as ET



class AmazonAws():

    def __init__(self):
        self.fullList=[]
        self.arrList=["dev","prod","staging"]
        self.filenames = []
        self.spaceExistsList = []
    def prepareFullList(self, name):
        # amazon cloud
        domain = ".s3.amazonaws.com"
        self.fullList.append(name + domain)
        for i in self.arrList:
            merged = i + "-" + name+domain
            self.fullList.append(merged)
            merged = name + "-" + i + domain
            self.fullList.append(merged)
            merged = name + i + domain
            self.fullList.append(merged)
            merged = i + name + domain
            self.fullList.append(merged)

        # google cloud
        domain = ".storage.googleapis.com"
        self.fullList.append(name + domain)
        for i in self.arrList:
            merged = i + "-" + name+domain
            self.fullList.append(merged)
            merged = name + "-" + i + domain
            self.fullList.append(merged)
            merged = name + i + domain
            self.fullList.append(merged)
            merged = i + name + domain
            self.fullList.append(merged)

        # digitalocean cloud
        regions = ["nyc1", "nyc3", "ams3", "sfo2", "sfo3", "sgp1", "lon1", "fra1", "tor1", "blr1", "syd1"]
        for region in regions:
            domain = "." + region + ".digitaloceanspaces.com"
            self.fullList.append(name + domain)
            for i in self.arrList:
                merged = i + "-" + name+domain
                self.fullList.append(merged)
                merged = name + "-" + i + domain
                self.fullList.append(merged)
                merged = name + i + domain
                self.fullList.append(merged)
                merged = i + name + domain
                self.fullList.append(merged)

    def enum(self, name):
        self.prepareFullList(name)
        for i in self.fullList:
            ret = self.askAws(i)
            if ret != False:
                self.parseResult(ret)

    def parseResult(self, xml_string):
        tree = ET.fromstring(xml_string)
        namespace = {'ns': tree.tag.split('}')[0].strip('{')}
        keys = tree.findall(".//ns:Key", namespace)
        for key in keys:
            self.filenames.append(self.currentName + "/" + key.text)

    def askAws(self,name):
        self.currentName = "https://" + name
        try:
            ret = req.get(self.currentName)
            if ret.status_code == 200:
                self.spaceExistsList.append(name)
                return ret.text
            elif ret.status_code == 403:
                self.spaceExistsList.append(name)
                return False
            else:
                return False
        except:
            return False

    def loadList(self):
        self.arrList=['access', 'admin', 'ai', 'alpha', 'america', 'analytics', 'ansible', 'apac', 'api', 'app', 'application', 'archive', 'archives', 'asia', 'asset', 'assets', 'assets-cache', 'audio', 'audit', 'auth', 'aws', 'backup', 'beta', 'bucket', 'build', 'business', 'cache', 'canada', 'cdn', 'cdn-cache', 'china', 'cloud', 'cluster', 'compliance', 'config', 'core', 'current', 'data', 'datasets', 'db', 'de', 'demo', 'dept', 'design', 'dev', 'developer', 'development', 'dns', 'docs', 'download', 'downloads', 'dump', 'emea', 'encrypted', 'engineering', 'eu', 'europe', 'ext', 'external', 'file', 'files', 'fileshare', 'finance', 'fr', 'general', 'group', 'historical', 'hotfix', 'hr', 'image', 'insights', 'integration', 'internal', 'iot', 'jp', 'lambda', 'latest', 'legacy', 'legal', 'local', 'logs', 'marketing', 'media', 'microservices', 'mirror', 'ml', 'module', 'my', 'net', 'new', 'nightly', 'northamerica', 'nosql', 'old', 'operations', 'patch', 'pipeline', 'pipelines', 'pl', 'previous', 'private', 'processed', 'prod', 'production', 'project', 'protected', 'proxy', 'public', 'public-read', 'public-write', 'qa', 'queue', 'raw', 'readonly', 'readwrite', 'region1', 'region2', 'release', 'reports', 'restricted', 'sales', 'sandbox', 'secure', 'service', 'session', 'share', 'snapshots', 'southamerica', 'sql', 'stage', 'staging', 'static', 'storage', 'support', 'sync', 'tables', 'team', 'temp', 'test', 'testing', 'transfer', 'uat', 'uk', 'upload', 'uploads', 'us', 'v1', 'v2', 'v3', 'v4', 'version1', 'version2', 'video', 'web', 'workflow']

    def showFiles(self, include):
        print("\n-------------------\nExisted files:")

        for i in self.filenames:
            if include in i:
                print(i)

    def showSpaces(self):
        print("\n-------------------\nExisted spaces:")
        for i in self.spaceExistsList:
            print(i)
AWS = AmazonAws()
#AWS.loadList()
AWS.enum(sys.argv[1])
if sys.argv[2]:
    include = sys.argv[2]
else:
    include = ""
AWS.showFiles(include)
AWS.showSpaces()





