from app import db, Product

def create_sample_data():
    db.create_all()
    
    # Add some sample products
    almonds = Product(name='Almonds', description='High-quality almonds sourced from California.', image_url='https://cdn.pixabay.com/photo/2022/10/04/06/26/almonds-7497425_1280.jpg')
    cashews = Product(name='Cashews', description='Crispy and delicious cashews packed with nutrients.', image_url='https://vaaradhifarms.com/cdn/shop/files/amer_med_roasted_cashews_in_a_white_bown_on_top_of_a_wooden_cou_2b1dd2d1-1690-45f2-ad3b-e79afcd643ab.png?v=1714074548&width=2048')
    walnuts = Product(name='Walnuts', description='Fresh walnuts rich in Omega-3 and antioxidants.', image_url='https://img.freepik.com/premium-photo/product-shots-walnuts-high-quality-4k-ultra-h_670382-121972.jpg')
    
    db.session.add_all([almonds, cashews, walnuts])
    db.session.commit()

if __name__ == '__main__':
    create_sample_data()
