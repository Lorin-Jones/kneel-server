import sqlite3
from models.metal import Metal

from models.order import Order
from models.size import Size
from models.style import Style

ORDERS= [
        {
            "id": 1,
            "metal_id": 3,
            "size_id": 2,
            "style_id": 3,
            "timestamp": 1614659931693
        }
    ]

def get_all_orders():
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.timestamp,
            m.metal,
            m.price,
            z.carets,
            z.price,
            s.style,
            s.price

        FROM orders o
        JOIN Metals m ON m.id = o.metal_id
        JOIN Sizes z ON z.id = o.size_id
        JOIN Styles s ON s.id = o.style_id
        """)

        # Initialize an empty list to hold all order representations
        orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an order instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # order class above.
            order = Order(row['id'], row['metal_id'], row['size_id'],
                            row['style_id'], row['timestamp'])

            size = Size(row['id'], row['carets'], row['price'])
            style = Style(row['id'], row['style'], row['price'])
            metal = Metal(row['id'], row['metal'], row['price'])

            order.size = size.__dict__
            order.style = style.__dict__
            order.metal = metal.__dict__

            orders.append(order.__dict__)

    return orders

def get_single_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.metal_id,
            a.size_id,
            a.style_id,
            a.timestamp
        FROM orders a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an order instance from the current row
        order = Order(data['id'], data['metal_id'], data['size_id'],
                            data['style_id'], data['timestamp'])

        return order.__dict__

def create_order(new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO orders
            ( metal_id, size_id, style_id, timestamp )
        VALUES
            ( ?, ?, ?, ? );
        """, (new_order['metal_id'], new_order['size_id'],
              new_order['style_id'], new_order['timestamp']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the order dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_order['id'] = id


    return new_order

def delete_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM orders
        WHERE id = ?
        """, (id, ))


def update_order(id, new_order):
    # Iterate the orderS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break
        