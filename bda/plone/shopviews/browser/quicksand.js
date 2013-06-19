$(document).ready(function(){

	// Clone shopitems items to get a second collection for Quicksand plugin
	var $shopitemsClone = $(".shopitems").clone();
	
	// Attempt to call Quicksand on every click event handler
	$(".filter a").click(function(e){
		
		$(".filter li").removeClass("current");	
		
		// Get the class attribute value of the clicked link
		var $filterClass = $(this).parent().attr("class");

		if ( $filterClass == "all" ) {
			var $filteredshopitems = $shopitemsClone.find("li");
		} else {
			var $filteredshopitems = $shopitemsClone.find("li[data-type~=" + $filterClass + "]");
		}
		
		// Call quicksand
		$(".shopitems").quicksand( $filteredshopitems, { 
			duration: 800, 
			easing: 'easeInOutQuad' 
		}, function(){
		});

		$(this).parent().addClass("current");

	})
});