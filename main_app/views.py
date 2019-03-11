from django.shortcuts import render
from django.http import HttpResponse

class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Pledge', 'Pitt-Mix', 'tripod', 9),
    Dog('Brooks', 'Boxer', 'floppy ears', 0),
    Dog('Swiffer', 'Greyhound ', 'very fast', 4)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Dogs, Dawgs!</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })