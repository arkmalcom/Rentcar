from django.core.exceptions import ValidationError

def validate_rnc(valor):
    rncTotal = 0
    digitoMult = [7, 9, 8, 6, 5, 4, 3, 2]
    ultimoDigito = int(valor[-1:])
    RNCMenosUltDigito = valor[:-1]
    checkDigito = 0

    for i, val in enumerate(RNCMenosUltDigito):
        rncTotal += int(val) * digitoMult[i]
    
    if(rncTotal % 11 == 0):
        checkDigito = 2
    elif(rncTotal % 11 == 1):
        checkDigito = 1
    else:
        checkDigito = 11 - (rncTotal % 11)
    
    if(checkDigito == ultimoDigito): return True
    else: raise ValidationError("RNC invalido.")

def validate_cedula(valor):
    cedTotal = 0
    cedula_valor = valor.replace('-', '')
    digitoMult = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]

    if(len(cedula_valor) == 9): validate_rnc(cedula_valor)
    else:
        if(len(cedula_valor) < 11): raise ValidationError("Un RNC debe contener 9 digitos, una cedula debe contener 11.")
        

        for i, val in enumerate(cedula_valor):
            dCalculo = int(cedula_valor[i]) * digitoMult[i]
            if(dCalculo < 10):
                cedTotal += dCalculo
            else:
                cedTotal += sum(int(c) for c in str(dCalculo))
            
        if (cedTotal % 10 == 0): return True
        else: raise ValidationError("Se debe ingresar una cedula valida")

def validate_cc(valor):
    ccTotal = 0
    ccValor = valor.replace('-', '')
    ultimoDigito = int(ccValor[-1:])
    ccMenosUltDig = ccValor[:-1]
    ccReversa = ccMenosUltDig[::-1]

    for i, val in enumerate(ccReversa, start=1):
        dCalculo = int(val)
        if(i % 2==0):
            ccTotal += dCalculo
        else:
            dCalculo = dCalculo * 2
            if(dCalculo > 9):
                dCalculo -= 9
                ccTotal += dCalculo
            else:
                ccTotal += dCalculo
        
    if((ccTotal + ultimoDigito) % 10 == 0): return True
    else: raise ValidationError("Se debe ingresar una tarjeta de credito valida")


