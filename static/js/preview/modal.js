(function ($) {
  'use strict';

  $(document).ready(function() {
    var tagEditor = new Tagify($('#tag-editor-invite').get(0));

    noUiSlider.create($('#mic-boost').get(0), {
      start: 40,
      connect: [true, false],
      range: {
        'min': 0,
        'max': 100
      }
    });

    noUiSlider.create($('#adjust-volume').get(0), {
      start: 50,
      connect: [true, false],
      range: {
        'min': 0,
        'max': 100
      }
    });
  });
})(jQuery);
