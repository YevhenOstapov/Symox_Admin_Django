/*
  Name: Symox - Admin & Dashboard  
Author: Themesbrand
Website: https://Themesbrand.com/
Contact:  andzukor@gmail.com
File: Email summernote Js File
*/

ClassicEditor
    .create( document.querySelector( '#email-editor' ) )
    .then( function(editor) {
        editor.ui.view.editable.element.style.height = '200px';
    })
    .catch( function(error) {
        console.error( error );
    });