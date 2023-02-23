import server_pkg.stephen as s


@s.global_vars.app.route("/pluginHome", methods=["GET"], strict_slashes=False)
@s.login_required
def pluginHome():
    return s.render_template('/plugin_edpt/Home.html')

@s.global_vars.app.route("/pluginAdmin", methods=["GET"], strict_slashes=False)
@s.admin_required
def pluginAdminDashboard():
    return s.render_template("/plugin_edpt/Admin.html")
