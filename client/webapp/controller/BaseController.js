sap.ui.define([
	"sap/ui/core/mvc/Controller",
	"sap/ui/core/routing/History",
	"boiler/ui5/jwt/class/Helper",
	"sap/ui/core/BusyIndicator",
], function (Controller, History, Helper, BusyIndicator) {
	"use strict";

	return Controller.extend("boiler.ui5.jwt.controller.BaseController", {

		getPageData: function (path) {
			return this.getModel("page").getProperty(path);
		},
		setPageData: function (path, value) {
			return this.getModel("page").setProperty(path, value);
		},
		getRouter: function () {
			return this.getOwnerComponent().getRouter();
		},
		getHelper: function () {
			return Helper.getInstance();
		},
		getModel: function (sName) {
			return this.getView().getModel(sName);
		},
		setModel: function (oModel, sName) {
			return this.getView().setModel(oModel, sName);
		},
		getResourceBundle: function () {
			return this.getOwnerComponent().getModel("i18n").getResourceBundle();
		},
		onNavBack: function () {
			var sPreviousHash = History.getInstance().getPreviousHash();

			if (sPreviousHash !== undefined) {
				history.go(-1);
			} else {
				this.getRouter().navTo("master", {}, {}, true);
			}
		},
		hideBusyIndicator: function () {
			BusyIndicator.hide();
		},
		showBusyIndicator: function () {
			BusyIndicator.show();
		},
		getCookie: function (cname) {
            var name = cname + "=";
            var ca = document.cookie.split(';');
            for (var i = 0; i < ca.length; i++) {
                var c = ca[i];
                while (c.charAt(0) == ' ') {
                    c = c.substring(1);
                }
                if (c.indexOf(name) == 0) {
                    return c.substring(name.length, c.length);
                }
            }
            return null;
        },
        setCookie: function (cname, cvalue, exhours) {
            var d = new Date();
            d.setTime(d.getTime() + (exhours * 60 * 60 * 1000));
            var expires = "expires=" + d.toUTCString();
            document.cookie = cname + "=" + cvalue + ";" + expires;
        },
        clearCookie: function (cname) {
            document.cookie = cname + "=;expires=Thu; 01 Jan 1970";
        },
	});
});