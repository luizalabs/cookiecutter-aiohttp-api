from .views import HealthCheckView, MonitorView


def register_routes(app):
    app.router.add_route('*', '/healthcheck/', HealthCheckView)
    app.router.add_route('*', '/monitor/', MonitorView)
