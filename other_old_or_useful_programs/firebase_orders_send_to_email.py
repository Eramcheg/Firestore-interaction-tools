import firebase_admin
from firebase_admin import credentials, firestore

from datetime import datetime, timedelta
import pytz
# Initialize Firebase
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)

# Firestore collection references
db = firestore.client()
full_orders_ref = db.collection("FullOrders")
backorders_ref = db.collection("Backorders")
orders_ref = db.collection("Orders")

timezone = pytz.timezone('Europe/Prague')
now = datetime.now(timezone)
start_of_day = datetime(now.year, now.month, now.day-1, 0, 0, 0, tzinfo=timezone)
end_of_day = start_of_day + timedelta(days=1)


todays_orders = {}


# Function to fetch all documents from a collection
def fetch_documents_by_date(collection_ref, start_of_day, end_of_day):
    query = collection_ref.where("date", ">=", start_of_day).where("date", "<", end_of_day)
    documents = query.stream()
    return [doc.to_dict() for doc in documents]


# Fetch and store documents in arrays by date
full_orders = fetch_documents_by_date(full_orders_ref, start_of_day, end_of_day)
back_orders = fetch_documents_by_date(backorders_ref, start_of_day, end_of_day)
orders = fetch_documents_by_date(orders_ref, start_of_day, end_of_day)

# Your logic to work with the arrays full_orders, back_orders, orders
for full_order in full_orders:
    print(f"Found in FullOrders: {full_order.get('order-id')}")
    # Assuming 'name-order' is a key in your documents
    name_order = full_order.get("order-id")
    todays_orders[name_order] = [full_order, {}, {}]
    # Find matching in back_orders
    matching_back_orders = [doc for doc in back_orders if doc.get("order-id") == name_order]
    for match in matching_back_orders:
        todays_orders[name_order][1] = match
        print(f"Matching in Backorders: {match.get('order-id')}")

    # Find matching in orders
    matching_orders = [doc for doc in orders if doc.get("order-id") == name_order]
    for match in matching_orders:
        todays_orders[name_order][2] = match
        print(f"Matching in Orders: {match.get('order-id')}")
print(todays_orders)