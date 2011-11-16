$(function(){
	if(!flux.browser.supportsTransitions)
		alert("Flux Slider requires a browser that supports CSS3 transitions, please update to Firefox5+ or Chrome12+");
	window.slider = new flux.slider('#slider', {
		transitions: [ 'blocks2' ],
        	pagination: false,
		captions: true,
		delay: 5000,
                autoplay: true
	});
});
