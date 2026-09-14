import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','restaurant.settings')
import django; django.setup()
from restaurant.core.models import MenuItem
items=[('چلو جوجه زعفرانی','جوجه گریل‌شده با برنج ایرانی و کره زعفرانی',245000,'main',True),('پیتزا مخصوص نارنج','سس مخصوص، پنیر کش‌دار، گوشت و سبزیجات تازه',315000,'pizza',True),('برگر نارنج','گوشت گریل‌شده، پنیر چدار و سس دست‌ساز',298000,'burger',True),('پاستا آلفردو','پاستا با سس خامه‌ای و مرغ گریل‌شده',275000,'main',False),('لیموناد تازه','لیموناد خانگی با لیموی تازه',95000,'drink',False),('چیزکیک شکلاتی','دسر شکلاتی نرم با سس مخصوص',145000,'dessert',False)]
for n,d,p,c,f in items: MenuItem.objects.get_or_create(name=n,defaults={'description':d,'price':p,'category':c,'featured':f})
print('Demo menu created.')
