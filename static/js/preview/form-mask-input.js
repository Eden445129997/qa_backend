(function ($) {
  'use strict';

  $(document).ready(function () {
    var phoneMask = new IMask(
      document.getElementById('pattern-phone'), {
        mask: '+{1}(000)000-00-00',
        placeholder: {lazy: false}
      })
    ;

    var numberMask = new IMask(
      document.getElementById('number-mask'),
      {
        mask: Number,
        min: -10000,
        max: 10000,
        thousandsSeparator: ' '
      })
    ;

    var dateMask = new IMask(
      document.getElementById('date-mask'),
      {
        mask: Date,
        min: new Date(2000, 0, 1),
        max: new Date(2020, 0, 1),
        placeholder: {lazy: false}
      })
    ;

    var dynamicMask = new IMask(
      document.getElementById('dynamic-mask'),
      {
        mask: [
          {
            mask: '+{1}(000)000-00-00'
          },
          {
            mask: /^\S*@?\S*$/
          }
        ]
      })
    ;

    var timeMask = new IMask(
      document.getElementById('time-mask'), {
        mask: '00:00:00'
      })
    ;

    var creditCardMask = new IMask(
      document.getElementById('credit-card-mask'), {
        mask: '0000 0000 0000 0000'
      })
    ;

    var card = new Card({
      form: 'form',
      container: '.card-wrapper',

      formSelectors: {
        nameInput: 'input[name="first_name"], input[name="last_name"]'
      }
    });
  });
})(jQuery);
