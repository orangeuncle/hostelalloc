from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
# from pyExcelerator import *
# from StringIO import StringIO
from .models import Hostel
from .models import Student

# def export_as_xls(modeladmin, request, queryset):
#     """
#     Generic xls export admin action.
#     """
#     if not request.user.is_staff:
#         raise PermissionDenied
#     opts = modeladmin.model._meta

#     wb = Workbook()
#     ws0 = wb.add_sheet('0')
#     col = 0
#     field_names = []
#     # write header row
#     for field in opts.fields:
#         ws0.write(0, col, field.name)
#         field_names.append(field.name)
#         col = col + 1

#     row = 1
#     # Write data rows
#     for obj in queryset:
#         col = 0
#         for field in field_names:
#             val = unicode(getattr(obj, field)).strip()
#             ws0.write(row, col, val)
#             col = col + 1
#         row = row + 1   

#     f = StringIO()
#     wb.save(f)
#     f.seek(0)
#     response = HttpResponse(f.read(), mimetype='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=%s.xls' % unicode(opts).replace('.', '_')
#     return response

# export_as_xls.short_description = "Export selected objects to XLS"


def showAllData(modeladmin, request, queryset):
    listData = {}
    n = 0
    for x in queryset:
        listData[n] = queryset[n]
        n += 1
    print("This is it: ", listData)
    # response = HttpResponse(request, '/playground.html', listData)
    response = render(request, 'blog/playground.html', listData)
    # response = HttpResponseRedirect('/playground/')
    return response

showAllData.short_description = "Show all hostel data"

# def resetRoomData(modeladmin, request, queryset):
#     # queryset.rooms = roomBaseCount
#     # queryset.room_size = roomBaseSize
#     # query.save()
#     return 0
# resetRoomData.short_description = "Restore to Default"




def totalNumberStudents():
    n = Student.objects.all()
    c = 0
    total = len(n)

    return total