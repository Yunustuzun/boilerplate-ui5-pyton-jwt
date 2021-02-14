sap.ui.define([
	"sap/ui/core/UIComponent",
	"sap/ui/Device",
	"./model/models",
	"boiler/ui5/jwt/class/User"
	// "./controller/ErrorHandler"
], function (UIComponent, Device, models, User) {
	"use strict";

	return UIComponent.extend("boiler.ui5.jwt.Component", {

		metadata: {
			manifest: "json"
		},
		/**
		 * The component is initialized by UI5 automatically during the startup of the app and calls the init method once.
		 * In this method, the device models are set and the router is initialized.
		 * @public
		 * @override
		 */
		init: function () {

			this.setModel(models.createDeviceModel(), "device");
			this.setModel(models.createUserModel(), "userModel");


			UIComponent.prototype.init.apply(this, arguments);
			this.getRouter().initialize();

			User.getInstance().isAuthenticated().done((data) => {
				this.getRouter().getTargets().display("home");
				this.getModel("userModel").setData(data.info);
			}).fail(() => {

				this.getRouter().getTargets().display("login");
			})

		},
		destroy: function () {
			// this._oErrorHandler.destroy();
			// call the base component's destroy function
			UIComponent.prototype.destroy.apply(this, arguments);
		},

		/**
		 * This method can be called to determine whether the sapUiSizeCompact or sapUiSizeCozy
		 * design mode class should be set, which influences the size appearance of some controls.
		 * @public
		 * @return {string} css class, either 'sapUiSizeCompact' or 'sapUiSizeCozy' - or an empty string if no css class should be set
		 */
		getContentDensityClass: function () {
			if (this._sContentDensityClass === undefined) {
				// check whether FLP has already set the content density class; do nothing in this case
				if (document.body.classList.contains("sapUiSizeCozy") || document.body.classList.contains("sapUiSizeCompact")) {
					this._sContentDensityClass = "";
				} else if (!Device.support.touch) { // apply "compact" mode if touch is not supported
					this._sContentDensityClass = "sapUiSizeCompact";
				} else {
					// "cozy" in case of touch support; default for most sap.m controls, but needed for desktop-first controls like sap.ui.table.Table
					this._sContentDensityClass = "sapUiSizeCozy";
				}
			}
			return this._sContentDensityClass;
		}

	});
});
