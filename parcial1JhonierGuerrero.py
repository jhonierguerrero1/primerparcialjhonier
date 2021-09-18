
import mysql.connector
print('Iniciando')
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='parcial1usuarios',
    port=3306
)

print(" ")
print(" ")
print("**     MENÚ     **")
print("1. Registrarse")
print("2. Iniciar Sesión")
print("3. salir")
opc=input("")

while opc!="3" and opc < "3":
    
    if opc=="1":

        def crearUsuario(nombre,correo,contrasenna):
            cursor=db.cursor()
            cursor.execute('''
                insert into usuarios(nombre,correo,contraseña)
                values (%s,%s,%s)''',
                (nombre,
                correo,
                contrasenna))

            db.commit()
            cursor.close()
        print("")
        nom=input("ingrese el nombre")
        corre=input("ingrese el correo")
        contra=input("ingrese la contraseña (minimo 8 caracteres,una mayuscula, un caracter especial)")
        a=contra.islower()
       
        while len(contra) < 8 or a == True:
            contra=input("ingrese la contraseña (minimo 8 caracteres)")
            a=contra.islower()
        crearUsuario(nom,corre,contra)

        print("Registrado correctamente...")
        print(" ")
        print(" ")
        print("**     MENÚ     **")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. salir")
        opc=input("")
#_____________________________________________________________________________________________________
    if opc=="2":

        correo=input("ingrese el correo")
        contraseña=input("ingrese la contraseña")

        cursor =db.cursor()
        cursor.execute('select nombre from usuarios where usuarios.correo = "'+correo+'" and usuarios.contraseña = "'+contraseña+'"' )
        usuarios = cursor.fetchall()
        

        if len(usuarios) > 0 :
            print("Bienvenido")
            print(usuarios)
            print(" ")
            print(" ")
            print("**     MENÚ     **")
            print("1. Registrarse")
            print("2. Iniciar Sesión")
            print("3. salir")
            opc=input("")   

        else :
            print("credenciales incorrectas")
            print(" ")
            print(" ")
            print("**     MENÚ     **")
            print("1. Registrarse")
            print("2. Iniciar Sesión")
            print("3. salir")
            opc=input("")   



