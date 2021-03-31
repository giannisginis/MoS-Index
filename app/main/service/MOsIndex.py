from app.main.utils.loader import load_metadata
import yaml


class MOsIndex:
    def __init__(self):
        self.metadata = load_metadata()
        self.att2type = {}
        self.type2att = {}
        self.class2att = {}

    @classmethod
    def from_yaml(cls, cfg):
        """Creates class instance from YAML"""
        with open(cfg, "r") as ymlfile:
            params = yaml.safe_load(ymlfile)
        cls().metadata = params
        return cls()

    def attributes2datatype(self):
        for j, mo_class in enumerate(self.metadata):
            for i in range(len(self.metadata[mo_class])):
                attribute, type = self.metadata[mo_class][i][0], self.metadata[mo_class][i][1]
                if attribute not in self.att2type:
                    self.att2type[attribute] = {"datatype": type, "MoClasses": [mo_class]}
                else:
                    self.att2type[attribute]["MoClasses"].append(mo_class)

        return self.att2type

    def datatype2attributes(self):

        for j, mo_class in enumerate(self.metadata):
            for i in range(len(self.metadata[mo_class])):
                att, type = self.metadata[mo_class][i][0], self.metadata[mo_class][i][1]
                if type not in self.type2att:
                    self.type2att[type] = {"attributes": [att]}
                else:
                    self.type2att[type]["attributes"].append(att)

        return self.type2att

    def class2attributes(self):
        for j, mo_class in enumerate(self.metadata.keys()):
            for i in range(len(self.metadata[mo_class])):
                att, type = self.metadata[mo_class][i][0], self.metadata[mo_class][i][1]
                if mo_class not in self.class2att:
                    self.class2att[mo_class] = [{"attribute": att, "type": type}]
                else:
                    self.class2att[mo_class].append({"attribute": att, "type": type})

        return self.class2att
