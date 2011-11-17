$(function(){
	if(!flux.browser.supportsTransitions)
		alert("Flux Slider requires a browser that supports CSS3 transitions, please update to Firefox5+ or Chrome12+");
	window.slider = new flux.slider('#slider', {
		transitions: [ 'blocks2' ],
        	pagination: false,
		captions: true,
		delay: 6000,
                autoplay: true
	});
	$('#controls').bind('click', function(event) {
	        event.preventDefault();
	        var command = 'window.mf.'+event.target.id+'();';
        	eval(command);
	});
});
