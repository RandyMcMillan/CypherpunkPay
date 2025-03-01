from cypherpunkpay import bitcoin

from test.unit.cypherpunkpay.cypherpunkpay_test_case import CypherpunkpayTestCase


class Bip32Test(CypherpunkpayTestCase):

    # Electrum mainnet P2WPKH seed words (no funds here):
    # file title fault retire nuclear alone kidney eternal error weekend canvas weird
    VALID_XPUB = 'xpub69JaX1RKMyHuoZSasFS7kvYZ8aoTFAjKzUpwr4aN9oRbTWohd6ZKuaSbqZ6PZz1bMkYJ77CHUJoFX6bvZzdLfpmWdD9E9ZMKuqpzeFxeKq2'
    VALID_ZPUB = 'zpub6ny78Lm9fLNsW9ppXy1NB6jZUX6M8QiKphsPQrN8upBMZiSA8QtT9hkssy1ZZoKSB2muc4PQPdWMHfq41PTNGJ8iMtY5KNzJTHxHRKvNMUf'

    # Electrum testnet P2WPKH seed words:
    # where about donkey cricket vacuum share jump cube filter idle shiver what
    VALID_VPUB = 'vpub5VpqsnbyXKZjcgWoTj8YThxGXMxFDnWo7AvCqBAsJhbgn5eRfT64uzXWAcfx1GGDTovhG9hN7uNVVedqjiyQ4XNctZM1q7PvfkHJ82PPKaY'
    VALID_TPUB = 'tpubD9s11MmVXxc9b55tadgt5oUeCRLo6QzrV2YwkX1nQd7LdZwbEzGHJZWcT4fuXaXJ4zhDNgQMaKudxQMaZyefYSC7gqVAgTh8o9zzf9UwhuQ'

    VALID_PATH = [0, 0]

    # p2wpkh_address_at

    def test_p2wpkh_address_at__invalid_network(self):
        with self.assertRaises(Exception):
            bitcoin.Bip32.p2wpkh_address_at('invalid network', self.VALID_ZPUB, self.VALID_PATH)

    def test_p2wpkh_address_at__invalid_xpub(self):
        with self.assertRaises(Exception):
            bitcoin.Bip32.p2wpkh_address_at('mainnet', 'invalid xpub', self.VALID_PATH)

    def test_p2wpkh_address_at__invalid_path(self):
        with self.assertRaises(Exception):
            bitcoin.Bip32.p2wpkh_address_at('mainnet', self.VALID_ZPUB, [0, -1])

    def test_p2wpkh_address_at__mainnet_account_0__derives_correct_receiving_address(self):
        receiving_address_0 = bitcoin.Bip32.p2wpkh_address_at('mainnet', self.VALID_ZPUB, [0, 0])
        self.assertEqual('bc1q4je2vdd5m3mffssjx2quza630f5k54cftmvktk', receiving_address_0)

        receiving_address_1 = bitcoin.Bip32.p2wpkh_address_at('mainnet', self.VALID_ZPUB, [0, 1])
        self.assertEqual('bc1qpwd06w4hfk7qasvce203jc2pshqrqkhg3chx9d', receiving_address_1)

        receiving_address_19 = bitcoin.Bip32.p2wpkh_address_at('mainnet', self.VALID_ZPUB, [0, 19])
        self.assertEqual('bc1qeuu8nqfth2as5hm39hpzezes55gy8mrz79zejt', receiving_address_19)

    def test_p2wpkh_address_at__mainnet_account_0__derives_correct_change_address(self):
        change_address_0 = bitcoin.Bip32.p2wpkh_address_at('mainnet', self.VALID_ZPUB, [1, 0])
        self.assertEqual('bc1qna9udmzvykpjln8d89tx4hzthvexln7p2v9ewx', change_address_0)

        change_address_1 = bitcoin.Bip32.p2wpkh_address_at('mainnet', self.VALID_ZPUB, [1, 1])
        self.assertEqual('bc1qe05x4hjcef88d0yjqe60dlpyye9kdnuvh6k2ag', change_address_1)

        change_address_9 = bitcoin.Bip32.p2wpkh_address_at('mainnet', self.VALID_ZPUB, [1, 9])
        self.assertEqual('bc1qdnrdwtx74yke86rj3zf5eq4e5c4rya6zp5ek2z', change_address_9)

    def test_p2wpkh_address_at__testnet_account_0__derives_correct_receiving_address(self):
        receiving_address_0 = bitcoin.Bip32.p2wpkh_address_at('testnet', self.VALID_VPUB, [0, 0])
        self.assertEqual('tb1qwm3y963a5vwudsfunzgsev4ms9n06vq5a5tglv', receiving_address_0)

        receiving_address_1 = bitcoin.Bip32.p2wpkh_address_at('testnet', self.VALID_VPUB, [0, 1])
        self.assertEqual('tb1qggypq3g9zl0fd2qtsh6eeek34vetc09kvc5g3y', receiving_address_1)

        receiving_address_19 = bitcoin.Bip32.p2wpkh_address_at('testnet', self.VALID_VPUB, [0, 19])
        self.assertEqual('tb1qurfecuwm5668lm29lxta8a9uymdhwx0h2t08zp', receiving_address_19)

    def test_p2wpkh_address_at__testnet_account_0__derives_correct_change_address(self):
        receiving_address_0 = bitcoin.Bip32.p2wpkh_address_at('testnet', self.VALID_VPUB, [1, 0])
        self.assertEqual('tb1qngws7lh305h7cu5whv9tsmzqq3wzpej9vpmzk3', receiving_address_0)

        receiving_address_1 = bitcoin.Bip32.p2wpkh_address_at('testnet', self.VALID_VPUB, [1, 1])
        self.assertEqual('tb1qg60e4594ksmav4wqclrc8uuf80r57d8v6uvqqr', receiving_address_1)

        receiving_address_9 = bitcoin.Bip32.p2wpkh_address_at('testnet', self.VALID_VPUB, [1, 9])
        self.assertEqual('tb1qvdg3eh25dnwm25mynmrdw2mm7umauleu0uktkl', receiving_address_9)

    # validate_xpub

    def test_validate_xpub__mainnet_unsupported_prefix_ypub(self):
        errors = bitcoin.Bip32.validate_p2wpkh_xpub('mainnet', 'ypub6WtZZEmASeeKp6zsNwrVtdESUFyQeUBHG3KQAegQKAg4NP7jAX4uu1oqQFJL2NdHnUGt6kNbgnaEYBR9hchDBiRXKvkSgsi2fd2FGNUX5Bu')
        self.assertTrue(errors)
        self.assertTrue('P2WPKH' in errors)
        self.assertTrue('xpub' in errors)
        self.assertTrue('zpub' in errors)

    def test_validate_xpub__mainnet_malformed(self):
        errors = bitcoin.Bip32.validate_p2wpkh_xpub('mainnet', 'zpub7oMKbeQTqZyz7mbfjdSBXbHwyXYYwEN5sDSV48rLqRk6rnLELQCnnG1GqKju3DwjKX7C8MkfTWjLUPCM6RoCMnTskbvQqaDSaatwVtBQVPL')
        self.assertTrue(errors)
        self.assertTrue('Malformed' in errors)
        self.assertTrue('xpub' in errors)
        self.assertTrue('zpub' in errors)

    def test_validate_xpub__testnet_unsupported_prefix_upub(self):
        errors = bitcoin.Bip32.validate_p2wpkh_xpub('testnet', 'upub5E3Sunp3uanxvzDGmjQYA3ZCW9aVU8RNaMyDn51ij9vR7gMZZT6Rr9atXgDdXwsjt2BsQTzTMYL6sjGesi6ueaQXqVzDJkPbZYWQKt1ec3c')
        self.assertTrue('P2WPKH' in errors)
        self.assertTrue('tpub' in errors)
        self.assertTrue('vpub' in errors)

    def test_validate_xpub__testnet_malformed(self):
        errors = bitcoin.Bip32.validate_p2wpkh_xpub('testnet', 'vpub6UtSQhMcYBgGe3UxC5suwHbayv9Xw2raS9U4kyv5pTrikTNGLbxhBdogWm8TffqLHZhEYo7uBcouPiFQ8BNMP6JFyJmqjDxxUyToB1RcToF')
        self.assertTrue(errors)
        self.assertTrue('Malformed' in errors)
        self.assertTrue('tpub' in errors)
        self.assertTrue('vpub' in errors)

    def test_validate_xpub__testnet_malformed_another_way_xpub(self):
        errors = bitcoin.Bip32.validate_p2wpkh_xpub('testnet', 'vpub5devvgkn7251z6adsvnxntbmkayc4dvtwmqklevdnkmczmzarsg4c3t2ufk5jikv5g6hekv9qdjrfzafjpfc6efigb8sdbgxrdxxxhhxnjv')
        self.assertTrue(errors)
        self.assertTrue('Malformed' in errors)
        self.assertTrue('tpub' in errors)
        self.assertTrue('vpub' in errors)

    def test_validate_xpub__mainnet_valid_xpub(self):
        errors = bitcoin.Bip32.validate_p2wpkh_xpub('mainnet', self.VALID_XPUB)
        self.assertEmpty(errors)

    def test_validate_xpub__mainnet_valid_zpub(self):
        errors = bitcoin.Bip32.validate_p2wpkh_xpub('mainnet', self.VALID_ZPUB)
        self.assertEmpty(errors)

    def test_validate_xpub__testnet_valid_tpub(self):
        errors = bitcoin.Bip32.validate_p2wpkh_xpub('testnet', self.VALID_TPUB)
        self.assertEmpty(errors)

    def test_validate_xpub__testnet_valid_vpub(self):
        errors = bitcoin.Bip32.validate_p2wpkh_xpub('testnet', self.VALID_VPUB)
        self.assertEmpty(errors)

    # generate_testnet_p2wpkh_wallet

    def test_generate_testnet_p2wpkh_wallet(self):
        xprv, xpub = bitcoin.Bip32.generate_testnet_p2wpkh_wallet()
        self.assertEqual('vprv', xprv[0:4])
        self.assertTrue('vpub', xpub[0:4])
        errors = bitcoin.Bip32.validate_p2wpkh_xpub('testnet', xpub)
        self.assertEmpty(errors)

    # to_standard_xpub

    def test_to_standard_xpub__mainnet(self):
        # VALID_XPUB and VALID_ZPUB are the same underlying public key
        result = bitcoin.Bip32.to_standard_xpub(self.VALID_ZPUB)
        self.assertEqual(self.VALID_XPUB, result)

    def test_to_standard_xpub__testnet(self):
        # VALID_TPUB and VALID_VPUB are the same underlying public key
        result = bitcoin.Bip32.to_standard_xpub(self.VALID_VPUB)
        self.assertEqual(self.VALID_TPUB, result)

    # wallet_fingerprint

    def test_wallet_fingerprint__mainnet(self):
        fingerprint1 = bitcoin.Bip32.wallet_fingerprint(self.VALID_XPUB)
        self.assertEqual('efaf6ac3aeaee6da', fingerprint1)

        # VALID_XPUB and VALID_ZPUB are the same underlying public key
        # The fingerprint should be the same regardless of the xpub encoding
        fingerprint2 = bitcoin.Bip32.wallet_fingerprint(self.VALID_ZPUB)
        self.assertEqual(fingerprint1, fingerprint2)

    def test_wallet_fingerprint__testnet(self):
        fingerprint1 = bitcoin.Bip32.wallet_fingerprint(self.VALID_TPUB)
        self.assertEqual('f4e82a22507a4196', fingerprint1)

        # VALID_TPUB and VALID_VPUB are the same underlying public key
        # The fingerprint should be the same regardless of the encoding the xpub is passed
        fingerprint2 = bitcoin.Bip32.wallet_fingerprint(self.VALID_VPUB)
        self.assertEqual(fingerprint1, fingerprint2)
