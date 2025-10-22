
tea_price_inr = {
    "masala chai":89,
    "mint tea":53,
    "elichi chai":200
}

tea_price_usd = {chai:price/80 for chai,price in tea_price_inr.items()}

print(tea_price_usd)