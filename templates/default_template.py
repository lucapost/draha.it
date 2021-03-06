import time
import datetime

SITE_NAME = "Casa Draha"
SITEMAP = "./dst/sitemap.xml"
URL = "https://draha.it"
SRC = "/home/lucapost/repo/draha.it/src/"
TITLE = "Draha"
SUBTITLE = "Vacanze e B&amp;B a Stregna nelle Valli del Natisone "
DST = "./dst/"
PREFIX = "/"
HOME = "/"
PATH_SEPARATOR = "/"

SRC_EXT = {"markdown": "md", "textile": "textile", "plain": "txt"}
DST_EXT = "html"
HIDDEN = set(["404.md"])

current_time = datetime.datetime.now()

def header(node):
    """Build the header and return it to a string."""

    return '''<!DOCTYPE html>
	<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="it"> <![endif]-->
	<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="it"> <![endif]-->
	<!--[if IE 8]>    <html class="no-js lt-ie9" lang="it"> <![endif]-->
	<!--[if gt IE 8]><!--> <html class="no-js" lang="it"> <!--<![endif]-->
	<head>
       	<meta charset="utf-8" />
        <meta name="google-translate-customization" content="b2d0413882278e06-5fc6a66e79b45ee8-g76640882c5a8ea73-8" />
       	<meta name="author" content="Luca Postregna" />
	    <meta name="description" content="''' + SUBTITLE + ''' - ''' + node.page.name + '''" />
        <meta name="keywords" content="casa vacanze, B&amp;B, Bed and Breakfast, valli del natisone, stregna, giardino">
       	<title>''' + SITE_NAME + ''' - ''' + SUBTITLE + ''' </title>
  		<meta name="viewport" content="width=device-width">
		<link rel="stylesheet" type="text/css" media="all" href="/css/reset.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/text.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/960.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/hashgrid.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/ouibounce.min.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" />
		<link href="//cdn-images.mailchimp.com/embedcode/slim-081711.css" rel="stylesheet" type="text/css">
		<link href='https://fonts.googleapis.com/css?family=Fanwood+Text' rel='stylesheet' type='text/css'>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js"></script>
  		<script src="/js/modernizr.min.js"></script> 
  		<script src="/js/hashgrid.js"></script> 
		<script type="text/javascript" src="/js/ouibounce.min.js"></script>
	</head>
	<body>
		<div class="socialbutton">	
			<div class="tt-share">
                		<a href="https://twitter.com/share" class="twitter-share-button" data-url="https://draha.it" data-lang="it" data-count="vertical">Tweet</a>
			</div>
            		<div class="g-plusone" data-size="tall" data-href="https://plus.google.com/108792283838853337639/about"></div><br/>
			<iframe src="//www.facebook.com/plugins/like.php?href=https%3A%2F%2Fwww.facebook.com%2Fcasadraha&amp;width&amp;layout=box_count&amp;action=like&amp;show_faces=true&amp;share=false&amp;height=65&amp;appId=706061039456171" scrolling="no" frameborder="0" style="border:none; overflow:hidden; height:65px;" allowTransparency="true"></iframe>
		</div>
	    <div id="top" class="container_12 clearfix">
            <div class="menu">
                <header class="grid_3 prefix_6">
					<h1><a href="/" title="home page">Casa Dra<span>h</span>a</a></h1>
					<h2>Vacanze e B&amp;B a Stregna<br/>nelle Valli del Natisone</h2>
                </header>
                <nav class="grid_3">
                    <ul>
                        <li><a href="/#alloggi" title="descrizione degli alloggi">Alloggi</a></li>
                        <li><a href="/#giardino" title="descrizione del giardino">Giardino</a></li>
                        <li><a href="/#info" title="informazioni generiche">Info</a></li>
                        <li><a href="/#contatti" title="come contattarci">Contatti</a></li>
                        <li><a href="/#newsletter" title="Iscriviti alla Newsletter" class="newsletter">Newsletter!</a></li>
                    </ul>
                </nav>
            </div>
            <div class="grid_12">
				<div id="slider">
                    			<img src="/images/slider/00.jpg" title="1/28 la sala d'ingresso del b&amp;b" alt="ingresso"/>
                    			<img src="/images/slider/01.jpg" title="2/28 il soggiorno del b&amp;b" alt="soggiorno"/>
					<img src="/images/slider/02.jpg" title="3/28 il soggiorno del b&amp;b verso il caminetto" alt="soggiorno verso caminetto"/>
					<img src="/images/slider/03.jpg" title="4/28 il tavolo massiccio del soggiorno" alt="tavolo"/>
					<img src="/images/slider/04.jpg" title="5/28 il tavolo della cucina per le colazioni" alt="tavolo cucina"/>
					<img src="/images/slider/05.jpg" title="6/28 l'anticamera del b&amp;b" alt="anticamera"/>
					<img src="/images/slider/06.jpg" title="7/28 la camera singola del b&amp;b" alt="cameretta singola"/>
					<img src="/images/slider/07.jpg" title="8/28 la camera matrimoniale del b&amp;b" alt="camera matrimoniale"/>
					<img src="/images/slider/08.jpg" title="9/28 il bagno del b&amp;b" alt="bagno"/>
					<img src="/images/slider/09.jpg" title="10/28 la camera matrimoniale della casa vacanze" alt="camera matrimoniale casa vacanze"/>
					<img src="/images/slider/10.jpg" title="11/28 la camera matrimoniale nella casa vacanze" alt="camera matrimoniale"/>
					<img src="/images/slider/11.jpg" title="12/28 il bagno della casa vacanze" alt="bagno casa vacanze"/>
					<img src="/images/slider/12.jpg" title="13/28 la cucina della casa vacanze" alt="cucina casa vacanze"/>
					<img src="/images/slider/13.jpg" title="14/28 la finestra della cucina della casa vacanze" alt="la finestra"/>
					<img src="/images/slider/14.jpg" title="15/28 l'ingresso del b&amp;b dall'esterno" alt="ingresso esterno"/>
					<img src="/images/slider/15.jpg" title="16/28 la casa dall'esterno" alt="casa"/>
					<img src="/images/slider/16.jpg" title="17/28 l'ingresso del b&amp;b dal giardino" alt="ingresso dal giardino"/>
					<img src="/images/slider/17.jpg" title="18/28 il balcone fiorito" alt="balcone"/>
					<img src="/images/slider/18.jpg" title="19/28 vista del giardino nei pressi dell'ingresso" alt="giardino"/>
					<img src="/images/slider/19.jpg" title="20/28 il giardino all'ingresso" alt="giardino all'ingresso"/>
					<img src="/images/slider/20.jpg" title="21/28 il dondolo e la fontana nel giardino" alt="dondolo e fontana"/>
					<img src="/images/slider/21.jpg" title="22/28 il dondolo e la fontana del giardino" alt="dondolo e fontana"/>
					<img src="/images/slider/22.jpg" title="23/28 le sdraio in giardino" alt="le sdraio in giardino"/>
					<img src="/images/slider/23.jpg" title="24/28 particolare di pietra in giardino" alt="pietra"/>
					<img src="/images/slider/24.jpg" title="25/28 la panca di legno in giardino" alt="panca"/>
					<img src="/images/slider/25.jpg" title="26/28 gli scalini di pietra del giardino" alt="scalini"/>
					<img src="/images/slider/26.jpg" title="27/28 vista panoramica di giorno verso valle" alt="vista di giorno"/>
					<img src="/images/slider/27.jpg" title="28/28 vista panoramica al tramonto verso valle" alt="vista al tramonto"/>
				</div>
            </div>
			<div class="clear"></div>
		</div>
		<section class="container_12 clearfix items">
            <div class="grid_12">
			'''
