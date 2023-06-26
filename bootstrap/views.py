from django.shortcuts import render

# Create your views here.

from django.http import request
from django.shortcuts import redirect, render
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import  View


# Create your views here.
class BootstrapView(LoginRequiredMixin, View):
    pass
#Elements   
bootstrap_alerts_view = BootstrapView.as_view( _name="bootstrap/alerts.html")
bootstrap_buttons_view = BootstrapView.as_view( _name="bootstrap/buttons.html")
bootstrap_cards_view = BootstrapView.as_view( _name="bootstrap/cards.html")
bootstrap_carousel_view = BootstrapView.as_view( _name="bootstrap/carousel.html")
bootstrap_dropdowns_view = BootstrapView.as_view( _name="bootstrap/dropdowns.html")
bootstrap_grid_view = BootstrapView.as_view( _name="bootstrap/grid.html")
bootstrap_images_view = BootstrapView.as_view( _name="bootstrap/images.html")
bootstrap_modals_view = BootstrapView.as_view( _name="bootstrap/modals.html")
bootstrap_offcanvas_view = BootstrapView.as_view( _name="bootstrap/offcanvas.html")
bootstrap_placeholder_view = BootstrapView.as_view( _name="bootstrap/placeholder.html")
bootstrap_placeholders_view = BootstrapView.as_view( _name="bootstrap/placeholders.html")
bootstrap_progressbars_view = BootstrapView.as_view( _name="bootstrap/progressbars.html")
bootstrap_tabs_view = BootstrapView.as_view( _name="bootstrap/tabs.html")
bootstrap_typography_view = BootstrapView.as_view( _name="bootstrap/typography.html")
bootstrap_video_view = BootstrapView.as_view( _name="bootstrap/video.html")
bootstrap_general_view = BootstrapView.as_view( _name="bootstrap/general.html")
bootstrap_colors_view = BootstrapView.as_view( _name="bootstrap/colors.html")