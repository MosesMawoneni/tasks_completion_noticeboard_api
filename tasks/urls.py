# This code is setting up a router for creating API endpoints using the Django REST Framework.
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register("users",views.WorkerViewSet,basename="users")
router.register("tasks",views.TaskViewSet,basename="tasks")
urlpatterns = router.urls
