from django.contrib import admin
from django.urls import path
from GulleApp.views import (Login, Logout,likeMessage, Signup, no_access, professors_list, message_professor, thankyou, dashboard)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', professors_list, name='home'),
    path('sendmessage/<int:professor_id>/', message_professor, name="send-message"),
    path('<int:professor_id>/thankyou/', thankyou, name="thank-you"),

    path('dashboard/', dashboard, name="dashboard"),
    path('message/<int:id>/like/', likeMessage, name="like"),


    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    # path('messages/',messages ,name='messages'),

    path('noaccess/',no_access ,name='no-access'),


    # path('like/<int:user_id>/', like, name='like'),
    # path('liked/',liked ,name='liked'),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
