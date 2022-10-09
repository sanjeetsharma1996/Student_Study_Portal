from django.urls import path
from dashboard.views.home import home 
from dashboard.views.notes import notes, delete_note, NotesDetailView
from dashboard.views.homework import homework, update_homework,delete_homework
from dashboard.views.youtube import youtube
from dashboard.views.todo import todo, update_todo, delete_todo
from dashboard.views.books import books
from dashboard.views.dictionary import dictionary
from dashboard.views.wiki import wiki
from dashboard.views.conversion import conversion


urlpatterns = [
    path('',home, name = 'home'),
    path('home/',home, name = 'home'),

    path('notes/',notes, name = 'note'),
    path('delete_note/<int:pk>',delete_note, name= 'delete_note'),
    path('note_Detail/<int:pk>/',NotesDetailView.as_view(), name ='note_Detail'),
    # path('Note_List/',views.NotesListView.as_view(), name ='note_Detail'),

    path('homework/',homework, name = 'homework'),
    path('update_homework/<int:pk>/',update_homework, name = 'update_homework'),
    path('delete_homework/<int:pk>/',delete_homework, name = 'delete_homework'),


    path('youtube/',youtube, name = 'youtube'),

    path('todo/',todo, name = 'todo'),
    path('update_todo/<int:pk>',update_todo, name = 'update_todo'),
    path('delete_todo/<int:pk>',delete_todo, name = 'delete_todo'),


    path('books/',books, name = 'books'),


    path('dictionary/',dictionary, name = 'dictionary'),

    path('wiki/',wiki, name = 'wiki'),

    path('conversion/',conversion, name = 'conversion'),

]
