
var nombre = document.getElementsByName('txt_nombre')
var appaterno = document.getElementsByName('txt_appaterno')
var apmaterno = document.getElementsByName('txt_apmaterno')
var rut = document.getElementsByName('txt_rut')
var edad = document.getElementsByName('txt_edad')
var nomvacuna = document.getElementsByName('txt_vacuna')
var fecha = document.getElementsByName('txt_fecha')
const form = document.getElementById('form')

form.addEventListener('submit', (e) => {

    if (nombre.value().length<3)
   {
       alert("Nombre debe tener al menos 3 caracteres")
       e.preventDefault()

       
   }
   if (appaterno.value().length<3)
   {
       alert("Apellido paterno debe tener al menos 3 caracteres")
       e.preventDefault()

   }
   if (apmaterno.value().length<3)
   {
       alert("Apellido materno debe tener al menos 3 caracteres")
       e.preventDefault()

       
   }

   if (rut.value()<9 && rut.value()>10 && rut.value().indexOf('-')<0)
   {
       alert("El rut debe tener entre 9 y 10 caracteres, sin puntos y debe contener un guión")
       e.preventDefault()

   }


    
})