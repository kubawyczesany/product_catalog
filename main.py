from flask import (Flask, render_template,
                    url_for, request, redirect)

def create_app ():
    app = Flask(__name__)
    products = ['Kawa', 'Mleko', 'Maselko']

    @app.route('/')
    def index ():
        items = [{'name': p,
                'del_url': url_for('delete', product=p)
                } for p in products]
        return render_template('items.html', items=items, add_url=url_for('add'))

    @app.route('/add', methods=['POST'])
    def add ():
        products.append(request.form['productName'])
        return redirect(url_for('index'))

    @app.route('/delete/<product>')
    def delete (product):
        try:
            products.remove(product)
        except:
            pass
        return redirect(url_for('index'))


    return app


create_app().run('0.0.0.0')
