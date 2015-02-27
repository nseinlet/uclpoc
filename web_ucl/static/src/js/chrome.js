(function() {

var instance = openerp;

instance.web.Menu.include({
    bind_menu: function () {
        var self = this;
        this._super.apply(this, arguments);
        this.toggled = false;
        this.$('#leftbar-toggle').on('click', function (ev) {
            ev.preventDefault();
            if (!self.toggled) {
                self.toggled = true;
                $('.oe_leftbar').css('display', 'none');
            } else {
                self.toggled = false;
                $('.oe_leftbar').css('display', 'table-cell');
            }
        });
    },
    on_top_menu_click: function (ev) {
        this.toggled = false;
        this._super.apply(this, arguments);
    },
});

})();
