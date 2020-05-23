(function ($) {
  'use strict';

  $(document).ready(function() {
    var noUiSliderTooltips = document.querySelector('.nouislider-tooltips');
    var nouislider = document.querySelector('.nouislider');
    var nouisliderCustom = document.querySelector('.nouislider-custom');

    if (noUiSliderTooltips) {
      noUiSlider.create(noUiSliderTooltips, {
        start: [20, 80],
        connect: true,
        tooltips: [wNumb({decimals: 0}), wNumb({decimals: 0})],
        range: {
          'min': 0,
          'max': 100
        }
      });
    }

    if (nouislider) {
      noUiSlider.create(nouislider, {
        start: 0,
        connect: [true, false],
        range: {
          'min': 0,
          'max': 100
        }
      });
    }

    if (nouisliderCustom) {
      noUiSlider.create(nouisliderCustom, {
        start: 50,
        connect: [true, false],
        range: {
          'min': 0,
          'max': 100
        }
      });
    }
  });
})(jQuery);
