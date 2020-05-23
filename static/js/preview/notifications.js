(function ($) {
  'use strict';

  $(document).ready(function () {
    $('#show-notification-default-alert').on('click', function () {
      var n = new GrowlNotification({
        title: 'Hello!',
        description: 'I am a default notification. I am a default notification. I am a default notification. I am a default notification.',
        position: 'bottom-right'
      });
      n.show();
    });

    $('#show-notification-default-success').on('click', function () {
      var n = new GrowlNotification({
        title: 'Well Done!',
        description: 'You just submit your resume successfully.',
        type: 'success',
        position: 'top-left'
      });
      n.show();
    });

    $('#show-notification-default-error').on('click', function () {
      var n = new GrowlNotification({
        title: 'Warning!',
        description: 'The data presentation here can be change.',
        type: 'error',
        position: 'bottom-left'
      });
      n.show();
    });

    $('#show-notification-default-warning').on('click', function () {
      var n = new GrowlNotification({
        title: 'Reminder!',
        description: 'You have a meeting at 10:30 АМ',
        type: 'warning'
      });
      n.show();
    });

    $('#show-notification-default-info').on('click', function () {
      var n = new GrowlNotification({
        title: 'Sorry!',
        description: 'Could not complete your transaction.',
        image: 'img/notifications/05.png',
        type: 'info'
      });
      n.show();
    });

    $('#show-notification-icon-alert').on('click', function () {
      var n = new GrowlNotification({
        title: 'Hello!',
        description: 'I am a default notification.',
        image: 'img/notifications/01.png'
      });
      n.show();
    });

    $('#show-notification-icon-success').on('click', function () {
      var n = new GrowlNotification({
        title: 'Well Done!',
        description: 'You just submit your resume successfully.',
        image: 'img/notifications/03.png',
        type: 'success'
      });
      n.show();
    });

    $('#show-notification-icon-error').on('click', function () {
      var n = new GrowlNotification({
        title: 'Warning!',
        description: 'The data presentation here can be change.',
        image: 'img/notifications/04.png',
        type: 'error'
      });
      n.show();
    });

    $('#show-notification-icon-warning').on('click', function () {
      var n = new GrowlNotification({
        title: 'Reminder!',
        description: 'You have a meeting at 10:30 АМ',
        image: 'img/notifications/02.png',
        type: 'warning'
      });
      n.show();
    });

    $('#show-notification-icon-info').on('click', function () {
      var n = new GrowlNotification({
        title: 'Sorry!',
        description: 'Could not complete your transaction.',
        image: 'img/notifications/05.png',
        type: 'info'
      });
      n.show();
    });
  });
})(jQuery);
