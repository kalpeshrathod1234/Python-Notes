class chai:
    size = 100

    def print_in_ml(self):
        return f"chai order in {self.size} ML"
    

cup1 = chai()
print(cup1.print_in_ml())


cup2 = chai()
cup2.size = 50
print(cup2.print_in_ml())