(function ($) {
  'use strict';

  $(document).ready(function() {
    var uploadChooseDefault = $('#upload-files-default').get(0);

    FileAPI.event.on(uploadChooseDefault, 'change', function (evt){
      var files = FileAPI.getFiles(evt); // Retrieve file list

      // Uploading Files
      FileAPI.upload({
        url: '/upload/',
        files: { files: files },
        progress: function (evt){ /* ... */ },
        complete: function (err, xhr){ /* ... */ }
      });
    });
  });
})(jQuery);
