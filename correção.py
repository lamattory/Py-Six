from flask import Flask,redirect,url_for,request,render_template
app =Flask(__name__)
@app.route('/admin/<nome>'/'<senha>')
def admin(nome , senha):
  frase = "<b>Bem vindo</b>"+nome +'sua senha é :' + senha 
  return frase
  
@app.route('/login/', methods = ['POST','GET'])
def login():
  if request.method == 'POST':
    usuario = request.form['c_usuario']
    senha = request.form['c_senha']
    if usuario == 'thamires' and senha == 123:
    return rediequest.args.get('c_usuario')
    return redirect(url_for('admin',nome = usuario))
  else:
    usuario = rrect(url_for('admin',nome = usuario))
@app.route('/entrar/')
def admin_index():
  return render_template('login.html')
  
if __name__== '__main__':
  app.run('0.0.0.0')
