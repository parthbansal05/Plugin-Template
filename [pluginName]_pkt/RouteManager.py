import server_pkg.essentials as e

def initRoute(self):
    # layout
    @self.app.route("/pluginHome", methods=["GET"], strict_slashes=False)
    @e.fl.login_required
    def pluginHome():
        return e.render_template('/plugin_edpt/Home.html')

    @self.app.route("/pluginAdmin", methods=["GET"], strict_slashes=False)
    @e.admin_required
    def pluginAdminDashboard():
        return e.render_template("/plugin_edpt/Admin.html")
