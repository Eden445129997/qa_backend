(function ($) {
  'use strict';

  $(document).ready(function() {
    $('.m-tasks__items').each(function () {
      Sortable.create(this, {
        group: ".m-tasks__items",
        sort: true,
        handle: '.m-tasks__item-name',
        animation: 150
      });
    });
  });
})(jQuery);
