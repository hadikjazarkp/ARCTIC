from django.contrib import admin
from django.contrib import messages
from .models import *

admin.site.register(SliderImage)

admin.site.register(ProductCard)

admin.site.register(Founder)

admin.site.register(SiteLogo)

admin.site.register(DisplayImage)
# Registering the Country model
admin.site.register(Country)

# Registering the Review model
admin.site.register(Review)

admin.site.register(AlertImage)

admin.site.register(ClassImage)

admin.site.register(HealthImage)

admin.site.register(HealthHeaderImage)

@admin.register(ShoeService)
class ShoeServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'image', 'description')
    search_fields = ('service_type',)
    list_per_page = 10
    
    
# Registering the TravelReview model with custom admin settings
@admin.register(TravelReview)
class TravelReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'location')  # Fields to display in the admin list view
    search_fields = ('name', 'job_title', 'location')  # Fields to search in the admin

# Registering the StudyReview model with custom admin settings
@admin.register(StudyReview)
class StudyReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')  # Fields to display in the admin list view
    search_fields = ('name', 'location')  # Fields to search in the admin

# Registering the MediaReview model with custom admin settings
@admin.register(MediaReview)
class MediaReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')  # Fields to display in the admin list view
    search_fields = ('name', 'location')  # Fields to search in the admin

# Registering the laundryReview model with custom admin settings
@admin.register(laundryReview)
class laundryReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')  # Fields to display in the admin list view
    search_fields = ('name', 'location')  # Fields to search in the admin

# Registering the healthReview model with custom admin settings
@admin.register(healthReview)
class healthReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')  # Fields to display in the admin list view
    search_fields = ('name', 'location')  # Fields to search in the admin

# Registering the Customer model with custom admin settings
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')  # Fields to display in the admin list view
    search_fields = ('full_name', 'email')  # Fields to search in the admin
    def save_model(self, request, obj, form, change):
        if not change:  # Only display the message on new registrations
            messages.add_message(request, messages.INFO, 'New customer registered!')
        super().save_model(request, obj, form, change)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')

# Optional: Register other models if not already registered
from .models import Country, Review, TravelReview, MediaReview, laundryReview, StudyReview


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('education_name', 'education_type')
    search_fields = ('education_name', 'education_type')

@admin.register(ContentBO)
class ContentBOAdmin(admin.ModelAdmin):
    list_display = ('heading', 'icon', 'online_text')
    
    
    
    
class ShoeCleaningServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'price')
    list_filter = ('service_type',)
    search_fields = ('service_type',)

admin.site.register(ShoeCleaningService, ShoeCleaningServiceAdmin)    
    
    
    
admin.site.register(Blog)    
  
admin.site.register(MediaContent)    
    
    
    
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'created_at']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'submitted_at']
    list_filter = ['question']    
    
    
    
    
    
    
    
    
    
    
    
    
    
# Username (leave blank to use 'hadik'): ARCTICADMIN
# Email address: ARCTIC@gmail.com
# Password: arctic12345