from django.contrib import admin
from django.urls import reverse
from .models import Block

class BlockAdmin(admin.ModelAdmin):
  list_display = (
    'timestamp',
    'previous_block', 
    'block_hash', 
    'action', 
    'data'
  )

admin.site.register(Block, BlockAdmin)
