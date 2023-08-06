from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register("users",views.WorkerViewSet,basename="users")
router.register("tasks",views.TaskViewSet,basename="tasks")
urlpatterns = router.urls
