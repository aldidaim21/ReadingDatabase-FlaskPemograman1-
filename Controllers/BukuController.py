from Models.BukuModel import Item, db

def index():
    # Ambil semua data buku dari database
    items = Item.query.all()
    return items

