$(function() {
  $('[data-toggle="tooltip"]').tooltip()
});
$(document).ready(function() {

  var control = true;

  //Checa e-mail / check if e-mail
  $("#email").change(function() {
    var email = $(this).val();
    $.ajax({
      url: 'ajax/check_email/',
      data: {
        'email': email
      },
      dataType: 'json',
      success: function(data) {
        if (data.is_taken) {
          control = false;
          $("#email").tooltip('dispose').tooltip({
            html: true,
            title: "<i class='fa fa-close'></i> Email já cadastrado",
            placement: "right",
          }).tooltip('show');
        } else{
          control = true;
          $("#email").tooltip('dispose').tooltip({
            html: true,
            title: "<i class='fa fa-check'></i> Email disponivel para uso",
            placement: "right",
          }).tooltip('show');
        }
      }
    });
  });


//Adiciona cidades / Add cities
  $("#estado").change(function(){
    var estado = $(this).val();
    $("#cidade")
     .empty()
     .append("<option value=''>Selecione uma opção abaixo</option>");
    $.ajax({
      url: 'ajax/get_cidade/',
      data: {'estado' : estado},
      dataType: 'json',
      success: function(data) {
        $("#cidade").prop("disabled",false);
        $(data.cities).each(function(){
          $("#cidade")
          .append("<option value='" + $(this)[0].id + "'>" + $(this)[0].nome + "</option>");
        });
      }
      });
    });

  // Confere form antes do envio / Check form before submit
  $("form #block-cadastro").submit(function(e) {
    e.preventDefault();
    var aux = true;
    if ($(".form-control:invalid").length == 0 && control) {
      $(this).submit();
    }
  });

});
