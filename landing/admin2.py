from django.contrib import admin
from .admin1 import SingletonAdmin
from .models2 import (
    WorkStep, StatItem, AdvantageItem, AdvantagesSection,
    ServicesSection, ContactSection, LeadSubmission, LeadInProgress
)


@admin.register(WorkStep)
class WorkStepAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'is_highlighted', 'order')
    list_editable = ('order', 'is_highlighted')
    ordering = ('order',)


@admin.register(StatItem)
class StatItemAdmin(admin.ModelAdmin):
    list_display = ('value', 'label', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(AdvantageItem)
class AdvantageItemAdmin(admin.ModelAdmin):
    list_display = ('icon_key', 'title', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(AdvantagesSection)
class AdvantagesSectionAdmin(SingletonAdmin):
    fieldsets = (
        ('Секція «Переваги»', {
            'fields': ('title', 'subtitle', 'footer_quote'),
        }),
    )


@admin.register(ServicesSection)
class ServicesSectionAdmin(SingletonAdmin):
    fieldsets = (
        ('Секція «Послуги»', {
            'fields': ('title', 'steps_title'),
        }),
    )


@admin.register(ContactSection)
class ContactSectionAdmin(SingletonAdmin):
    fieldsets = (
        ('Секція «Контакти»', {
            'fields': ('title', 'description', 'form_title', 'form_btn_text', 'privacy_note'),
        }),
    )


@admin.register(LeadSubmission)
class LeadSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'interest', 'status', 'created_at')
    list_filter = ('interest', 'status')
    list_editable = ('status',)
    search_fields = ('name', 'phone', 'comment')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(status__in=[
            LeadSubmission.STATUS_NEW,
            LeadSubmission.STATUS_NO_ANSWER,
            LeadSubmission.STATUS_CALL_BACK,
            LeadSubmission.STATUS_THINKING,
            LeadSubmission.STATUS_PUSH,
            LeadSubmission.STATUS_WAITING_PAYMENT,
        ])


@admin.register(LeadInProgress)
class LeadInProgressAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'interest', 'status', 'comment', 'created_at')
    list_filter = ('interest', 'status')
    list_editable = ('status', 'comment')
    search_fields = ('name', 'phone', 'comment')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(status__in=[
            LeadSubmission.STATUS_DATA_COLLECTION,
            LeadSubmission.STATUS_IN_PROCESS,
            LeadSubmission.STATUS_CLOSED,
            LeadSubmission.STATUS_OFFER_NEW,
        ])
