from django.contrib import admin
from django.urls import path, include
from studentorg.views import *

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", HomePageView.as_view(), name="home"),

    path("organization/", OrganizationList.as_view(), name="organization-list"),
    path("organization/add/", OrganizationCreateView.as_view(), name="organization-add"),
    path("organization/<pk>/", OrganizationUpdateView.as_view(), name="organization-update"),
    path("organization/<pk>/delete/", OrganizationDeleteView.as_view(), name="organization-delete"),

    path("orgmember/", OrgMemberList.as_view(), name="orgmember-list"),
    path("orgmember/add/", OrgMemberCreateView.as_view(), name="orgmember-add"),
    path("orgmember/<pk>/", OrgMemberUpdateView.as_view(), name="orgmember-update"),
    path("orgmember/<pk>/delete/", OrgMemberDeleteView.as_view(), name="orgmember-delete"),

    path("student/", StudentList.as_view(), name="student-list"),
    path("student/add/", StudentCreateView.as_view(), name="student-add"),
    path("student/<pk>/", StudentUpdateView.as_view(), name="student-update"),
    path("student/<pk>/delete/", StudentDeleteView.as_view(), name="student-delete"),

    path("college/", CollegeList.as_view(), name="college-list"),
    path("college/add/", CollegeCreateView.as_view(), name="college-add"),
    path("college/<pk>/", CollegeUpdateView.as_view(), name="college-update"),
    path("college/<pk>/delete/", CollegeDeleteView.as_view(), name="college-delete"),

    path("program/", ProgramList.as_view(), name="program-list"),
    path("program/add/", ProgramCreateView.as_view(), name="program-add"),
    path("program/<pk>/", ProgramUpdateView.as_view(), name="program-update"),
    path("program/<pk>/delete/", ProgramDeleteView.as_view(), name="program-delete"),

    path("accounts/", include("allauth.urls")),
]