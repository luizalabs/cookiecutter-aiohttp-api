from .views import HealthCheckView


def register_routes(app):
    app.router.add_route('*', '/healthcheck/', HealthCheckView)
