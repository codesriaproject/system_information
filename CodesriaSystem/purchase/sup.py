from purchase.models import *
from users.models import *





def get_invoice(id):

    invoice = Invoice.objects.get(id=id)
    # staff_instance = Staff.objects.get(admin_id=request.user)
    signature=Signature.objects.all()
    # validate = SecretaryValidate.objects.filter(staff_id=signature)


    articles = invoice.article_set.all()

    context = {
        'invoice': invoice,
        'articles': articles,
        'signature':signature,
        # 'validate':validate
    }

    return context