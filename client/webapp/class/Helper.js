sap.ui.define([
    "sap/ui/base/Object",
    'sap/m/MessageBox',
], function (
    BaseObject,
    MessageBox
) {
    "use strict";
    var instance;
    var helper = BaseObject.extend("boiler.ui5.jwt.class.Helper", {

        constructor: function () {
            if (!this.instance) {
                this.instance = this;
            }
            return this.instance;
        },
        createGuid() {
            function _p8(s) {
                var p = (Math.random().toString(16) + "000000000").substr(2, 8);
                return s ? "-" + p.substr(0, 4) + "-" + p.substr(4, 4) : p;
            }
            return _p8() + _p8(true) + _p8(true) + _p8();
        },
        getApiDomain: function () {


            if (!window.location.host.includes("localhost")) {
                return "xxxxxxxxxxxxx.herokuapp.com"
            }
            else {
                return "http://127.0.0.1:5000";
            }
        },
        cloneObject: function (object) {

            var b = {};
            let c = jQuery.extend(true, b, object);

            return c;

        },
        keepCloning: function (objectpassed) {
            if (objectpassed === null || typeof objectpassed !== 'object') {
                return objectpassed;
            }
            var temporaryStorage = objectpassed.constructor();
            for (var key in objectpassed) {
                temporaryStorage[key] = this.keepCloning(objectpassed[key]);
            }
            return temporaryStorage;
        },
        _dialogApprove: function (message, title, clb) {
            MessageBox.warning(message, {
                title: title,
                actions: [MessageBox.Action.OK, MessageBox.Action.CANCEL],
                emphasizedAction: MessageBox.Action.OK,
                onClose: (action) => {
                    if (action === "OK") {
                        clb();
                    }
                }
            });
        }
    });

    return {
        getInstance: function () {
            if (!instance) {
                instance = new helper();
            }
            return instance;
        }
    };
});