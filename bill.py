"""
bill.py
Billing entity for a patient's hospital visit.
"""

from datetime import datetime


class Bill:
    """Manages charges and payments for a patient's stay."""

    _counter = 1

    def __init__(self, patient_id: str, patient_name: str):
        self._bill_id = f"BILL{Bill._counter:04d}"
        Bill._counter += 1
        self._patient_id = patient_id
        self._patient_name = patient_name
        self._items: list[dict] = []
        self._paid: bool = False
        self._created_at: datetime = datetime.now()
        self._discount_percent: float = 0.0

    # ---------- properties ----------
    @property
    def bill_id(self):
        return self._bill_id

    @property
    def patient_id(self):
        return self._patient_id

    @property
    def is_paid(self):
        return self._paid

    @property
    def discount_percent(self):
        return self._discount_percent

    @discount_percent.setter
    def discount_percent(self, value: float):
        if not (0 <= value <= 100):
            raise ValueError("Discount must be between 0 and 100.")
        self._discount_percent = value

    # ---------- methods ----------
    def add_item(self, description: str, amount: float, quantity: int = 1):
        self._items.append(
            {"description": description, "amount": amount, "quantity": quantity}
        )

    @property
    def subtotal(self) -> float:
        return sum(item["amount"] * item["quantity"] for item in self._items)

    @property
    def discount_amount(self) -> float:
        return self.subtotal * (self._discount_percent / 100)

    @property
    def total(self) -> float:
        return self.subtotal - self.discount_amount

    def pay(self):
        self._paid = True

    def print_bill(self):
        separator = "─" * 52
        print(f"\n{'─'*52}")
        print(f"  HOSPITAL BILL  |  {self._bill_id}")
        print(f"  Patient: {self._patient_name} [{self._patient_id}]")
        print(f"  Date   : {self._created_at.strftime('%Y-%m-%d %H:%M')}")
        print(separator)
        print(f"  {'Description':<28} {'Qty':>4} {'Amount':>10}")
        print(separator)
        for item in self._items:
            total_item = item["amount"] * item["quantity"]
            print(f"  {item['description']:<28} {item['quantity']:>4} {total_item:>10,.0f}")
        print(separator)
        print(f"  {'Subtotal':<34} {self.subtotal:>10,.0f}")
        if self._discount_percent > 0:
            print(f"  {'Discount (' + str(self._discount_percent) + '%)':<34} -{self.discount_amount:>9,.0f}")
        print(f"  {'TOTAL (Rs.)':<34} {self.total:>10,.0f}")
        print(f"  Status : {'✓ PAID' if self._paid else '✗ UNPAID'}")
        print(separator)

    def get_info(self) -> dict:
        return {
            "Bill ID": self._bill_id,
            "Patient ID": self._patient_id,
            "Patient Name": self._patient_name,
            "Subtotal": f"Rs. {self.subtotal:,.0f}",
            "Discount": f"{self._discount_percent}%",
            "Total": f"Rs. {self.total:,.0f}",
            "Status": "Paid" if self._paid else "Unpaid",
        }

    def __str__(self):
        return (
            f"Bill [{self._bill_id}] Patient: {self._patient_name} | "
            f"Total: Rs.{self.total:,.0f} | {'PAID' if self._paid else 'UNPAID'}"
        )
