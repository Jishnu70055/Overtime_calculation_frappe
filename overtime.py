from __future__ import unicode_literals
import frappe
from frappe import throw, _
from frappe.utils import cint, cstr, getdate, today
from frappe.utils.nestedset import NestedSet, get_ancestors_of, get_descendants_of
# from frappe.desk.doctype.attendance.attendance import Attendance
from erpnext.hr.doctype.attendance.attendance import Attendance
from frappe.utils import getdate, nowdate
from frappe import _
import urllib
from urllib.request import urlretrieve
from frappe.model.document import Document
from frappe.utils import cstr, get_datetime, formatdate
from datetime import datetime ,timedelta


def before_submit(doc, event):
    date_format = "%Y-%m-%d %H:%M:%S"
    start = datetime.strptime(doc.in_time_employee, date_format)
    end = datetime.strptime(doc.out_time_employee, date_format)
    time_delta = end - start
    # frappe.throw(frappe.time_delta)
    total_seconds = time_delta.total_seconds()
    minutes = total_seconds/60
    hours = int(total_seconds // 3600)
    working_minute = int(minutes % 60)
    ot_hour = int(hours - 8) 
    overtime = minutes - 480
    ot_minutes = int(overtime % 60)
    # frappe.throw(o)

    # frappe.throw(minutes)
    doc.total_work = str(hours) +":"+str(working_minute)
    if ot_hour < 0:
        doc.ot = 0
    else:
        doc.ot = str(ot_hour)+":"+str(ot_minutes)
    # doc.over_time_employee = k
    # doc.save()


