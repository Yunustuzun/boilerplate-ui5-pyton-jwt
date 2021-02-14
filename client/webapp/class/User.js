sap.ui.define([
    "sap/ui/base/Object",
    "boiler/ui5/jwt/class/Backend"
], function (
    BaseObject,
    Backend
) {
    "use strict";
    var instance;
    var user = BaseObject.extend("boiler.ui5.jwt.class.User", {

        constructor: function () {
            if (!this.instance) {
                this.instance = this;

            }
            return this.instance;
        },
        isAuthenticated: function () {
            return new Backend().request("POST", '/auth/status', {}).done((data) => {
                localStorage.setItem("token", data.token)
            })
        },
        signIn: function (userId, password) {
            return new Backend().request("POST", '/auth/signin', {
                UserID: userId,
                Password: password
            }).done((data) => {
                localStorage.setItem("token", data.token)
            })
        },
        signOut: function () {
            //TODO: Send register it is in blacklist
            localStorage.removeItem("token")
        }
    });

    return {
        getInstance: function () {
            if (!instance) {
                instance = new user();
            }
            return instance;
        }
    };
});