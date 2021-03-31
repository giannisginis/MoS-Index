from app.main.service.MOsIndex import MOsIndex

instance = MOsIndex.from_yaml("managed-object-index.yaml")


def test_attributes2datatype():
    att2type = instance.attributes2datatype()

    assert att2type["userLabel"]["datatype"] == "string"
    assert "BtsFunction" in att2type["userLabel"]["MoClasses"]


def test_datatype2attributes():
    type2att = instance.datatype2attributes()

    assert "release" in type2att["string"]["attributes"]


def test_class2attributes():
    class2att = instance.class2attributes()
    for l in class2att["BtsFunction"]:
        if l["attribute"] == ["btsFunctionId"]:
            assert class2att["BtsFunction"]["attribute"]["btsFunctionId"] == "string"
            assert class2att["BtsFunction"]["attribute"]["gsmMcpaIpmCapacity"] == "uint32"