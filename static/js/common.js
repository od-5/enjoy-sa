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


});