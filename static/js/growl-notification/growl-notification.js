var GrowlNotification = /** @class */ (function () {
    function GrowlNotification(options) {
        if (options === void 0) { options = {}; }
        this.options = {
            margin: 20,
            type: 'alert',
            title: '',
            description: '',
            image: '',
            closeTimeout: false,
            animation: {
                show: 'slide-in',
                close: 'slide-out'
            },
            animationDuration: .3,
            position: 'top-right'
        };
        this.template = "<span class=\"growl-notification__close\">\n     <span class=\"iconfont iconfont-alert-close\"></span>\n   </span>\n   {{ image }}\n   <div class=\"growl-notification__content\">\n     <div class=\"growl-notification__title\">{{ title }}</div>\n     <div class=\"growl-notification__desc\">{{ description }}</div>\n   </div>";
        this.options = this.mergeOptions(this.options, options);
    }
    GrowlNotification.prototype.show = function () {
        var _this = this;
        var self = this;
        var options = this.options;
        var top = this.options.margin;
        var notifications = [].slice.call(document.querySelectorAll('.growl-notification.position-' + this.options.position));
        notifications.slice().forEach(function (el) {
            top += (Number(el.clientHeight)) + _this.options.margin;
        });
        var body = document.querySelector('body');
        var newNotification = document.createElement('div');
        var template = this.template.replace('{{ title }}', options.title);
        template = template.replace('{{ image }}', options.image ? '<img src="' + options.image + '" alt="" class="growl-notification__image">' : '');
        template = template.replace('{{ description }}', options.description);
        newNotification.className = "growl-notification" + (options.type ? ' growl-notification--' + options.type : '');
        newNotification.className += (options.image ? ' growl-notification--image' : '');
        newNotification.className += ' animation-' + options.animation.show;
        this.addClass(newNotification, 'position-' + this.options.position);
        newNotification.innerHTML = template;
        var position = this.options.position.split('-'); //[0] - top,bottom, [1] - left,right
        newNotification.style[position[0]] = top + 'px';
        newNotification.style[position[1]] = this.options.margin + 'px';
        body.appendChild(newNotification);
        var closeBtn = newNotification.querySelector('.growl-notification__close');
        closeBtn.addEventListener('click', function () {
            self.close(newNotification);
        });
        if (options.closeTimeout && (options.closeTimeout > 0)) {
            setTimeout(function () {
                self.close(newNotification);
            }, options.closeTimeout);
        }
    };
    GrowlNotification.prototype.close = function (notification) {
        var self = this;
        this.removeClass(notification, 'animation-' + this.options.animation.show);
        this.addClass(notification, 'animation-' + this.options.animation.close);
        setTimeout(function () {
            self.remove(notification);
            self.recalculatePositions();
        }, this.options.animationDuration * 1000);
    };
    GrowlNotification.prototype.remove = function (notification) {
        notification.remove();
    };
    GrowlNotification.prototype.recalculatePositions = function () {
        var _this = this;
        var top = this.options.margin;
        var notifications = [].slice.call(document.querySelectorAll('.growl-notification.position-' + this.options.position));
        notifications.slice().forEach(function (el) {
            var position = _this.options.position.split('-'); //[0] - top,bottom, [1] - left,right
            el.style[position[0]] = top + 'px';
            top += (Number(el.clientHeight)) + _this.options.margin;
        });
    };
    GrowlNotification.prototype.mergeOptions = function (destination, source) {
        for (var property in source) {
            destination[property] = source[property];
        }
        return destination;
    };
    GrowlNotification.prototype.addClass = function (element, className) {
        var classNames = element.className.split(' ');
        classNames.push(className);
        element.className = classNames.join(' ');
    };
    GrowlNotification.prototype.removeClass = function (element, className) {
        var classNames = element.className.split(' ');
        var index = classNames.indexOf(className);
        if (index > -1) {
            classNames.splice(index, 1);
        }
        element.className = classNames.join(' ');
    };
    return GrowlNotification;
}());
