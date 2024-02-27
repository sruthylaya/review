from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import  TemplateView
from django.views.generic import ListView, DetailView
from .models import Review
from django.views.generic.edit import CreateView
# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context
    
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #    base_query = super().get_queryset()
    #    data = base_query.filter(rating__gt=4)
    #    return data

    
class SingleReviewView(DetailView):
    template_name = "Reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favourite_id = request.session.get("favourite_review")
        context["is_favourite"] = favourite_id == str(loaded_review.id)
        return context
            

class AddFavouriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session["favourite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)




    


           
    


       
        


        
    
    




    