import datetime


class PaymentMethodValidator:
    def validate(self, metadata):
        raise NotImplementedError()


class CreditCardValidator(PaymentMethodValidator):
    def validate(self, metadata):
        if not metadata.get("card_number") or not metadata.get("expiry"):
            raise ValueError("Invalid credit card metadata")


class PayPalValidator(PaymentMethodValidator):
    def validate(self, metadata):
        if not metadata.get("paypal_account"):
            raise ValueError("Invalid PayPal metadata")


class DiscountStrategy:
    def apply(self, amount):
        return amount


class Summer20Discount(DiscountStrategy):
    def apply(self, amount):
        return amount * 0.8


class Welcome10Discount(DiscountStrategy):
    def apply(self, amount):
        return amount - 10


class NoDiscount(DiscountStrategy):
    def apply(self, amount):
        return amount


class FraudChecker:
    def check(self, user_id, amount):
        raise NotImplementedError()


class LightFraudChecker(FraudChecker):
    def check(self, user_id, amount):
        print(f"Light fraud check for user {user_id} on amount {amount}")


class HeavyFraudChecker(FraudChecker):
    def check(self, user_id, amount):
        print(f"Heavy fraud check for user {user_id} on amount {amount}")


class NoFraudChecker(FraudChecker):
    def check(self, user_id, amount):
        pass


class CurrencyConverter:
    def __init__(self, rate=1.2):
        self.rate = rate

    def convert(self, amount, currency):
        if currency == "USD":
            return amount
        return amount * self.rate


class PaymentProcessorRefactored:
    def __init__(
        self,
        api_client,
        validator,
        fraud_checker,
        discount_strategy,
        currency_converter,
    ):
        self.api = api_client
        self.validator = validator
        self.fraud = fraud_checker
        self.discount = discount_strategy
        self.converter = currency_converter

    def process_payment(self, amount, currency, user_id, payment_method, metadata):
        self.validator.validate(metadata)
        self.fraud.check(user_id, amount)
        final_amount = self.discount.apply(amount)
        final_amount = self.converter.convert(final_amount, currency)
        transaction = {
            "user_id": user_id,
            "original_amount": amount,
            "final_amount": final_amount,
            "currency": currency,
            "payment_method": payment_method,
            "metadata": metadata,
            "timestamp": datetime.datetime.now().isoformat(),
        }

        self.api.post("/payments", transaction)
        return transaction
