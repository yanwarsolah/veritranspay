import unittest

from faker import Faker

from veritranspay.payment_types import CreditCard, Indomaret, VirtualAccountPermata, VirtualAccountBca, \
    VirtualAccountBni, VirtualAccountMandiri, BriEpay, MandiriClickpay, CimbClicks, BCAKlikPay, KlikBCA

fake = Faker()


class CreditCardTests(unittest.TestCase):

    def test_init(self):
        ''' Makes sure the expected attributes are required, and
        persisted as instance attributes.
        '''
        bank = fake.word()
        token_id = fake.word()

        cc = CreditCard(bank=bank, token_id=token_id)

        self.assertEqual(cc.bank, bank)
        self.assertEqual(cc.token_id, token_id)

    def test_serialization(self):
        bank = fake.word()
        token_id = fake.word()

        cc = CreditCard(bank=bank, token_id=token_id)

        serialized = cc.serialize()
        expected = {'payment_type': CreditCard.PAYMENT_TYPE_KEY,
                    CreditCard.PAYMENT_TYPE_KEY: {
                        'bank': bank,
                        'token_id': token_id,
                    }}

        self.assertEqual(serialized, expected)


class CStoreIndomaretTests(unittest.TestCase):

    def test_init(self):
        message = fake.word()

        indomrt = Indomaret(message=message)

        self.assertEqual(indomrt.store, 'Indomaret')
        self.assertEqual(indomrt.message, message)

    def test_serialization(self):
        message = fake.word()

        indomrt = Indomaret(message=message)

        expected = {
            'payment_type': 'cstore',
            'cstore': {
                'store': 'Indomaret',
                'message': message
            }
        }

        self.assertDictEqual(expected, indomrt.serialize())


class VirtualAccountPermataTests(unittest.TestCase):
    def test_init(self):
        permata = VirtualAccountPermata()
        self.assertEqual(permata.bank, 'permata')

    def test_serialization(self):
        permata = VirtualAccountPermata()

        expected = {
            'payment_type': 'bank_transfer',
            'bank_transfer': {
                'bank': 'permata'
            }
        }

        self.assertDictEqual(expected, permata.serialize())


class VirtualAccountBcaTests(unittest.TestCase):
    def test_init(self):
        bca = VirtualAccountBca()
        self.assertEqual(bca.bank, 'bca')

    def test_serialization(self):
        bca = VirtualAccountBca()

        expected = {
            'payment_type': 'bank_transfer',
            'bank_transfer': {
                'bank': 'bca'
            }
        }

        self.assertDictEqual(expected, bca.serialize())


class VirtualAccountBniTests(unittest.TestCase):
    def test_init(self):
        bni = VirtualAccountBni()
        self.assertEqual(bni.bank, 'bni')

    def test_serialization(self):
        bni = VirtualAccountBni()

        expected = {
            'payment_type': 'bank_transfer',
            'bank_transfer': {
                'bank': 'bni'
            }
        }

        self.assertDictEqual(expected, bni.serialize())


class VirtualAccountMandiriTests(unittest.TestCase):
    def test_init(self):
        mandiri = VirtualAccountMandiri(bill_info1='info1', bill_info2='info2')
        self.assertEqual(mandiri.bill_info1, 'info1')
        self.assertEqual(mandiri.bill_info2, 'info2')

    def test_serialization(self):
        mandiri = VirtualAccountMandiri(bill_info1='info1', bill_info2='info2')

        expected = {
            'payment_type': 'echannel',
            'echannel': {
                'bill_info1': "info1",
                'bill_info2': "info2",
            }
        }

        self.assertDictEqual(expected, mandiri.serialize())


class BriEpayTests(unittest.TestCase):
    def test_serialization(self):
        bri = BriEpay()

        expected = {
            'payment_type': 'bri_epay',
            'bri_epay': {
            }
        }

        self.assertDictEqual(expected, bri.serialize())


class BCAKliPayTest(unittest.TestCase):
    def test_serialization(self):
        bca_klikpay = BCAKlikPay(type_id=1, description="Pembelian Barang")

        expected = {
            'payment_type': 'bca_klikpay',
            'bca_klikpay': {
                'type': 1,
                'description': 'Pembelian Barang'
            }
        }

        self.assertDictEqual(expected, bca_klikpay.serialize())


class KlikBCATest(unittest.TestCase):

    def test_serialization(self):
        klik_bca = KlikBCA(user_id="midtrans1012", description="testing transaction")

        expected = {
            'payment_type': 'bca_klikbca',
            'bca_klikbca': {
                'description': 'testing transaction',
                'user_id': 'midtrans1012'
            }
        }

        self.assertDictEqual(expected, klik_bca.serialize())


class MandiriClickpayTest(unittest.TestCase):

    def test_serialization(self):
        data_init = {
            'card_number': '4111111111111111',
            'input1': '1111111111',
            'input2': '145000',
            'input3': '54321',
            'token': '000000'
        }

        mandiri_clickpay = MandiriClickpay(**data_init)

        expected = {
            'payment_type': 'mandiri_clickpay',
            'mandiri_clickpay': {
                'card_number': '4111111111111111',
                'input1': '1111111111',
                'input2': '145000',
                'input3': '54321',
                'token': '000000'
            }
        }

        self.assertDictEqual(expected, mandiri_clickpay.serialize())


class CimbClicksTest(unittest.TestCase):
    def test_serialization(self):
        cimb_clicks = CimbClicks(description='Purchase of a special event item')

        expected = {
            'payment_type': 'cimb_clicks',
            'cimb_clicks': {
                'description': 'Purchase of a special event item'
            }
        }

        self.assertDictEqual(expected, cimb_clicks.serialize())