#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0.0
    self.items = []
    self.last_transaction_amount = 0.0
    self.last_added_items = []

  def add_item(self, title, price, quantity=1):
    self.last_transaction_amount = price * quantity
    self.total += self.last_transaction_amount
    self.last_added_items = []
    for _ in range(quantity):
      self.items.append(title)
      self.last_added_items.append(title)

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      discount_multiplier = 1 - (self.discount / 100)
      self.total *= discount_multiplier
      if self.total == int(self.total):
        print(f"After the discount, the total comes to ${int(self.total)}.")
      else:
        print(f"After the discount, the total comes to ${self.total:.2f}.")

  def void_last_transaction(self):
    self.total -= self.last_transaction_amount
    for item in self.last_added_items:
      # Remove only one instance of the item at a time
      # This handles cases where multiple of the same item were added in the last transaction
      if item in self.items:
        self.items.remove(item)
    self.last_transaction_amount = 0.0
    self.last_added_items = []