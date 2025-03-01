from test.unit.cypherpunkpay.cypherpunkpay_test_case import CypherpunkpayTestCase
from cypherpunkpay.tools.pbkdf2 import PBKDF2


class PBKDF2Test(CypherpunkpayTestCase):

    def test_pass(self):
        pass

    # A smoke test only! Implementation relies on built in pbkdf2 library
    def test_hash(self):
        h = PBKDF2.hash('password123')

        # proper length
        self.assertEqual(len(h), 8 + 64 + 64)

        # million iterations
        MILLION_ITERATIONS = '00030d40'  # unsigned 4 bytes
        self.assertTrue(MILLION_ITERATIONS in h)

    # If this starts failing then maybe the default 12 rounds is no longer enough
    def test_hash_speed(self):
        import time
        start = time.time()
        PBKDF2.hash('password123')
        end = time.time()
        self.assertGreater(end-start, 0.05)

    # Based on https://bcrypt-generator.com/
    def test_password_is_correct(self):
        self.assertTrue(PBKDF2.password_is_correct('', PBKDF2.hash('')))
        self.assertTrue(PBKDF2.password_is_correct('password123', PBKDF2.hash('password123')))
        self.assertTrue(PBKDF2.password_is_correct('QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*(_+-={}|[];:,.<>', PBKDF2.hash('QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*(_+-={}|[];:,.<>')))
