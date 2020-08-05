from application import Application as App

class Main:
    def __init__(self):
        self.app = App()

    def run(self):
        self.app.run()

if __name__=="__main__":
    main = Main()
    main.run()