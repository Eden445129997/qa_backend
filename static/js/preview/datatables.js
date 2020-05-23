(function ($) {
  'use strict';

  $(document).ready(function() {
    var table = $('#datatable').DataTable({
      lengthChange: false,
      buttons: [
        'print', 'excel', 'pdf', 'colvis'
      ],
      select: true,
      lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]]
    });
    table.buttons().container().appendTo('#datatable_wrapper .col-md-6:eq(0)');
  });
})(jQuery);
