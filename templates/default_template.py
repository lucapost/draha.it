import time
import datetime

SITE_NAME = "Casa Draha"
SITEMAP = "sitemap.xml"
URL = "http://draha.it"
SRC = "/home/lucapost/repo/draha.it/src/"
TITLE = "Draha"
SUBTITLE = "Vacanze e B&B nelle Valli del Natisone"
DST = "./"
PREFIX = "/"
HOME = "/"
PATH_SEPARATOR = "/"

SRC_EXT = {"markdown": "md", "textile": "tt", "plain": "txt"}
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
        <meta name="google-translate-customization" content="b2d0413882278e06-5fc6a66e79b45ee8-g76640882c5a8ea73-8"></meta>
       	<meta name="author" content="Luca Postregna" />
	    <meta name="description" content="''' + SUBTITLE + '''" />
       	<title>''' + SITE_NAME + ''' | ''' + SUBTITLE + '''</title>
  		<meta name="viewport" content="width=device-width">
		<link rel="stylesheet" type="text/css" media="all" href="/css/reset.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/text.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/960.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/hashgrid.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" />
		<link href='http://fonts.googleapis.com/css?family=Fanwood+Text' rel='stylesheet' type='text/css'>
  		<script src="/js/modernizr.js"></script> 
		<script src="/js/jquery.min.js"></script>
  		<script src="/js/hashgrid.js"></script> 
		<script src="/js/flux.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript" charset="utf-8">
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
	</head>
	<body>
		<div id="top" class="container_12 clearfix">
            <menu>
                <header class="grid_3 prefix_6">
					<h1><a href="/" title="home page">Casa Draha</a></h1>
					<h2>Vacanze e B&B <br/>nelle Valli del Natisone</h2>
                </header>
                <nav class="grid_3">
                    <ul class="menu">
                        <li><a href="#alloggi" title="descrizione degli alloggi">Alloggi</a></li>
                        <li><a href="#giardino" title="descrizione del giardino">Giardino</a></li>
                        <li><a href="#info" title="informazioni generiche">Info</a></li>
                        <li><a href="#contatti" title="come contattarci">Contatti</a></li>
                    </ul>
                </nav>
            </menu>
            <div class="grid_12">
				<div id="slider">
                    <img src="/images/slider/00.jpg" title="1/28 la sala d'ingresso del b&b" alt="ingresso"/>
                    <img src="/images/slider/01.jpg" title="2/28 il soggiorno del b&b" alt="soggiorno"/>
					<img src="/images/slider/02.jpg" title="3/28 il soggiorno del b&b verso il caminetto" alt="soggiorno verso caminetto"/>
					<img src="/images/slider/03.jpg" title="4/28 il tavolo massiccio del soggiorno" alt="tavolo"/>
					<img src="/images/slider/04.jpg" title="5/28 il tavolo della cucina per le colazioni" alt="tavolo cucina"/>
					<img src="/images/slider/05.jpg" title="6/28 l'anticamera del b&b" alt="anticamera"/>
					<img src="/images/slider/06.jpg" title="7/28 la camera singola del b&b" alt="cameretta singola"/>
					<img src="/images/slider/07.jpg" title="8/28 la camera matrimoniale del b&b" alt="camera matrimoniale"/>
					<img src="/images/slider/08.jpg" title="9/28 il bagno del b&b" alt="bagno"/>
					<img src="/images/slider/09.jpg" title="10/28 la camera matrimoniale della casa vacanze" alt="camera matrimoniale casa vacanze"/>
					<img src="/images/slider/10.jpg" title="11/28 la camera matrimoniale nella casa vacanze" alt="camera matrimoniale"/>
					<img src="/images/slider/11.jpg" title="12/28 il bagno della casa vacanze" alt="bagno casa vacanze"/>
					<img src="/images/slider/12.jpg" title="13/28 la cucina della casa vacanze" alt="cucina casa vacanze"/>
					<img src="/images/slider/13.jpg" title="14/28 la finestra della cucina della casa vacanze" alt="la finestra"/>
					<img src="/images/slider/14.jpg" title="15/28 l'ingresso del b&b dall'esterno" alt="ingresso esterno"/>
					<img src="/images/slider/15.jpg" title="16/28 la casa dall'esterno" alt="casa"/>
					<img src="/images/slider/16.jpg" title="17/28 l'ingresso del b&b dal giardino" alt="ingresso dal giardino"/>
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
            <a href="http://www.tripadvisor.it/" title="scrivi una recensione su Casa Draha"><img src="/images/tripadvisor.png" alt="tripadvisor logo" title="scrivi una recensione su Casa Draha" class="grid_3 tripadvisor"/></a>
			<div class="grid_6">
                    <p><strong>Casa Draha</strong>, Vacanze e B&B nelle Valli del Natisone, di Teresa Postregna</p>
                    <p>Via Postregna 17, 33040 Stregna, Udine, Italy</p>
                    <p>email: <a href="mailto:info@draha.it">info@draha.it</a>, phone: +393337600975 (+390432724192)</p>
					<p class="last">&copy <a href="http://luca.postregna.name">lucapost</a> ''' + str(current_time.year) + ''', <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">license CC by-nc</a>, <a href="/privacy.html" title="normativa sulla privacy">privacy</a>, edit: ''' + time.strftime("%Y%m%d %I:%M:%S %p", node.page.last_edit) + '''</p>
			</div>
            <div class="grid_3 social">
                <a href="http://twitter.com/casadraha" title="pagina twitter di @CasaDraha"><img src="/images/twitter.png" alt="twitter logo" title="profilo twitter di @casadraha" class="grid_1 alpha social"/></a>
                <a href="https://plus.google.com/101321731330801126248/posts" title="pagina google plus di Casa Draha"><img src="/images/gplus.png" alt="google plus logo" title="profilo google plus" class="grid_1 social"/></a>
                <a href="https://www.facebook.com/pages/Casa-Draha/130267147110320" title="pagina facebook di Casa Draha"><img src="/images/facebook.png" alt="facebook logo" title="pagina fecbook di Casa Draha" class="grid_1 omega social"/></a>
                <div id="google_translate_element" class="grid_3"></div>
            </div>
			<div class="clear"></div>
		</footer>	
<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->
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
</body>
</html>'''	
