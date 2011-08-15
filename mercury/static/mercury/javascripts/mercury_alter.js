// TODO: don't hardcode, move to more appropriate place (config, but Mercury isn't known there yet, so provide it as an option)
Mercury.saveURL =  '/mercury/save_content';//'{% url mercury-save-content %}';

// replace the save method
Mercury.PageEditor.prototype.save = function() {
    var __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

    var data, url, _ref, _ref2;
    url = (_ref = (_ref2 = this.saveUrl) != null ? _ref2 : Mercury.saveURL) != null ? _ref : this.iframeSrc();
    data = this.serialize();
    var headers =  {};
    headers[Mercury.csrfTag] = Mercury.csrfToken;

    Mercury.log('saving', data);
    if (this.options.saveStyle !== 'form') {
        data = jQuery.toJSON(data);
    }
    return jQuery.ajax(url, {
        type: 'POST',
        headers: headers,
        data: {
            content: data
        },
        success: __bind(function() {
            return Mercury.changes = false;
        }, this),
        error: __bind(function() {
            return alert("Mercury was unable to save to the url: " + url);
        }, this)
    });
};

