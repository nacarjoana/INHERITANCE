class ContentCreator:
    def __init__(self, name, followers):
        self.name = name
        self.followers = followers

    def createPost(self):
        if self.followers < 1000:
            print(f"{self.name} posted something! Gaining traction!")
        else:
            print(f"{self.name} posted something! The audience loves it!")


class Tiktoker(ContentCreator):
    def __init__(self, name, followers, niche):
        super().__init__(name, followers)  
        self.niche = niche

    def recordVideo(self):
        print(f"{self.name} is recording a new {self.niche} TikTok video!")


creator1 = ContentCreator("joana", 100)
creator1.createPost()

tiktoker1 = Tiktoker("trishia", 1000, "dance")
tiktoker1.createPost()
tiktoker1.recordVideo()