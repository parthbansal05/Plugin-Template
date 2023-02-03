import server_pkg.essentials as e
from Plugins.PluginFiles.plugin import RouteManager

RouteManager.initRoute(self)


while(True):
    while(self.new == False):
        time.sleep(self.sleepTime)
    data = self.data
    self.new = False

    if data.target == "*":
        # a broadcast msg
        # follow Category format
        pass
    else:
        # a direct msg
        # follow HOOK format
        pass