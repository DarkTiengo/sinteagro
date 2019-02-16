$(document).ready(function(){

// Create Calendar / Cria Calendario
  $('#calendar').fullCalendar({
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'month,agendaWeek,agendaDay,listMonth'
    },
    locale: "pt-br"
  });

//js Calendario
moment().locale('pt-br');

$("#note-date").append(moment().format('LL'))
// Create note lines / Cria linhas da agenda
var i = 0;
  while(i < 8){
    $(".list").append('<div class="lines"></div><li><input class="input-note" type="text" /></li>');
    i++;
  };



  });
