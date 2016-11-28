from sqlalchemy import *
from database_setup import Base, Category, CategoryItem
from sqlalchemy.orm import sessionmaker

# Seeding the database for testing

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Clear the tables
session.query(Category).delete()
session.query(CategoryItem).delete()

# Add categories
sample_categories = ['Big Ten', 'SEC', 'Pac-12', 'Big 12', 'ACC']

for category_name in sample_categories:
    category = Category(category_name)
    session.add(category)
session.commit()

# Add items
sample_items = {'Ohio State': 1, 'Alabama': 2, 'Stanford': 3,
                'Oklahoma': 4, 'Clemson': 5, 'Wisconsin': 1, 'Florida': 2,
                'Berkeley': 3, 'Texas': 4, 'Virginia': 5}

for item_title, item_category in sample_items.iteritems():
    item = CategoryItem(item_title, "Sample description", item_category, 1)
    session.add(item)
session.commit()
