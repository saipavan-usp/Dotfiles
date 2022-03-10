from libqtile.command.client import InteractiveCommandClient

c = InteractiveCommandClient()
print(str(c.layout.info()["name"]).title())