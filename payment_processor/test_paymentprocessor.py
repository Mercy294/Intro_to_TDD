import unittest
from unittest.mock import MagicMock
from payment import PaymentProcessor
import datetime


class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.api = MagicMock()
        self.processor = PaymentProcessor(api_client=self.api)

    def test_credit_card_validation_fails(self):
        metadata = {"card_number": "", "expiry": ""}
        with self.assertRaises(ValueError):
            self.processor.process_payment(
                300, "USD", 5, "credit_card", metadata, None, 0
            )

    def test_paypal_validation_fails(self):
        metadata = {"paypal_account": None}
        with self.assertRaises(ValueError):
            self.processor.process_payment(200, "USD", 3, "paypal", metadata, None, 0)

    def test_summer20_discount(self):
        metadata = {"card_number": "294", "expiry": "12/26"}
        result = self.processor.process_payment(
            400, "USD", 1, "credit_card", metadata, "SUMMER20", 0
        )
        self.assertEqual(result["final_amount"], 320)

    def test_welcome10_discount(self):
        metadata = {"card_number": "180", "expiry": 12 / 25}
        result = self.processor.process_payment(
            230, "USD", 1, "credit_card", metadata, "WELCOME10", 0
        )
        self.assertEqual(result["final_amount"], 220)

    def test_currency_conversion(self):
        metadata = {"card_number": "200", "expiry": "12/25"}
        result = self.processor.process_payment(
            100, "EUR", 1, "credit_card", metadata, None, 0
        )
        self.assertEqual(result["final_amount"], 100 * 1.2)

    def test_light_fraud_check_called(self):
        self.processor._light_fraud_check = MagicMock()
        metadata = {"card_number": "120", "expiry": "12/25"}
        self.processor.process_payment(50, "USD", 1, "credit_card", metadata, None, 1)
        self.processor._light_fraud_check.assert_called_once_with(1, 50)

    def test_heavy_fraud_check_called(self):
        self.processor._heavy_fraud_check = MagicMock()
        metadata = {"card_number": "123", "expiry": "12/25"}
        self.processor.process_payment(150, "USD", 1, "credit_card", metadata, None, 1)
        self.processor._heavy_fraud_check.assert_called_once_with(1, 150)

    def test_api_called_for_credit_card(self):
        metadata = {"card_number": "111", "expiry": "12/26"}
        self.processor.process_payment(100, "USD", 1, "credit_card", metadata, None, 0)
        self.api.post.assert_called_once()

    def test_refund_fee_calculation(self):
        metadata = {"reason": "test"}
        result = self.processor.refund_payment(
            "txn123", 1, "reason", 100, "USD", metadata
        )
        self.assertEqual(result["net_amount"], 95)
