var Notification = /** @class */ (function () {
    function Notification() {
    }
    Notification.show = function (options) {
        var top = 20;
        var notifications = [].slice.call(document.querySelectorAll('.notification'));
        notifications.slice().forEach(function (el) {
            top += (Number(el.clientHeight)) + 20;
        });
        var template = "<span class=\"notification__close\">\n        <span class=\"iconfont iconfont-alert-close\"></span>\n      </span>\n      {{ image }}\n      <div class=\"notification__content\">\n        <div class=\"notification__title\">{{ title }}</div>\n        <div class=\"notification__desc\">{{ description }}</div>\n      </div>";
        var body = document.querySelector('body');
        var div = document.createElement('div');
        template = template.replace('{{ title }}', options.title);
        template = template.replace('{{ image }}', options.image ? '<img src="' + options.image + '" alt="" class="notification__image">' : '');
        template = template.replace('{{ description }}', options.description);
        div.className = "notification" + (options.type ? ' notification--' + options.type : '');
        div.className += (options.image ? ' notification--image' : '');
        div.innerHTML = template;
        div.style['top'] = top + 'px';
        body.appendChild(div);
        this.openedNotificationsCount++;
    };
    Notification.openedNotificationsCount = 0;
    return Notification;
}());
