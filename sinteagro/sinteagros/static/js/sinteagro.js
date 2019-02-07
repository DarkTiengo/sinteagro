
$(document).ready(function() {

  $(".a_fechar").click(function(event) {
    /* Fechar janela */
    event.preventDefault();
    $(".pop-cadastro").remove();
  });

  $("#add_produtividade").click(function(event) {
    /* Chamar o campo de registro da Produtividade */
    event.preventDefault();
    $("body").append('<div class="pop-cadastro"><div class="row"> <div class="col text-right"> <a href="#" class="a_fechar"><i class="fa fa-close" title="Fechar"></i> </a></div></div></div>');
  });
});
