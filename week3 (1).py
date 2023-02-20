class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)

    def __str__(self):
        return f"Kangaroo object with pouch contents: {self.pouch_contents}"

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch(roo)
print(kanga) 