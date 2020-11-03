from app import db, Order_created, Product, Customer

db.create_all()

Tom = Customer(first_name = 'Tom', last_name = 'Hennessy')
Ben = Customer(first_name = 'Ben', last_name = 'Hasketh')
db.session.add(Tom)
db.session.add(Ben)

db.session.commit()


mouse = Product(item = 'Razer mouse')
keyboard = Product(item = 'Excelvan keyboard')
monitor = Product(item = 'HP monitor')
db.session.add(mouse)
db.session.add(monitor)
db.session.add(keyboard)

db.session.commit()

order_1 = Order_created(customer_id = Tom.id, product_id = mouse.id)
order_2 = Order_created(customer_id = Tom.id, product_id = keyboard.id)
order_3 = Order_created(customer_id = Ben.id, product_id = mouse.id)
db.session.add(order_1)
db.session.add(order_2)
db.session.add(order_3)

db.session.commit()
