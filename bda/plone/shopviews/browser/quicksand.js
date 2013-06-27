$(document).ready(function(){
 
 // Custom sorting plugin
 // not done yet, more here:
 // http://razorjack.net/quicksand/demos/one-set-clone.html
  (function($) {
	$.fn.sorted = function(customOptions) {
		var options = {
			by: function(a) { return a.text(); }
		};
		$.extend(options, customOptions);
		$data = $(this);
		arr = $data.get();
		return $(arr);
	};
  });
 
  // DOMContentLoaded
  $(function() {
  
	// bind radiobuttons in the form
	var $filterType = $('#filter input[name="type"]');
	var $filterSort = '';
	
	// get the first collection
	var $quicksandbox = $('#shopitems');
	
	// clone quicksandbox to get a second collection
	var $data = $quicksandbox.clone();

	// attempt to call Quicksand on every form change
	$filterType.add($filterSort).change(function(e) {
		if ($($filterType+':checked').val() == 'all') {
			var $filteredData = $data.find('li');
		} else {
			var $filteredData = $data.find('.' + $($filterType+":checked").val());
		}
	
	  // no sorting until price is an index
		var $sortedData = $filteredData; 

		
		// finally, call quicksand
		$quicksandbox.quicksand($sortedData, {
			duration: 800, 
			easing: 'easeInOutQuad' 
		});
	});
  });
});