function verificarCPF(c){
    console.log(c)
    let string = c.split('');
    let num = string.length;
    var i;
    s = c;
    var c = s.substr(0,9);
    var dv = s.substr(9,2);
    var d1 = 0;
    var v = false;

    for (i = 0; i < 9; i++){
        d1 += c.charAt(i)*(10-i);
    }
    if((num > 11)||(num <11)){
        v = false;
        return v;
    }
    if (d1 == 0){
        //alert("CPF Inválido")
        v = false;
        return v;
    }
    d1 = 11 - (d1 % 11);
    if (d1 > 9) d1 = 0;
    if (dv.charAt(0) != d1){
       // alert("CPF Inválido")
        v = false;
        return v;
    }

    d1 *= 2;
    for (i = 0; i < 9; i++){
        d1 += c.charAt(i)*(11-i);
    }
    d1 = 11 - (d1 % 11);
    if (d1 > 9) d1 = 0;
    if (dv.charAt(1) != d1){
       // alert("CPF Inválido")
        v = false;
        return v;
    }
    if (!v) {
        //alert(c + "nCPF Válido")
        v = true;
        return v;
    }
}

function validatePhone (phone) {
    var regex = new RegExp('^((1[1-9])|([2-9][0-9]))((3[0-9]{3}[0-9]{4})|(9[0-9]{3}[0-9]{5}))$');
    return regex.test(phone);
}

function validatePhone (phone) {
    var regex = new RegExp('^((1[1-9])|([2-9][0-9]))((3[0-9]{3}[0-9]{4})|(9[0-9]{3}[0-9]{5}))$');
    return regex.test(phone);
}

(function(win,doc){
    'use strict';


    var id_nome = document.querySelector('#id_cpf');
    id_nome.setAttribute('onblur','TestaCPF2(this)')



    /*Limpa formulario*/
    let submit_create = document.querySelector('.btn-success');
    submit_create.addEventListener ('keypress', (event) => {
        let form_create = document.querySelector('.form');
        form_create.querySelectorAll('input').forEach(element => {
            console.log(element);
            element.value = '';
         })
    });




    let cpf = document.querySelector('#id_cpf');
    let cpf_label = document.querySelector('.cpf_valido');
    let  id_telefone = document.querySelector('#id_telefone');
    let id_telefone_label = document.querySelector('.celular_valido');

    cpf.addEventListener ('blur', (event) => {
        var aux = cpf.value;
        const strNum = aux.replace(/[^0-9]/g, '')
        var result = verificarCPF(strNum);
        if(result){
            cpf_label.classList.remove("ative");
            cpf_label.classList.add("inative");
        }else{
            cpf_label.classList.remove("inative");
            cpf_label.classList.add("ative");
        }
    });

    id_telefone.addEventListener ('blur', (event) => {
        var aux = id_telefone.value;
        const strNum = aux.replace(/[^0-9]/g, '')
        var result = validatePhone(strNum);
        console.log(result);
        if(result){
            id_telefone_label.classList.remove("ative");
            id_telefone_label.classList.add("inative");
        }else{
            id_telefone_label.classList.remove("inative");
            id_telefone_label.classList.add("ative");
        }
    });




})(window,document);