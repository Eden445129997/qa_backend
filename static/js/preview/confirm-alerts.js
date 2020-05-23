(function ($) {
  'use strict';

  $(document).ready(function () {
    $('.example-p-1').on('click', function () {
      $.alert({
        title: 'Alert alert!',
        content: 'This is a simple alert. <br> with some <strong>HTML</strong> <em>contents</em>',
        icon: 'icon icon-info',
        animation: 'zoom',
        closeAnimation: 'zoom',
        closeIcon: true,
        draggable: false,
        buttons: {
          okay: {
            text: 'Okay',
            btnClass: 'btn-info'
          }
        }
      });
    });

    // confirmation
    $('.example-p-2').on('click', function () {
      $.confirm({
        title: 'A secure action',
        content: 'Its smooth to do multiple confirms at a time. <br> Click confirm or cancel for another modal',
        icon: 'icon icon-warning',
        animation: 'scale',
        closeAnimation: 'scale',
        opacity: 0.5,
        draggable: false,
        closeIcon: true,
        buttons: {
          'confirm': {
            text: 'Proceed',
            btnClass: 'btn-info',
            action: function () {
              $.confirm({
                title: 'This maybe critical',
                content: 'Critical actions can have multiple confirmations like this one.',
                icon: 'icon icon-warning',
                animation: 'zoom',
                closeAnimation: 'zoom',
                buttons: {
                  confirm: {
                    text: 'Yes, sure!',
                    btnClass: 'btn-danger',
                    action: function () {
                      $.alert('A very critical action <strong>triggered!</strong>');
                    }
                  },
                  cancel: function () {
                    $.alert('you clicked on <strong>cancel</strong>');
                  }
                }
              });
            }
          },
          cancel: function () {
            $.alert('you clicked on <strong>cancel</strong>');
          }
        }
      });
    });

    // prompt
    $('.example-p-7-1').on('click', function () {
      $.confirm({
        title: 'A simple form',
        content: '' +
        '<form action="" class="formName">' +
        '<div class="form-group">' +
        '<label>Enter something here</label>' +
        '<input type="text" placeholder="Your name" class="name form-control" required />' +
        '</div>' +
        '</form>',
        draggable: false,
        closeIcon: true,
        buttons: {
          sayMyName: {
            text: 'Say my name',
            btnClass: 'btn-success',
            action: function () {
              var input = this.$content.find('input#input-name');
              var errorText = this.$content.find('.text-danger');
              if (input.val() == '') {
                errorText.html('Please don\'t keep the name field empty!').slideDown(200);
                return false;
              } else {
                $.alert('Hello ' + input.val() + ', i hope you have a great day!');
              }
            }
          },
          later: function () {
            // do nothing.
          }
        }
      });
    });

    // alert types
    $('.example-p-70-type').on('click', function () {
      $.alert({
        title: 'Oh no',
        type: 'red',
        content: 'Something bad, bad happened.',
        draggable: false,
        closeIcon: true
      });
    });

    // background dismiss
    $('.example-p-3').on('click', function () {
      $.alert({
        title: 'Background dismiss',
        content: 'Click outside the modal to close it.',
        animation: 'top',
        closeAnimation: 'bottom',
        backgroundDismiss: true,
        closeIcon: true,
        draggable: false,
        buttons: {
          okay: {
            text: 'okay',
            btnClass: 'btn-info',
            action: function () {
              // do nothing
            }
          },
          cancelAction: {
            text: 'Cancel',
            action: function () {

            }
          }
        }
      });
    });

    // using as dialogs
    $('.example-p-4').on('click', function () {
      $.dialog({
        title: 'Title comes here',
        content: 'Just need a popup without buttons, <strong>no problem!</strong><br>' +
        '<h3>disable the buttons</h3>' +
        '<h4>and you get a dialog modal</h4>' +
        '<p><em>Well, that close icon is shown if no buttons are here (u need something to close the modal right), u can explicitly control that too.</em></p>' +
        '<button type="button" class="btn btn-success">Click me to change the content</button>',
        animation: 'scale',
        closeIcon: true,
        draggable: false,
        onOpen: function () {
          var that = this;
          this.$content.find('button').click(function () {
            that.setContent('As simple as that !');
          })
        }
      });
    });

    // asynchronous content
    $('.example-p-5').on('click', function () {
      $.dialog({
        title: 'Asynchronous content',
        content: 'url:data/alert-table.html',
        animation: 'zoom',
        columnClass: 'medium',
        closeAnimation: 'scale',
        backgroundDismiss: true,
        closeIcon: true,
        draggable: false
      });
    });

    // auto close
    $('.example-p-6').on('click', function () {
      $.confirm({
        title: 'Auto close',
        content: 'Some actions maybe critical, prevent it with the Auto close. This dialog will automatically trigger cancel after the timer runs out.',
        autoClose: 'cancelAction|10000',
        escapeKey: 'cancelAction',
        draggable: false,
        closeIcon: true,
        buttons: {
          confirm: {
            btnClass: 'btn-danger',
            text: 'Delete ben\'s account',
            action: function () {
              $.alert('You deleted Ben\'s account!');
            }
          },
          cancelAction: {
            text: 'Cancel',
            action: function () {
              $.alert('Ben just got saved!');
            }
          }
        }
      });
    });

    // key strokes
    $('.example-p-7').on('click', function () {
      $.confirm({
        title: 'Keystrokes',
        escapeKey: true, // close the modal when escape is pressed.
        content: 'Press the <strong>escape key</strong> to close the modal. That works.' +
        '<br> press <strong>enter key</strong> to trigger okay.' +
        '<br> press <strong>shift or ctrl key</strong> to trigger cancel.',
        backgroundDismiss: true, // for escapeKey to work, backgroundDismiss should be enabled.
        draggable: false,
        closeIcon: true,
        buttons: {
          okay: {
            keys: [
              'enter'
            ],
            action: function () {
              $.alert('<strong>Okay button</strong> was triggered.');
            }
          },
          cancel: {
            keys: [
              'ctrl',
              'shift'
            ],
            action: function () {
              $.alert('<strong>Cancel button</strong> was triggered.');
            }
          }
        }
      });
    });

    // alignment
    $('.example-pc-1').on('click', function () {
      $.confirm({
        title: 'Gracefully center aligned',
        content: '<p>You can add content and not worry about the alignment. The goal is to make a Interactive dialog!.</p>' +
        '<button type="button" class="btn btn-success">Click me to add more content</button> <span> <br></span> ',
        draggable: false,
        closeIcon: true,
        buttons: {
          someButton: {
            text: 'Add wow',
            btnClass: 'btn-success',
            action: function () {
              this.$content.find('span').append('<br>Wowww');
              return false; // prevent dialog from closing.
            }
          },
          someOtherButton: {
            text: 'Clear it',
            btnClass: 'btn-success',
            action: function () {
              this.$content.find('span').html('');
              return false; // prevent dialog from closing.
            }
          },
          close: function () {
            // lets the user close the modal.
          }
        },
        onOpen: function () {
          // onOpen attach the events.
          var that = this;
          this.$content.find('button').click(function () {
            that.$content.find('span').append('<br>This is awesome!!!!');
          });
        }
      });
    });

    // working with images
    // todo: images is not tested yet.
    $('.example-pc-2').on('click', function () {
      $.confirm({
        title: 'Adding images',
        content: 'Images from flickr <br><img src="https://c2.staticflickr.com/4/3891/14354989289_2eec0ba724_b.jpg" class="rounded img-fluid mt-1">',
        animation: 'zoom',
        animationClose: 'top',
        draggable: false,
        closeIcon: true,
        buttons: {
          confirm: {
            text: 'Add more',
            btnClass: 'btn-info',
            action: function () {
              this.$content.append('<img src="https://c2.staticflickr.com/6/5248/5240523362_8d6d315391_b.jpg" class="rounded img-fluid mt-1">');
              return false; // prevent dialog from closing.
            }
          },
          cancel: function () {
            // lets the user close the modal.
          }
        }
      });
    });

    // animations
    $(' .example-pc-3').on('click', function () {
      $.alert({
        title: 'Animations',
        content: 'jquery-confirm provides a lot of open &amp; close animations out of the box. <br>The best part is, you can add custom ones too.',
        animation: 'rotate',
        closeAnimation: 'right',
        draggable: false,
        closeIcon: true,
        buttons: {
          zoom: function () {
            this.setCloseAnimation('zoom');
          },
          rotate: function () {
            this.setCloseAnimation('rotate');
          },
          scale: function () {
            this.setCloseAnimation('scale');
          },
          top: function () {
            this.setCloseAnimation('top');
          }
        },
        backgroundDismiss: function () {
          return false;
        }
      });
    });

    $('.example-p-7-2').on('click', function () {
      $.alert({
        title: 'A draggable dialog',
        content: 'This dialog is draggable, use the title to drag it around. It wont touch the screen borders',
        type: 'info',
        draggable: true
      });
    });

    /**
     * Dialog types
     */
    $('.primary-dialog-example').on('click', function () {
      $.confirm({
        title: 'Primary!',
        content: 'Some content here.',
        draggable: false,
        type: 'primary',
        closeIcon: true,
        buttons: {
          confirm: {
            text: 'Ok',
            btnClass: 'btn-primary'
          },
          cancel: function () {

          }
        }
      });
    });

    $('.success-dialog-example').on('click', function () {
      $.confirm({
        title: 'Success!',
        content: 'Some content here.',
        draggable: false,
        closeIcon: true,
        type: 'success',
        buttons: {
          confirm: {
            text: 'Ok',
            btnClass: 'btn-success'
          },
          cancel: function () {

          }
        }
      });
    });

    $('.info-dialog-example').on('click', function () {
      $.confirm({
        title: 'Info!',
        content: 'Some content here.',
        draggable: false,
        type: 'info',
        closeIcon: true,
        buttons: {
          confirm: {
            text: 'Ok',
            btnClass: 'btn-info'
          },
          cancel: function () {

          }
        }
      });
    });

    $('.warning-dialog-example').on('click', function () {
      $.confirm({
        title: 'Warning!',
        content: 'Some content here.',
        draggable: false,
        closeIcon: true,
        type: 'warning',
        buttons: {
          confirm: {
            text: 'Ok',
            btnClass: 'btn-warning'
          },
          cancel: function () {

          }
        }
      });
    });

    $('.danger-dialog-example').on('click', function () {
      $.confirm({
        title: 'Danger!',
        content: 'Some content here.',
        type: 'danger',
        buttons: {
          confirm: {
            text: 'OK',
            btnClass: 'btn-danger'
          },
          cancel: function () {

          }
        }
      });
    });
  });
})(jQuery);
