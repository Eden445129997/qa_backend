(function ($) {
  'use strict';

  $(document).ready(function () {
    $('#show-notification-mint-alert').on('click', function () {
      new Noty({
        type: 'alert',
        text: 'Some notification text',
        theme: 'mint'
      }).show();
    });

    $('#show-notification-mint-success').on('click', function () {
      new Noty({
        type: 'success',
        text: 'Some notification text',
        theme: 'mint'
      }).show();
    });

    $('#show-notification-mint-error').on('click', function () {
      new Noty({
        type: 'error',
        text: 'Some notification text',
        theme: 'mint'
      }).show();
    });

    $('#show-notification-mint-warning').on('click', function () {
      new Noty({
        type: 'warning',
        text: 'Some notification text',
        theme: 'mint'
      }).show();
    });

    $('#show-notification-mint-info').on('click', function () {
      new Noty({
        type: 'info',
        text: 'Some notification text',
        theme: 'mint'
      }).show();
    });
  });
})(jQuery);
