 // Used to add a spinner to submit buttons
 var temp_button_text;
 function CustomFormSubmitPost(e) {
     var el = $(e);
     temp_button_text = el.attr("value")
     el.attr('disabled', 'disabled').attr("value", "Loading...");
 };
 function CustomFormSubmitResponse(e) {
     var el = $(e);
     el.removeAttr('disabled').attr("value", temp_button_text);
 };
 
 function getSubmitButton(form){
     return form.find(":submit")
 }
 
 
 function manageCart(url){
     $.ajax({
         url: url,
         method: "POST",
         success: function(json){
             ShowAlert(json["result"], json["message"], json["result"].toLowerCase(), json["redirect"]);
         },
         error: function(xhr){
             console.log(xhr.status + ": " + xhr.responseText);
         }
     })
 }

 function createSession(url){
    $.ajax({
        url: url,
        method: "POST",
        success: function(json){
            ShowAlert(json["result"], json["message"], json["result"].toLowerCase(), json["redirect"]);
        },
        error: function(xhr){
            console.log(xhr.status + ": " + xhr.responseText);
        }
    })
}
 
 function ajaxForm(form, data){
     var submit_button = getSubmitButton(form)
     console.log(data)
     $.ajax({
         url: form.attr("action"),
         method: form.attr("method"),
         data: data,
         success: function(json){
             CustomFormSubmitResponse(submit_button);
             form[0].reset()
             ShowAlert(json["result"], json["message"], json["result"].toLowerCase(), json["redirect"]);
         },
         error: function(xhr){
             CustomFormSubmitResponse(submit_button);
             console.log(xhr.status + ": " + xhr.responseText);
         }
     })
 }
 
  
 var CourseFunctions = function(){
     
     "use strict"
 
     var secureBasicForm = function () {
         var form = $('#securebasicform')
         var submit_button = getSubmitButton(form)
         form.submit(function(event){
             event.preventDefault();
             CustomFormSubmitPost(submit_button);
             grecaptcha.ready(function() {
                 grecaptcha.execute(recaptcha_site_key, {action: "/"}).then(function(token) {
                     document.getElementById('id_recaptcha_token').value = token;
                     var formdata = form.serialize() 
                     ajaxForm(form, formdata)
                 })
             })
         })    
     };

     var nlSecureBasicForm = function () {
        var form = $('#nlsecurebasicform')
        var submit_button = getSubmitButton(form)
        form.submit(function(event){
            event.preventDefault();
            CustomFormSubmitPost(submit_button);
            grecaptcha.ready(function() {
                grecaptcha.execute(recaptcha_site_key, {action: "/"}).then(function(token) {
                    document.getElementById('id_nl_recaptcha_token').value = token;
                    var formdata = form.serialize() 
                    ajaxForm(form, formdata)
                })
            })
        })    
    };

     
     /* Function ============ */
     return {
         init:function(){
             secureBasicForm();
             nlSecureBasicForm();
         },

     }
     
 }();
 
 /* Document.ready Start */	
 jQuery(document).ready(function() {
     'use strict';
     CourseFunctions.init();
     
 });
 
 $(function() {
     // This function gets cookie with a given name
     function getCookie(name) {
         var cookieValue = null;
         if (document.cookie && document.cookie != '') {
             var cookies = document.cookie.split(';');
             for (var i = 0; i < cookies.length; i++) {
                 var cookie = jQuery.trim(cookies[i]);
                 // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
     }
     var csrftoken = getCookie('csrftoken');
     function csrfSafeMethod(method) {
         // these HTTP methods do not require CSRF protection
         return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
     }
     function sameOrigin(url) {
         // test that a given url is a same-origin URL
         // url could be relative or scheme relative or absolute
         var host = document.location.host; // host + port
         var protocol = document.location.protocol;
         var sr_origin = '//' + host;
         var origin = protocol + sr_origin;
         // Allow absolute or scheme relative URLs to same origin
         return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
             (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
             // or any other URL that isn't scheme relative or absolute i.e relative.
             !(/^(\/\/|http:|https:).*/.test(url));
     }
     $.ajaxSetup({
         beforeSend: function(xhr, settings) {
             if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                 // Send the token to same-origin, relative URLs only.
                 // Send the token only if the method warrants CSRF protection
                 // Using the CSRFToken value acquired earlier
                 xhr.setRequestHeader("X-CSRFToken", csrftoken);
             }
         }
     });
 })
 