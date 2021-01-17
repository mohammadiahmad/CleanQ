from django.urls import include, path

from .views import clinic,clinic_manager,patient

urlpatterns = [
    path('', clinic.home, name='home'),
    path('patient/', include(([
                                    path('', patient.ReservationListView.as_view(), name='reservation_list'),
                                    path('profile/', patient.Profile.as_view(), name='profile_detail'),
    #                                # path('interests/', students.StudentInterestsView.as_view(),
    #                                #      name='student_interests'),
    #                                # path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
    #                                # path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
                               ], 'clinic'), namespace='patient')),
    path('clinic-manger/', include(([
                                   path('', clinic_manager.ReservationListView.as_view(), name='reservation_list'),
                                   path('profile/', clinic_manager.Profile.as_view(), name='profile_detail'),
    #                                # path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
    #                                # path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
    #                                # path('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(),
    #                                #      name='quiz_results'),
    #                                # path('quiz/<int:pk>/question/add/', teachers.question_add, name='question_add'),
    #                                # path('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers.question_change,
    #                                #      name='question_change'),
    #                                # path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/',
    #                                #      teachers.QuestionDeleteView.as_view(), name='question_delete'),
                               ], 'clinic'), namespace='clinic_manager')),

]
