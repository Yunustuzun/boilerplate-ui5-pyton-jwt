sap.ui.define([
	"./BaseController",
	"sap/ui/model/json/JSONModel",
	"boiler/ui5/jwt/class/User"
], function (BaseController,
	JSONModel,
	User
) {
	"use strict";

	return BaseController.extend("boiler.ui5.jwt.controller.Home", {

		formatInitial: function (nameSurname) {
			if (nameSurname) {
				return nameSurname.substring(0, 2).toUpperCase();
			}
		},
		onInit: function () {
		},
		onAfterRendering: function () {
		},
		onSignout: function () {
			let clb = () => {
				User.getInstance().signOut();
				this.getOwnerComponent().getModel("userModel").setData();
				this.getRouter().getTargets().display("login");
			}
			this.getHelper()._dialogApprove("Çıkış yapmak istediğinize emin misiniz?", "Uyarı", clb)
		},
	});
});