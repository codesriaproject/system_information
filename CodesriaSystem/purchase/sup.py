from purchase.models import *




def get_invoice(id):

    invoice = Invoice.objects.get(id=id)

    articles = invoice.article_set.all()

    context = {
        'invoice': invoice,
        'articles': articles
    }

    return context