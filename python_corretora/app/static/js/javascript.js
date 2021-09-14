(function(win,doc){
    'use strict';


    //Ajax do form
    if(doc.querySelector('#form')){
        var data = JSON.stringify({
            "sexo": "F",
            "nome": "Regis Tadeu",
            "cpf": "38852824880",
            "email": "",
            "telefone": "1198974562",
            "endereco": "Rua: Costa flores 52",
            "data_nascimento": "1960-01-30",
            "status_civil": "C",
            "salario": "7500.00"
          });
        let form=doc.querySelector('#form');
        function sendForm(event)
        {
            event.preventDefault();
            //let data = new FormData(form);
            console.log(data);
            let ajax = new XMLHttpRequest();
            let token = document.querySelectorAll('input')[0].value;
            //ajax.open('POST', form.action);
            ajax.open("POST", "https://projetocorretoraapicrud.herokuapp.com/api/v1/corretora/create/");
            ajax.setRequestHeader('X-CSRF-TOKEN',token);
            ajax.onreadystatechange = function()
            {
                if(ajax.status === 200 && ajax.readyState === 4){
                    //let result = doc.querySelector('#result');
                    //result.innerHTML = 'Operação realizada com sucesso!';
                    //result.classList.add('alert');
                    //result.classList.add('alert-success');
                }
            }
            ajax.send(data);
            form.reset();
        }
        form.addEventListener('submit',sendForm,false);
    }
})(window,document);

