from test.acceptance.cypherpunkpay.cypherpunkpay_app_test_case import CypherpunkpayAppTestCase


class RootViewTest(CypherpunkpayAppTestCase):

    def test_get_root(self):
        res = self.webapp.get('/cypherpunkpay/', status=302)
        self.assertTrue(res.location.endswith('/donations'))
