from Flask import Flask,redirect,url_for,request
app =Flask(__name__)
@app.rout('/admin/<nome>')
def admin(nome):
  return"bem vindo"
@app.route('/login/', methods = ['POST','GET'])
def login():
  if request.method == 'POST':
    usuario = request.form['c_usuario']
    return redirect(url_for('admin',nome = usuario))
  else:
      usuario = request.args.get('c_usuario')
return redirect(url_for('admin',nome = usuario))

@app.route('/entrar/')
def admin_index():
    return render_template('login.html')
  
  if __name__== '__main__':
    app.run(deubug = True)
