sap.ui.define([
    "boiler/ui5/jwt/controller/BaseController",
    "boiler/ui5/jwt/class/Backend",
    "boiler/ui5/jwt/class/User"
], function (BaseController, Backend, User) {
    "use strict";

    return BaseController.extend("boiler.ui5.jwt.controller.Login", {
        onInit: function () {

        },
        onAfterRendering: function () {
            this._setDefaults();
        },
        onPressLogin: function () {
            let userName = jQuery("#username").val();
            let password = jQuery("#pass").val();

            User.getInstance().signIn(userName, password).done((data) => {
                this.getRouter().getTargets().display("home");
                this.getOwnerComponent().getModel("userModel").setData(data.info)
            })

        },
        onForgotPassword: function () {

        },
        _setDefaults: function () {

            function validate(input) {
                if ($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
                    if ($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                        return false;
                    }
                }
                else {
                    if ($(input).val().trim() == '') {
                        return false;
                    }
                }
            }

            function showValidate(input) {
                var thisAlert = $(input).parent();

                $(thisAlert).addClass('alert-validate');
            }

            function hideValidate(input) {
                var thisAlert = $(input).parent();

                $(thisAlert).removeClass('alert-validate');
            }

            // Login Button Event
            jQuery("#loginButton").on("click", this.onPressLogin.bind(this));

            // Attach CSS
            $.ajax({
                url: 'css/login/main.css',
                success: function (data) {
                    $("<style></style>").appendTo(".login-container").html(data);
                }
            });

            $.ajax({
                url: 'css/login/util.css',
                success: function (data) {
                    $("<style></style>").appendTo(".login-container").html(data);
                }
            });

            // Key Events
            jQuery("#inputPassword").on('keyup', function (event) {

                if (event.keyCode == 13) {
                    this._onPressLogin();
                }
            }.bind(this));

            jQuery("#inputPassword").on('keyup', function (event) {
                if (event.keyCode == 13) {
                    this._onPressLogin();
                }
            }.bind(this));


            // Validatiton
            var input = $('.validate-input .input100');

            $('.validate-form').on('submit', function () {
                var check = true;

                for (var i = 0; i < input.length; i++) {
                    if (validate(input[i]) == false) {
                        showValidate(input[i]);
                        check = false;
                    }
                }

                return check;
            });


            $('.validate-form .input100').each(function () {
                $(this).focus(function () {
                    hideValidate(this);
                });
            });

            // Show pass 
            var showPass = 0;
            $('.btn-show-pass').on('click', function () {
                if (showPass == 0) {
                    $(this).next('input').attr('type', 'text');
                    $(this).addClass('active');
                    showPass = 1;
                }
                else {
                    $(this).next('input').attr('type', 'password');
                    $(this).removeClass('active');
                    showPass = 0;
                }

            });

        },



    });
});