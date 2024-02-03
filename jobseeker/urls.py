from django.urls import path
from jobseeker.views import EducationView,SkillView,ExperienceView
urlpatterns=[
  path('education/',EducationView.as_view(),name='education'),
  path('education/<int:id>/',EducationView.as_view(),name='education'),
  path('skill/',SkillView.as_view(),name='skill'),
  path('skill/<int:id>/',SkillView.as_view(),name='skill'),
  path('experience/',ExperienceView.as_view(),name='experience'),
  path('experience/<int:id>/',ExperienceView.as_view(),name='experience'),
]