import os

wallet_location = r"C:\Users\klimentt\OneDrive - AMU v Praze\Plocha\Wallet_DEMO"
print("Exists?", os.path.exists(wallet_location))
print("TNS file exists?", os.path.exists(os.path.join(wallet_location, "tnsnames.ora")))