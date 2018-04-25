# coding: utf-8
import logging
import uuid

from record.models import TelephoneChargesRecord

logger = logging.getLogger('django')


class TelephoneChargesCompute:
    @staticmethod
    def compute_telephone_charges(user_id, operation, charge, extra=None):
        record = TelephoneChargesRecord.objects.filter(user_id=user_id).latest('-create_at').first()
        balance = charge if not record else record.balance + charge
        TelephoneChargesRecord.objects.create(id=str(uuid.uuid4()), user_id=user_id, operation=operation,
                                              charge=charge, balance=balance, extra=extra)
