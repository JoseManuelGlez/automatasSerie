from flask import Flask, render_template, request

app = Flask(__name__)

abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def verificar1(c, array):
    if not c[2] in abecedario[10:]:
        array.append("Falla q2")
        return
    array.append("q17 → ")

    if not c[3] in abecedario:
        array.append("Falla q17")
        return

    array.append("q18 → ")
    if c[4] != "-":
        array.append("Falla q18")
        return

    array.append("q19 → ")
    
    if c[5] == '0':
        array.append("q30 → ")
        if not c[6] in numeros[1]:
            array.append("Falla q30")
            return
    elif c[5] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
        array.append("q20 → ")
        if not c[6] in numeros:
            array.append("Falla q20")
            return
    else:
        array.append("Falla q19")
    array.append("q21 → ")

    if not c[7] in abecedario:
        array.append("Falla q21")
        return
    
    array.append("q22")
    

    array.append("La cadena es correcta")

################################################################################
def verificar2(c, array):
    if not c[3] in abecedario[23:]:
        array.append("Falla q3")
        return
    array.append("q18 → ")

    if c[4] != "-":
        array.append("Falla q18")
        return
    array.append("q19 → ")

    if c[5] == '0':
        array.append("q30 → ")
        if not c[6] in numeros[1]:
            array.append("Falla q30")
            return
    elif c[5] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
        array.append("q20 → ")
        if not c[6] in numeros:
            array.append("Falla q20")
            return
    else:
        array.append("Falla q19")
    array.append("q21 → ")

    if not c[7] in abecedario:
        array.append("Falla q21")
        return
    array.append("q22")

    array.append("La cadena es correcta")

################################################################################
def verificar3(c, array):
    if not c[5] in numeros[1:]:
        array.append("Falla q5")
        return
    array.append("q20 → ")
    

    if not c[6] in numeros:
        array.append("Falla q20")
        return
    array.append("q21 → ")

    if not c[7] in abecedario:
        array.append("Falla q21")
        return
    array.append("q22")

    array.append("La cadena es correcta")

################################################################################
def verificar4(c, array):
    if not c[6] in numeros:
        array.append("Falla q6")
        return
    array.append("q21 → ")

    if not c[7] in abecedario:
        array.append("Falla q21")
        return
    array.append("q22")

    array.append("La cadena es correcta")

################################################################################
def verificar5(c, array):
    if c[7] in abecedario[6:]:
        array.append("La cadena es correcta")
    else:
        array.append("Falla q7")
    array.append("q22")

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
def verificar6(c, array):
    if not c[2] in abecedario[0:10]:
        array.append("Falla q10")
        return
    array.append("q23 → ")

    if not c[3] in abecedario:
        array.append("Falla q23")
        return
    array.append("q24 → ")

    if c[4] != "-":
        array.append("Falla q24")
        return
    array.append("q25 → ")

    if c[5] == '0':
        array.append("q29 → ")
        if not c[6] in numeros[1:]:
            array.append("Falla q29")
            return
    elif c[5] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
        array.append("q26 → ")
        if not c[6] in numeros:
            array.append("Falla q26")
            return
    else:
        array.append("Falla q25")
    array.append("q27 → ")

    if not c[7] in abecedario:
        array.append("Falla q27")
        return
    array.append("q28")

    array.append("La cadena es correcta")

################################################################################
def verificar7(c, array):
    if not c[3] in abecedario[0:4]:
        array.append("Falla q11")
        return
    array.append("q24 → ")

    if c[4] != "-":
        array.append("Falla q24")
        return
    array.append("q25 → ")

    if c[5] == '0':
        if not c[6] in numeros[1:]:
            array.append("Falla q29")
            return
    elif c[5] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
        if not c[6] in numeros:
            array.append("Falla q26")
            return
    else:
        array.append("Falla q25")
    array.append("q27 → ")

    if not c[7] in abecedario:
        array.append("Falla q27")
        return
    array.append("q28")

    array.append("La cadena es correcta")

################################################################################
def verificar8(c, array):
    
    if c[5] == '0':
        if not c[6] in numeros[1]:
            array.append("Falla q29")
            return
    elif c[5] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
        if not c[6] in numeros:
            array.append("Falla q26")
            return
    else:
        array.append("Faala q25")
    array.append("q27 → ")

    if not c[7] in abecedario:
        array.append("Falla q27")
        return
    array.append("q28")

    array.append("La cadena es correcta")

################################################################################
def verificar9(c, array):
    if not c[6] in numeros[0:9]:
        array.append("Falla q14")
        return
    array.append("q27 → ")

    if not c[7] in abecedario:
        array.append("Falla q27")
        return
    array.append("q28")

    array.append("La cadena es correcta")

################################################################################
def verificar10(c, array):
    if not c[7] in abecedario[0:19]:
        array.append("Falla q15")
        return
    array.append("q28")

    array.append("La cadena es correcta")

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
def validar_serie(c, array):
    array.append("→q0 → ")
    if c[0] == "1":
        array.append("q1 → ")
        if c[1] == "-":
            array.append("q2 → ")
            if c[2] == "J":
                array.append("q3 → ")
                if c[3] == "W":
                    array.append("q4 → ")
                    if c[4] == "-":
                        array.append("q5 → ")
                        if c[5] == "0":
                            array.append("q6 → ")
                            if c[6] == "1":
                                array.append("q7 → ")
                                if c[7] == "F":
                                    array.append("q8")
                                    array.append("La cadena es correcta")
                                else:
                                    verificar5(c, array)
                            else:
                                verificar4(c, array)
                        else:
                            verificar3(c, array)
                    else:
                        array.append("Falla q4")
                else:
                    verificar2(c, array)
            else:
                verificar1(c, array)
        else:
            array.append("Falla q1")
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
    elif c[0] == "2":
        array.append("q9 → ")
        if c[1] == "-":
            array.append("q10 → ")
            if c[2] == "K":
                array.append("q11 → ")
                if c[3] == "E":
                    array.append("q12 → ")
                    if c[4] == "-":
                        array.append("q13 → ")
                        if c[5] == "9":
                            array.append("q14 → ")
                            if c[6] == "9":
                                array.append("q15 → ")
                                if c[7] == "T":
                                    array.append("q16")
                                    array.append("La cadena es correcta")
                                else:
                                    verificar10(c, array)
                            else:
                                verificar9(c, array)
                        else:
                            verificar8(c, array)
                    else:
                        array.append("Falla q12")
                else:
                    verificar7(c, array)
            else:
                verificar6(c, array)
        else:
            array.append("Falla q9")
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
    else:
        array.append("Falla q0")
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################

@app.route('/', methods=['GET', 'POST'])
def index():
    array=[]
    input_string = ""
    result = None
    if request.method == 'POST':
        input_string = request.form['input_string']
        validar_serie(input_string, array)
        if array[-1][0] == "F":
            array.append("La cadena es incorrecta")
        

    return render_template('index.html', result=array, cadena=input_string)

if __name__ == '__main__':
    app.run(debug=True)