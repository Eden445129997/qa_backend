(function ($) {
  'use strict';

  $(document).ready(function() {
    var filesScrollWrap = new SimpleBar($('.m-file-manager__content-files-scrollpane').get(0));

    $('.m-file-manager__content-view-control').on('click', function () {
      $('.m-file-manager__content-view-control').removeClass('is-active');

      var view = $(this).data('view');

      if (view === 'grid') {
        $('.m-file-manager__content-body').removeClass('m-file-manager__content-compact-mode');
      } else if (view === 'list') {
        $('.m-file-manager__content-body').addClass('m-file-manager__content-compact-mode');
      }

      filesScrollWrap.recalculate();

      $(this).addClass('is-active');

      return false;
    });
  });
})(jQuery);
