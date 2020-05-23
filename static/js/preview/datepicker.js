(function ($) {
  'use strict';
  
  $(document).ready(function() {
    $('.flatpickr').flatpickr();
    $("#flatpickr-disable-range").flatpickr({
      disable: [
        {
          from: "2016-08-16",
          to: "2016-08-19"
        },
        "2016-08-24",
        new Date().fp_incr(30) // 30 days from now
      ]
    });
  });
})(jQuery);
