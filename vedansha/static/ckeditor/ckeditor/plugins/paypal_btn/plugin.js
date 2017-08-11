CKEDITOR.plugins.add('paypal_btn',{
  init: function(editor){
    var cmd = editor.addCommand('paypal_btn', {
      exec:function(editor){
        editor.insertHtml(
            '<form style="display: inline-block;" action="https://www.paypal.com/cgi-bin/webscr" class="btn-paypal" method="post" target="_top">' +
                '<input name="cmd" type="hidden" value="_s-xclick" />' +
                '<input name="hosted_button_id" type="hidden" value="28MW5BMZFA98Y" />' +
                '<input name="on0" type="hidden" value="Course advance fee" />' +
                '<button class="btn btn--orange" name="submit" title="PayPal – The safer, easier way to pay online!" type="submit"><em class="icon icon-paypal">&nbsp;</em>&ensp;Buy Now</button>' +
            '</form>'
        ); // собственно сама работа плагина
      }
    });
    cmd.modes = { wysiwyg : 1, source: 1 };// плагин будет работать и в режиме wysiwyg и в режиме исходного текста
    editor.ui.addButton('paypal_btn',{
      label: 'Add PayPal code',
      icon:this.path+'paypal.svg', // иконка
      command: 'paypal_btn'
    });
  }
});