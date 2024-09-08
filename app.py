from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dry Fruit Shop</title>
        
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f5f5f5;
                color: #333;
            }
            header {
                background-color: #fff;
                padding: 20px 0;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                position: relative;
            }
            .header-image {
                width: 100%;
                height: auto;
                display: block;
            }
            .nav-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
                position: relative;
                z-index: 1;
            }
            .logo {
                font-size: 1.5em;
                font-weight: bold;
                color: #4CAF50;
            }
            nav ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                display: flex;
            }
            nav ul li {
                margin-left: 20px;
            }
            nav ul li a {
                text-decoration: none;
                color: #333;
                font-weight: bold;
            }
            #hero {
                background: url('https://images.unsplash.com/photo-1605450532074-bb3be9fcfc4f') no-repeat center center/cover;
                color: white;
                height: 500px;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
            }
            .hero-text {
                background-color: rgba(0, 0, 0, 0.5);
                padding: 20px;
                border-radius: 10px;
            }
            .hero-text h2 {
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            .hero-text p {
                font-size: 1.2em;
                margin-bottom: 20px;
            }
            .btn-primary {
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
            }
            .btn-primary:hover {
                background-color: #45a049;
            }
            #products {
                max-width: 1200px;
                margin: 50px auto;
                padding: 0 20px;
                text-align: center;
            }
            #products h3 {
                font-size: 2em;
                margin-bottom: 20px;
            }
            .product-container {
                display: flex;
                justify-content: space-around;
                flex-wrap: wrap;
            }
            .product-item {
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                max-width: 300px;
                margin: 20px;
                text-align: center;
            }
            .product-item img {
                width: 100%;
                height: auto;
                border-radius: 10px;
                margin-bottom: 15px;
            }
            footer {
                background-color: #4CAF50;
                color: white;
                text-align: center;
                padding: 10px 0;
                margin-top: 50px;
            }
        </style>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    </head>
    <body>
        <header>
            <div class="nav-container">
                <h1 class="logo">Dry Fruit Shop</h1>
                <nav>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Products</a></li>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </nav>
            </div>
        </header>

        <section id="hero">
            <div class="hero-text">
                <h2>Fresh & Healthy Dry Fruits</h2>
                <p>Experience the finest selection of dry fruits delivered to your doorstep.</p>
                <a href="#products" class="btn-primary">Explore Products</a>
            </div>
        </section>
        
        <section id="products">
            <h3>Our Best Sellers</h3>
            <div class="product-container">
                <div class="product-item">
                    <img src="https://cdn.pixabay.com/photo/2022/10/04/06/26/almonds-7497425_1280.jpg" alt="Almonds">
                    <h4>Almonds</h4>
                    <p>High-quality almonds sourced from California.</p>
                </div>
                <div class="product-item">
                    <img src="https://vaaradhifarms.com/cdn/shop/files/amer_med_roasted_cashews_in_a_white_bown_on_top_of_a_wooden_cou_2b1dd2d1-1690-45f2-ad3b-e79afcd643ab.png?v=1714074548&width=2048" alt="Cashews">
                    <h4>Cashews</h4>
                    <p>Crispy and delicious cashews packed with nutrients.</p>
                </div>
                <div class="product-item">
                    <img src="https://img.freepik.com/premium-photo/product-shots-walnuts-high-quality-4k-ultra-h_670382-121972.jpg" alt="Walnuts">
                    <h4>Walnuts</h4>
                    <p>Fresh walnuts rich in Omega-3 and antioxidants.</p>
                </div>
            </div>
        </section>
        
        <footer>
            <p>&copy; 2024 Dry Fruit Shop. All rights reserved.</p>
        </footer>

        <script>
            document.addEventListener("DOMContentLoaded", function() {
                console.log("Welcome to the Advanced Dry Fruit Shop!");
            });
        </script>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True, port=5666)
