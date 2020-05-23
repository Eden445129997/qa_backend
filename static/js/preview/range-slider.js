(function ($) {
  'use strict';

  $(document).ready(function() {
    var noUiSliderTooltips = document.querySelector('.nouislider-tooltips');
    var nouislider = document.querySelector('.nouislider');
    var nouisliderCustom = document.querySelector('.nouislider-custom');
    var nouisliderA = $('#nouislider-a');
    var nouisliderA1 = $('#nouislider-a1');
    var nouisliderB = $('#nouislider-b');
    var nouisliderB1 = $('#nouislider-b1');
    var nouisliderB2 = $('#nouislider-b2');
    var nouisliderB3 = $('#nouislider-b3');

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

    if (nouisliderA.length) {
      noUiSlider.create(nouisliderA.get(0), {
        start: 50,
        connect: [true, false],
        range: {
          'min': 0,
          'max': 100
        }
      });
    }

    if (nouisliderA1.length) {
      noUiSlider.create(nouisliderA1.get(0), {
        start: 20,
        connect: true,
        tooltips: [wNumb({decimals: 0})],
        range: {
          'min': 0,
          'max': 100
        }
      });
    }

    if (nouisliderB.length) {
      noUiSlider.create(nouisliderB.get(0), {
        start: 50,
        connect: [true, false],
        range: {
          'min': 0,
          'max': 100
        }
      });
    }

    if (nouisliderB1.length) {
      noUiSlider.create(nouisliderB1.get(0), {
        start: [ 40, 60 ],
        behaviour: 'drag-tap',
        tooltips: [wNumb({decimals: 0}), wNumb({decimals: 0})],
        connect: true,
        range: {
          'min':  20,
          'max':  80
        }
      });
    }

    var rangeAllSliders = {
      'min': [     0 ],
      '10%': [   500,  500 ],
      '50%': [  4000, 1000 ],
      'max': [ 10000 ]
    };

    if (nouisliderB2.length) {
      noUiSlider.create(nouisliderB2.get(0), {
        range: rangeAllSliders,
        start: 0,
        pips: {
          mode: 'range',
          density: 3
        }
      })
    }

    var rangeSlidersNouisliderB3 = {
      'min': [ 0 ],
      'max': [ 100 ]
    };

    if (nouisliderB3.length) {
      noUiSlider.create(nouisliderB3.get(0), {
        range: rangeSlidersNouisliderB3,
        start: 0,
        pips: {
          mode: 'range',
          density: 3
        }
      })
    }
  });
})(jQuery);
