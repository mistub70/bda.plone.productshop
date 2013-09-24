$(document).ready(function()  {
  $('div.variations > .False').hide();   
  var selected = '.' + $('#fronted').val() + ' input';
  $('#fronted').hide();
  $($(selected)).click();
  $("#filter input").click(function() {
       var $value = 'div.variations div.' + $(this).val();
       $('div.variations > div').hide();      
       $($value).show();          
  });
});
