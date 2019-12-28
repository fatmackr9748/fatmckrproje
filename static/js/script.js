$(document).ready(function() {
    //DIMMER

    $('.special.cards .image').dimmer({
        on: 'hover'
      });
      
    //Sıdebar
    $('.ui.sidebar')
        .sidebar('attach events', '.toc.item');

    // MODAL

    $("#card1").click(function() {
        $(".ui.modal1.modal1").modal("toggle");
    });

    $("#card2").click(function() {
        $(".ui.modal2.modal2").modal("toggle");
    });

    $("#card3").click(function() {
        $(".ui.modal3.modal3").modal("toggle");
    });

    $("#card4").click(function() {
        $(".ui.modal4.modal4").modal("toggle");
    });

    $("#card5").click(function() {
        $(".ui.modal5.modal5").modal("toggle");
    });

    $("#card6").click(function() {
        $(".ui.modal6.modal6").modal("toggle");
    });
    $(document)
    .ready(function() {
      $('.ui.form')
        .form({
          fields: {
            email: {
              identifier  : 'email',
              rules: [
                {
                  type   : 'empty',
                  prompt : 'E-mail Adresinizi Girmediniz.'
                },
                {
                  type   : 'email',
                  prompt : 'Lütfen, geçerli bir e-mail adresi giriniz.'
                }
              ]
            },
            password: {
              identifier  : 'password',
              rules: [
                {
                  type   : 'empty',
                  prompt : 'Parolanızı giriniz.'
                },
                {
                  type   : 'length[6]',
                  prompt : 'Parola karakteriniz en az 6 karakter olmalı.'
                }
              ]
            },
            name: {
                identifier  : 'name',
                rules: [
                  {
                    type   : 'empty',
                    prompt : 'adınızı giriniz.'
                  }
                ]
              },
              surname: {
                identifier  : 'surname',
                rules: [
                  {
                    type   : 'empty',
                    prompt : 'Soyadınızı giriniz.'
                  }
                ]
              }
          }
        })
      ;
    })
  ;
});