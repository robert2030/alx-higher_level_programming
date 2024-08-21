// 103-script.js
$(document).ready(function() {
    $('#btn_translate').click(translateHello);
    $('#language_code').keydown(function(event) {
      if (event.keyCode === 13) {
        translateHello();
      }
    });
  
    function translateHello() {
      // Obtener el valor del campo de entrada 'language_code'
      var languageCode = $('#language_code').val();
  
      // Realizar una solicitud AJAX para obtener la traducción desde el servicio API
      $.ajax({
        url: 'https://www.fourtonfish.com/hellosalut/hello/',
        data: { lang: languageCode },
        method: 'GET',
        success: function(data) {
          // Mostrar la traducción de "Hello" en el elemento <div> con ID 'hello'
          $('#hello').text(data.hello);
        },
        error: function() {
          $('#hello').text('Error al cargar la traducción');
        }
      });
    }
  });