def footer(node):
    """Build the footer and return it to a string."""

    return '''
            </div>
			<div class="clear"></div>
		</section>
		<footer class="container_12 clearfix">
			<div class="grid_3">
				<p>ci scrivi una recensione?</p>
				<a href="http://www.tripadvisor.it/Hotel_Review-g3374478-d4544610-Reviews-Casa_Draha-Stregna_Province_of_Udine_Friuli_Venezia_Giulia.html" title="scrivi una recensione su Casa Draha"><img src="/images/tripadvisor.png" alt="tripadvisor logo" title="scrivi una recensione su Casa Draha" class="tripadvisor"/></a>
			</div>
			<div class="grid_6">
				<p class="calltoaction"><a href="mailto:info@draha.it?subject=prenotazione soggiorno dal ... al ..." alt="scrivi una email a casadraha">scrivici una email e prenota il tuo soggiorno</a></p>
		    		<p class="footercontacts">telefono: <a class="phone" href="tel:+393337600975" title="numero di telefono casa draha">(+39)3337600975</a> - email: <a href="mailto:info@draha.it" title="indirizzo email casa draha">info@draha.it</a></p>
                		<p class="address">Via Postregna 17, 33040 Stregna, Udine, Italy</p>
			</div>
            <div class="grid_3 social">
                <a href="https://twitter.com/casadraha" title="pagina twitter di @CasaDraha"><img src="/images/twitter.png" alt="twitter logo" title="profilo twitter di @casadraha" class="grid_1 alpha social"/></a>
                <a href="https://plus.google.com/+CasaDrahaStregna" title="pagina google plus di Casa Draha"><img src="/images/gplus.png" alt="google plus logo" title="profilo google plus" class="grid_1 social"/></a>
                <a href="https://www.facebook.com/casadraha" title="pagina facebook di Casa Draha"><img src="/images/facebook.png" alt="facebook logo" title="pagina fecbook di Casa Draha" class="grid_1 omega social"/></a>
                <div id="google_translate_element" class="grid_3"></div>
            </div>
	    <div class="grid_12">
		<p class="last">&copy; <a href="https://luca.postregna.name">lucapost</a> ''' + str(current_time.year) + ''', <a rel="license" href="https://creativecommons.org/licenses/by-nc/3.0/">license</a>, <a href="/privacy.html" title="normativa sulla privacy">privacy</a>, edit: ''' + time.strftime("%Y%m%d %I:%M", node.page.last_edit) + '''</p>
	    </div> 
			<div class="clear"></div>
		</footer>	
<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->
    		<script src="/js/flux.min.js" type="text/javascript" charset="utf-8"></script>
	    	<script type="text/javascript">
		    	$(function(){
			    	if(!flux.browser.supportsTransitions)
				    	alert("Flux Slider requires a browser that supports CSS3 transitions");
    				window.f = new flux.slider('#slider', {
    					pagination: false,
                        controls: true,
                        captions: true,
    					transitions: [ 'dissolve' ],
    					delay: 5500
    				});
    			});
    		</script> 
            <script type="text/javascript">
               function googleTranslateElementInit() {
                new google.translate.TranslateElement({pageLanguage: 'it', includedLanguages: 'en,de,fr', layout: google.translate.TranslateElement.InlineLayout.SIMPLE, autoDisplay: false, multilanguagePage: true}, 'google_translate_element');
                }
            </script>
            <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
            <script type="text/javascript">
              var _gaq = _gaq || [];
              _gaq.push(['_setAccount', 'UA-6164762-7']);
              _gaq.push(['_trackPageview']);
              (function() {
                  var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                  ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                  var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
            })();
            </script>
            <script type="text/javascript">
                window.___gcfg = {lang: 'it'};
                (function() {
                var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
                po.src = 'https://apis.google.com/js/plusone.js';
                var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
                })();
            </script>
            <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="https://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>


    <div id="ouibounce-modal">
    <div class="underlay"></div>
    <div class="modal">
    <div class="modal-title">
    <h3>Newsletter</h3>
    </div>
    <div class="modal-body">
<p>Ricevi notizie sugli eventi e le offerte di Casa Draha:</p>
<div id="mc_embed_signup">
<form action="//draha.us3.list-manage.com/subscribe/post?u=9a891f3ce811f3a5542c15596&amp;id=c319375be9" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
    <div id="mc_embed_signup_scroll">
	
	<input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="indirizzo email" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;"><input type="text" name="b_9a891f3ce811f3a5542c15596_c319375be9" tabindex="-1" value=""></div>
    <div><input type="submit" value="Iscriviti" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
    	</div>
    </div>
    </div>
    <script>
    // if you want to use the 'fire' or 'disable' fn,
    // you need to save OuiBounce to an object
    var _ouibounce = ouibounce(document.getElementById('ouibounce-modal'), {
      aggressive: true,
      timer: 0,
      callback: function() { console.log('ouibounce fired!'); }
    });
    $('body').on('click', function() {
      $('#ouibounce-modal').hide();
    });
    $('#ouibounce-modal .modal-footer').on('click', function() {
      $('#ouibounce-modal').hide();
    });
    $('#ouibounce-modal .modal').on('click', function(e) {
      e.stopPropagation();
    });
    </script>


</body>
</html>'''
