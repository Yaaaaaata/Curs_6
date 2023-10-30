from django.urls import path

from newsletter.views import ClientListView, HomeView, ClientCreateView, MessageCreateView, NewsletterCreateView, \
    NewsletterListView, MessageListView, LogListView, MessageDetailView, MessageDeleteView, MessageUpdateView, \
    NewsletterDetailView, NewsletterDeleteView, ClientDeleteView, ClientDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('client_form/', ClientCreateView.as_view(), name='client_form'),
    path('message_form/', MessageCreateView.as_view(), name='message_form'),
    path('newsletter_form/', NewsletterCreateView.as_view(), name='newsletter_form'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_confirm_delete'),
    path('client/detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('newsletter_list/', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletter_detail/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('newsletter_confirm_delete/<int:pk>/', NewsletterDeleteView.as_view(), name='newsletter_confirm_delete'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_confirm_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_confirm_delete'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('log_list/', LogListView.as_view(), name='log_list'),
    ]
