class CreativeEntrepreneur:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        return f"I am {self.name}, a creative entrepreneur!"


class RawDesigner(CreativeEntrepreneur):
    def create_design(self):
        return f"{self.name} is crafting unique designs!"
class ContentStrategist(CreativeEntrepreneur):
    def brainstorm_content(self):
        return f"{self.name} is strategizing compelling content ideas!"

class TalesFromTheIslandsCreator(RawDesigner, ContentStrategist):
    def __init__(self, name, trending_topic):
        super().__init__(name)
        self.trending_topic = trending_topic
    def produce_reel(self):
        if self.trending_topic == "Conspiracy Theories":
            return f"{self.name} is creating a reel focused on gripping conspiracy theories!"
        elif self.trending_topic == "Motivational Stories":
            return f"{self.name} is crafting an inspiring reel with motivational stories!"
        else:
            return f"{self.name} is exploring a new creative direction!"

creator = TalesFromTheIslandsCreator("Anna", "Motivational Stories")
print(creator.introduce())
print(creator.create_design())
print(creator.brainstorm_content())
print(creator.produce_reel())
