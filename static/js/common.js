/**
 * Created by alexy on 28.05.15.
 */
$(function() {
  $.validator.messages.required = "* поле обязательно для заполнения";

//  Модальные окна
  $('#js-auth-button').fancybox();
  $('.js-ticket-button').fancybox({
    afterClose: function (e) {
      $('.ticket-modal-form').trigger('reset');
      $('.ticket-form').trigger('reset');
    }
  });
  $('a.documents-gallery').fancybox();
  $('a.photo-gallery').fancybox();
  $('.review-slider').flexslider({
        animation: "slide",
        selector: ".review-slides > li",
        animationLoop: true,
        controlNav: false,
        //itemWidth: 800,
        itemMargin: 1,
        prevText: '<<',
        nextText: '>>'
    });

  // заполненяем поля модальной формы
  $('.js-ticket-button').on('click', function(e){
    var form = $(this).parent('form');

    if ($(this).data('group')){
      var group = $(this).data('group');
      //alert(group);
      $('.pop-form__group').val(group);
    }

    if (form.length != 0) {
      var name = form.find('.ticket-form__name').val();
      var email = form.find('.ticket-form__email').val();
      $('.ticket-modal-form__name').val(name);
      $('.ticket-modal-form__email').val(email);
    }
  });

  $.validator.messages.required = "* поле обязательно для заполнения";

  // валидация формы на странице
  $( ".js-ticket-form" ).validate({
    rules: {
      name: {
        required: true
      },
      email: {
        required: true
      }
    },
    messages: {
      name: "Введите ваше имя",
      email: {
        required: "Введите ваш email для обратной связи",
        email: "e-mail должен быть вида name@domain.com"
      }
    },
    submitHandler: function(e) {
      $('.js-ticket-form').ajaxSubmit({
          success: function(data){
            console.log(data.success);
            $.notify(data.success, 'success');
            $('.js-ticket-form').trigger('reset');
          }
      });
    }
  });

  // валидация формы на странице
  $( ".js-modal-ticket-form").validate({
    rules: {
      name: {
        required: true
      },
      email: {
        required: true
      }
    },
    messages: {
      name: "Введите ваше имя",
      email: {
        required: "Введите ваш email для обратной связи",
        email: "e-mail должен быть вида name@domain.com"
      }
    },
    submitHandler: function(e) {
      $('.js-modal-ticket-form').ajaxSubmit({
          success: function(data){
            console.log(data.success);
            $.notify(data.success, 'success');
            $.fancybox.close();
            $('.js-modal-ticket-form').trigger('reset');
          }
      });
    }
  });


});