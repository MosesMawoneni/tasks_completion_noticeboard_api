from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register("tasks",views.TaskViewSet,basename="tasks")
urlpatterns = router.urls
