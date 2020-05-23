(function ($) {
  'use strict';

  $(document).ready(function() {
    var formUpload = $('.form-upload');

    formUpload.on('dragover', function(e) {
        e.preventDefault();
        e.stopPropagation();


        /*if (!$(e.target).closest('.form-upload')) {
          $(this).removeClass('is-dragenter');
        }*/
      }
    );

    /*formUpload.on('dragleave', function(e) {
        e.preventDefault();
        e.stopPropagation();

        if (!e.originalEvent.clientX && !e.originalEvent.clientY) {
          console.log(22);
        }
      }
    );*/

    formUpload.on('dragenter', function(e) {
        e.preventDefault();
        e.stopPropagation();

        $(this).addClass('is-dragenter');
      }
    );

    formUpload.on('drop', function(e) {
        $(this).removeClass('is-dragenter');

        if (e.originalEvent.dataTransfer) {
          if (e.originalEvent.dataTransfer.files.length) {
            e.preventDefault();
            e.stopPropagation();

            upload(e.originalEvent.dataTransfer.files);
          }
        }
      }
    );

    function upload(files) {
      /*alert('Upload '+files.length+' File(s).');*/
    }
  });
})(jQuery);
