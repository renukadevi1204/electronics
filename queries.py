from database import create_connection
def get_all_products():

    conn = create_connection()
    cur = conn.cursor()
    cur.execute("select * from products");
    return cur.fetchall()
    cur.close()
    conn.close()

def get_products_by_brand(brand_name):
    conn = create_connection()
    if conn is None:
        return[]
    cur = conn.cursor()
    cur.execute("select name from products where name=%s;", (brand_name,));
    return cur.fetchall()
    cur.close()
    conn.close()

def get_customer_orders(customer_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("select * from orders where customer_id = %s",(customer_id,));
    return cur.fetchall()
    cur.close()
    conn.close()
    