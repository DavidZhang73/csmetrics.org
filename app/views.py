from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django import template
from django.contrib import messages
from operator import itemgetter
from .utils import *

TITLE = "Institutional Publication Metrics for Computer Science"
labels = {
    "title": TITLE,
    "label_year": "Year",
    "label_category": "Category",
    "label_venueweight": "Venue Weight",
    "label_venuelist": "Venue List",
    "slider_desc": "Year of publication",
    "forward": "Predicted",
    "forward_tooltip": "The prediction metric counts papers in the year range.",
    "backward": "Measured",
    "backward_tooltip": "The measured metric uses citation counts and includes all citations at anytime to papers published in the year range.",
    "ctable_label_0": "Abbr.",
    "ctable_label_1": "Type",
    "ctable_label_2": "Fullname",
    "ctable_label_3": "Weight",
    "weight_option_tooltip": "A venue weight of one values all venues equally. The geometric mean venue weight assigns each venue the geometric mean of citations to papers.",
    "select_weight_option_equal": "Equal",
    "select_weight_option_geo": "Geo Mean",
    "rank_button": "Go",
    "select_inst_types": ["All", "Education", "Company", "Government", "Facility", "Nonprofit", "Healthcare", "Archive", "Other"],
    "select_inst_regions": ContinentOrdered,
    "msg_empty_table": "Calculating the Ranking...",
    "rtable_label_0": "Rank",
    "rtable_label_1": "Institution",
    "rtable_label_2": "Measured",
    "rtable_label_3": "Predicted",
    "rtable_label_4": "Combined",
}

@csrf_exempt
def updateTable(request): # /update
    pub_s = int(request.POST.get("pub_syear"))
    pub_e = int(request.POST.get("pub_eyear"))
    cit_s = int(request.POST.get("cit_syear"))
    cit_e = int(request.POST.get("cit_eyear"))
    weight = request.POST.get("weight")
    conflist = request.POST.get("conflist")
    # print(conflist.split(','), [pub_s, pub_e], [cit_s, cit_e], weight)
    data = getPaperScore(conflist.split(','), [pub_s, pub_e], [cit_s, cit_e], weight!="equal")
    return JsonResponse(data, safe=False)


@csrf_exempt
def selectKeyword(request): # /select
    keywords = request.POST.get("keyword")
    # print(keywords)
    sorted_conf = getVenueListFromKeywords(keywords.split(','))
    return JsonResponse(sorted_conf, safe=False)


def getVenueListFromKeywords(keywords):
    conf = getVenueList(keywords)
    sorted_conf = sorted(conf, key=lambda s: s[0].lower(), reverse=False)
    return sorted_conf


register = template.Library()
@register.simple_tag
def openMDDocs(request, html, alt_link, alt_title):
    try:
        template.loader.get_template(html)
        return render(request, "doc.html", {"exist":True,
            "template":html, "words":{"title":TITLE}})
    except template.TemplateDoesNotExist:
        return render(request, "doc.html", {"exist":False,
            "alt_link":alt_link, "alt_title":alt_title, "words":{"title":TITLE}})


def overview(request):
    return openMDDocs(request, "overview_generated.html",
        "https://github.com/csmetrics/csmetrics.org/blob/master/docs/Overview.md",
        "motivation and methodology")

def acks(request):
    return openMDDocs(request, "acks_generated.html",
        "https://github.com/csmetrics/csmetrics.org/blob/master/docs/Acks.md",
        "Acknowledgements")

def faq(request):
    return openMDDocs(request, "faq_generated.html",
        "https://github.com/csmetrics/csmetrics.org/blob/master/docs/FAQ.md",
        "FAQ")


def shareable(request):
    loadData()
    tags = createCategoryCloud()
    yearRange = [2007, 2020]
    try:
        pub = request.GET.get("pub").split(",")
        cit = request.GET.get("cit").split(",")
        weight = request.GET.get("weight")
        alpha = request.GET.get("alpha")
        keywords = request.GET.get("keywords")
        conflist = request.GET.get("venues")

        pub_s = int(pub[0])
        pub_e = int(pub[1])
        cit_s = int(cit[0])
        cit_e = int(cit[1])
        values = {
            "yearRange": yearRange,
            "pubYears": [max(yearRange[0], pub_s), min(yearRange[1], pub_e)],
            "citYears": [max(yearRange[0], cit_s), min(yearRange[1], cit_e)],
            "lockedState": str(pub_s-1 == cit_e),
            "weight": weight,
            "alpha": alpha,
            "keywords": keywords.split(',') if keywords != '' else [],
            "venues": conflist.split(',') if conflist != '' else [],
        }
        print(values)

        messages.info(request, "Ranking generated from sharable link.")
        return render(request, "main.html", {
            "default": values,
            "words": labels,
            "tags": tags
        })

    except Exception as e:
        messages.error(request, "Invalid link. Return to default settings.")
        return render(request, "main.html", {
            "default": {
                "yearRange": yearRange,
                "pubYears": [2018, 2020],
                "citYears": [2007, 2017],
                "lockedState": "True",
                "weight": "geomean", # or equal
                "alpha": str(0.3),
                "keywords": tags,
                "venues": [t[0] for t in getVenueListFromKeywords(tags)],
            },
            "words": labels,
            "tags": tags
        })

def main(request):
    loadData()
    tags = createCategoryCloud()
    yearRange = [2007, 2020]
    defaultValues = {
        "yearRange": yearRange,
        "pubYears": [2018, 2020],
        "citYears": [2007, 2017],
        "lockedState": "True",
        "weight": "geomean", # or equal
        "alpha": str(0.3),
        "keywords": tags,
        "venues": [t[0] for t in getVenueListFromKeywords(tags)],
    }
    return render(request, "main.html", {
        "default": defaultValues,
        "words": labels,
        "tags": tags
    })
