#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/9/29 14:42
@user: jiananwang
@title: SQL_to_noSQL
"""
from typing import List, Any

customer_dict = {
    "1000": "Ben Choi",
    "1001": "Jayden Choi",
    "1002": "Cammy Soh",
    "1004": "Mason Greenwood",
    "1005": "Dean Henderson",
}

product_dict = {
    "50001": ("Scott Pick A Size Multi Purpose Towels", 4.25),
    "50002": ("Japanese Super Crispy Chicken", 11.80),
    "50003": ("Vegan Beyond Burger Plant Based Patties Beef", 14.90),
    "50004": ("Korean Honey Sweet Potato", 9.90),
    "50005": ("Premium Atlantic Salmon 1Kg", 22.00)
}

order_dict = {
    "1880001": ("1000", "2020/01/21"),
    "1880002": ("1000", "2020/01/22"),
    "1880003": ("1000", "2020/01/23"),
    "1880004": ("1001", "2020/01/22"),
    "1880005": ("1001", "2020/01/23"),
    "1880006": ("1004", "2020/01/24"),
    "1880007": ("1005", "2020/01/25"),
}

order_line_dict = {
    ("1000", "1880001", "50001"): 2,
    ("1000", "1880001", "50003"): 1,
    ("1000", "1880002", "50002"): 2,
    ("1000", "1880003", "50004"): 4,
    ("1000", "1880003", "50005"): 2,
    ("1001", "1880004", "50003"): 1,
    ("1001", "1880004", "50004"): 1,
    ("1001", "1880005", "50002"): 2,
    ("1004", "1880006", "50004"): 1,
    ("1004", "1880006", "50005"): 1,
    ("1005", "1880007", "50002"): 2,
    ("1005", "1880007", "50003"): 1,
    ("1005", "1880007", "50001"): 2
}


def get_customer_order_id(customer_id: str, order_dict: dict) -> list[Any] | str:
    order_list = []
    for k, b in order_dict.items():
        if b[0] == customer_id:
            order_list.append(k)

    if order_list:
        return order_list
    return "null"


def get_productInfors(orderid: str) -> list:
    def make_string(productid: str, quantity: int, price: float) -> dict:
        product_infro_dict = {"prodcutID": str(productid),
                              "quantity": quantity,
                              "price": price}
        return product_infro_dict

    productInfors = []
    for k_order_line, v_order_line in order_line_dict.items():
        if orderid == k_order_line[1]:
            product_id = k_order_line[2]
            product_quantity = v_order_line
            product_price = product_dict[product_id][1]
            productInfors.append(make_string(product_id, product_quantity, product_price))

    return productInfors


for k, v in customer_dict.items():
    print(f"""{{
            "_id": "{k}",
            "customerName": "{v}",
            "customerOrder": {get_customer_order_id(k, order_dict)}
        }},
        """, end="")
print()
print()
print("-------------"*2)

for k, v in order_dict.items():
    print(f"""
    {{
        "_id": "{k}",
        "orderDate": "{v[1]}",
        "customerID": "{v[0]}",
        "productInfors":
            {get_productInfors(orderid=k)}
    }},""", end="")

print()
print()
print("-------------"*2)

for k, v in product_dict.items():
    print(f"""
    {{
        "_id": "{k}",
        "productName": "{v[0]}",
        "standardPrice": {v[1]}
    }},""", end="")
