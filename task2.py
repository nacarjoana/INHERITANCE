class GraphicDesigner:
    def __init__(self, name):
        self.name = name

    def designLogo(self):
        print(f"{self.name} is designing a stunning logo!")
class WebDeveloper:
    def __init__(self, name):
        self.name = name

    def buildWebsite(self):
        print(f"{self.name} is building a responsive website!")

class DigitalSolutionsProvider(GraphicDesigner, WebDeveloper):
    def __init__(self, name):
        GraphicDesigner.__init__(self, name)
        WebDeveloper.__init__(self, name)

    def deliverProject(self):
        print(f"{self.name} is delivering a full digital solution:")
        self.designLogo()
        self.buildWebsite()


provider = DigitalSolutionsProvider("joana")
provider.deliverProject()
      