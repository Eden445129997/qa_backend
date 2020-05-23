(function($) {
  'use strict';

  // -------------------------------------------------------------------------------------------------
  // NAVBAR SEARCH ................ Navbar search
  // SIDEBAR NAV .................. Sidebar nav
  // -------------------------------------------------------------------------------------------------

  $(document).ready(function() {
    initSidebarScrollbar(),
    navbarSearch();
    sidebarNav();
    select2();
    flatpickr();
    tooltips();
    sidebarCollapse();
  });

  // -------------------------------------------------------------------------------------------------
  // NAVBAR SEARCH
  // -------------------------------------------------------------------------------------------------

  function navbarSearch() {
    $('.navbar-search__input').click(function(e) {
      e.preventDefault();
      var el = $(this);
      el.parent().addClass('focus');
    });
    $(document).click(function(e) {
      var el = $('.form-control');
      if (!el.is(e.target) && el.parent().has(e.target).length === 0) {
        el.parent().removeClass('focus');
      }
    });
  }

  // -------------------------------------------------------------------------------------------------
  // SIDEBAR
  // -------------------------------------------------------------------------------------------------

  function sidebarNav() {
    $('.sidebar-nav__link').on('click', function(event) {
      var el = $(this);
      var isActive = el.parent().hasClass('is-active');

      $('.sidebar-nav__item').removeClass('is-active');

      if (!isActive) {
        el.parent().addClass('is-active');
      }

      if ($('body').hasClass('sidebar-sm') || $('body').hasClass('sidebar-md')) {
        var offsetTop = 0;

        if ($('body').hasClass('sidebar-sm')) {
          offsetTop = $('.sidebar').position().top + el.offset().top - $('body').scrollTop() - el.closest('.sidebar-nav__item').height() - 1;
        } else if ($('body').hasClass('sidebar-md')) {
          offsetTop = $('.sidebar').position().top + el.position().top + el.closest('.sidebar-nav__item').height();
        }

        $('.sidebar-subnav').not(el.next()).slideUp(0);
        el.next().slideToggle(0);
        el.next().css('top', offsetTop);
      } else {
        $('.sidebar-subnav').not(el.next()).slideUp(150);
        el.next().slideToggle(150);
      }

      //localStorage.setItem('navItem', elIndex);

      setTimeout(function () {
        $(document).trigger('recalculate-sidebar-scroll');
      }, 200);

      if (el.closest('.sidebar-nav__item').find('.sidebar-subnav').length) {
        return false;
      }
    });
  }

  $('.sidebar-section-nav__link').on('click', function(event) {
    var el = $(this);
    var isActive = el.parent().hasClass('is-active');

    $('.sidebar-section-nav__item').removeClass('is-active');

    if (!isActive) {
      el.parent().addClass('is-active');
    }

    if ($('body').hasClass('sidebar-sm') || $('body').hasClass('sidebar-md')) {
      var offsetTop = 0;

      if ($('body').hasClass('sidebar-sm')) {
        offsetTop = $('.sidebar-section').position().top + el.offset().top - $('body').scrollTop() - el.closest('.sidebar-section-nav__item').height() - 1;
      } else if ($('body').hasClass('sidebar-md')) {
        offsetTop = $('.sidebar-section').position().top + el.position().top + el.closest('.sidebar-section-nav__item').height();
      }

      $('.sidebar-section-subnav').not(el.next()).slideUp(0);
      el.next().slideToggle(0);
      el.next().css('top', offsetTop);
    } else {
      $('.sidebar-section-subnav').not(el.next()).slideUp(150);
      el.next().slideToggle(150);
    }

    setTimeout(function () {
      $(document).trigger('recalculate-sidebar-scroll');
    }, 200);

    if (el.closest('.sidebar-section-nav__item').find('.sidebar-section-subnav').length) {
      return false;
    }
  });

  function select2() {
    $('select').each(function () {
      var options = {
        placeholder: function() {
          var el = $(this);
          el.data('placeholder');
        }
      };

      if (!$(this).is('[data-search-enable]')) {
        options['minimumResultsForSearch'] = Infinity;
      }

      $(this).select2(options);
    });

    function formatUsers(user) {
      if (!user.id) { return user.text; }
      var $user = $(
        '<span class="select-user__img"><img src="img/users/' + user.element.value.toLowerCase() + '.png" /></span><span class="select-user__name">' + user.text + '</span>'
      );
      return $user;
    }

    $(".select-user").select2({
      dropdownCssClass: "select-user-dropdown",
      templateSelection: formatUsers,
      templateResult: formatUsers,
      minimumResultsForSearch: Infinity
    });

    $('.select2').click(function(e) {
      var el = $(this);
      el.find('b').hide();
    });
  }

  function flatpickr() {
    $('.flatpickr').flatpickr({
      altInput: true
    });
  }

  function tooltips() {
    $('[data-toggle="tooltip"]').tooltip();
  }

  function toggleSidebar() {
    $('body').toggleClass('sidebar-sm');

    if ($('body').hasClass('sidebar-sm')) {
      initSidebarScrollbar(false);
    } else {
      initSidebarScrollbar(true);
    }

    setTimeout(function () {
      $(document).trigger('recalculate-sidebar-scroll');
    }, 200);
  }

  function sidebarCollapse() {
    $('.sidebar__collapse').on('click', function () {
      toggleSidebar();
    });
  }

  $(document).on('collapse-sidebar', function () {
    toggleSidebar();
  });

  /**
   * Scroll for any element
   */
  $('.js-scrollable').each(function () {
    new SimpleBar(this);
  });

  function initSidebarScrollbar() {
    var autoHide = true;

    if ($('body').hasClass('sidebar-sm') || $('body').hasClass('sidebar-md')) {
      autoHide = false;
    }

    if ($('.sidebar').length) {
      /**
       * Scroll for sidebar
       */
      if ($('.sidebar').css('position') === 'fixed') {
        var sidebarScroll = new SimpleBar($('.sidebar__scroll').get(0), {
          autoHide: autoHide
        });

        sidebarScroll.getScrollElement().addEventListener('scroll', function() {
          if ($('body').hasClass('sidebar-sm')) {
            $('.sidebar-subnav').hide();
            $('.sidebar-nav__item').removeClass('is-active');
          }
        });
      }
    }


    if ($('.sidebar-section').length) {
      /**
       * Scroll for section sidebar
       */
      if ($('.sidebar-section').css('position') === 'fixed') {
        var sidebarSectionScroll = new SimpleBar($('.sidebar-section__scroll').get(0), {
          autoHide: autoHide
        });

        sidebarSectionScroll.getScrollElement().addEventListener('scroll', function() {
          if ($('body').hasClass('sidebar-sm')) {
            $('.sidebar-section-subnav').hide();
            $('.sidebar-section-nav__item').removeClass('is-active');
          }
        });
      }
    }
  }

  $('.textavatar').each(function () {
    $(this).textAvatar({
      width: $(this).data('width'),
      height: $(this).data('height')
    });
  });

  $('.sidebar-toggler').on('click', function () {
    $('body').toggleClass('sidebar-is-opened');
  });

  $(document).on('click', function (e) {
    if ($('body').hasClass('sidebar-is-opened') && !$(e.target).closest('.sidebar-toggler').length) {
      if (!$(e.target).closest('.sidebar').length) {
        $('body').removeClass('sidebar-is-opened');
      }
    }

    if ($('.navbar-collapse').hasClass('show') && !$(e.target).closest('.navbar-toggler').length) {
      if (!$(e.target).closest('.navbar-collapse').length) {
        $('.navbar-collapse').removeClass('show');
        $('body').removeClass('is-navbar-opened');
      }
    }

    // Hide sidebar submenu if sidebar collapsed
    if ($('body').hasClass('sidebar-sm') || $('body').hasClass('sidebar-md')) {
      if (!$(e.target).closest('.sidebar').length) {
        $('.sidebar-subnav').hide();
        $('.sidebar-nav__item').removeClass('is-active');
      }
    }
  });

  $('.navbar-toggler').on('click', function () {
    $('body').toggleClass('is-navbar-opened');
  });

  if ($('.preloader').length) {
    setTimeout(function () {
      $('.preloader').fadeOut(0);
      $('body').removeClass('js-loading');
    }, 1500);
  }

  $('.color-checkbox :checkbox').on('change', function () {
    var parent = $(this).closest('.color-checkbox');

    if (this.checked) {
      parent.addClass('is-checked');
    } else {
      parent.removeClass('is-checked');
    }
  });

  $('.color-radio :radio').on('click', function () {
    var parent = $(this).closest('.color-radio');
    var name = $(this).attr('name');

    $('.color-radio input[name="' + name + '"]').each(function () {
      $(this).closest('.color-radio').removeClass('is-checked');
    });

    parent.addClass('is-checked');
  });

  $('.btn').on('mouseup', function () {
    var self = this;

    setTimeout(function () {
      self.blur();
    }, 500);
  });

  $('.js-datepicker').flatpickr();
  $('[data-toggle="popover"]').popover()
})(jQuery);
