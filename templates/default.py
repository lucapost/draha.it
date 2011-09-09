author = "Luca Postregna"
path_separator = "/"
home = "/"
src_ext = {"textile": "textile"}
dst_ext = "html"
hidden = set(["404.textile", "500.textile", "privacy.textile"])
current_time = datetime.datetime.now()

def header(node):
	"""Builds the header and returns it to a string."""

	return '''<!doctype html>
	<!-- paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ -->
	<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="''' + language + '''"> <![endif]-->
	<!--[if IE 7]>    <html class="no-js ie7 oldie" lang="''' + language + '''"> <![endif]-->
	<!--[if IE 8]>    <html class="no-js ie8 oldie" lang="''' + language + '''"> <![endif]-->
	<!-- Consider adding a manifest.appcache: h5bp.com/d/Offline -->
	<!--[if gt IE 8]><!--> <html class="no-js" lang="''' + language + '''"> <!--<![endif]-->
	<head>
		<meta charset="utf-8">
		<!-- Use the .htaccess and remove these lines to avoid edge case issues.
		     More info: h5bp.com/b/378 -->
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<title>''' + site_name + ' | ' + node.name + '''</title>
		<meta name="author" content="''' + author + '''" />
		<meta name="keywords" content="''' + keywords + ',' + node.name + '''" />
		<meta name="description" content="''' + description + ',' + node.name + '''" />

		<!-- Mobile viewport optimized: j.mp/bplateviewport -->
	  	<meta name="viewport" content="width=device-width,initial-scale=1">

	  	<!-- Place favicon.ico and apple-touch-icon.png in the root directory: mathiasbynens.be/notes/touch-icons -->

	  	<link rel="stylesheet" href="/css/style.css">
  
	  	<!-- More ideas for your <head> here: h5bp.com/d/head-Tips -->
		<link rel="stylesheet" type="text/css" media="all" href="/css/custom.css" /> 

	  	<!-- All JavaScript at the bottom, except this Modernizr build incl. Respond.js
		      	Respond is a polyfill for min/max-width media queries. Modernizr enables HTML5 elements & feature detects; 
       			for optimal performance, create your own custom Modernizr build: www.modernizr.com/download/ -->
  		<script src="/js/libs/modernizr-2.0.6.min.js"></script>
	</head>
	<body>
		<div id="top" class="container_12">
			<div id="googleplus" class="grid_1 prefix_1">
				<g:plusone size="medium"></g:plusone> 
			</div>
			<div id="twitter" class="grid_2">
				<a title="share on twitter" href="http://twitter.com/share" data-url="http://bb.draha.it" data-text="#vallidelnatisone #stregna #bb" class="twitter-share-button">Tweet</a>
			</div>
			<div class="grid_5"><p class="hide">select language</p></div>
			<div class="grid_1" id="flagit">
				<a href="/benvenuti.html" title="switch to italian language"><p class="hide">it</p></a> 
			</div>
			<div class="grid_1" id="flagde">
				<a href="/de/willkommen.html" title="switch to deutsch language"><p class="hide">de</p></a> 
			</div>
			<div id="clear"></div>
		</div><!-- end top -->
		<article class="container_12">
			<section id="main" class="grid_6 prefix_1">
	'''
def footer(node):
	"""Builds the footer and returns it to a string."""
	return '''
			</section>
			<nav class="grid_4 pull_1 clearfix"> 
				<div id="logo">
					<a title="home" href="''' + prefix + '''"> 
						<h1> Draha <br/>Casa Vacanze</h1> 
						<img src="/images/logo.png" alt="" />
						<h1>Oasi di Pace <br/> B&amp;B</h1> 
					</a> 
				</div>
				<menu> 
					%%%MENU%%%
				</menu>
			</nav>
			<footer class="grid_8 prefix_2">
				&copy; ''' + str(current_time.year) + ''' <a title="il blog di Luca Postregna" href="http://luca.postregna.name">Luca Postregna</a> ::
				<a title="Creative Commons licenes" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">license</a> ::
				<a title="Privacy" href="/privacy.html">privacy</a> ::
				update: ''' + str(current_time.strftime("%Y%m%d")) + ''' ::
				<a title="xhtml validator" href="http://validator.w3.org/check?uri=referer">xhtml</a> <a title="css validator" href="http://jigsaw.w3.org/css-validator/check/referer">css</a>
			</footer>
			<div class="clear"></div>
		</article>

  		<!-- JavaScript at the bottom for fast page loading -->

  		<!-- Grab Google CDN's jQuery, with a protocol relative URL; fall back to local if offline -->
  		<script src="//ajax.googleapis.com/ajax/libs/jquery/1.6.3/jquery.min.js"></script>
  		<script>window.jQuery || document.write('<script src="/js/libs/jquery-1.6.3.min.js"><\/script>')</script>

  		<!-- scripts concatenated and minified via build script -->
  		<script defer src="/js/plugins.js"></script>
  		<script defer src="/js/script.js"></script>
		<!-- end scripts -->

		<script type="text/javascript" src="/js/hashgrid.js" ></script> 
		<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
		<script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>
		<script type="text/javascript">
			$(document).ready(function(){
			$('#main').fadeIn(2000);
			});
		</script>
		<script type="text/javascript" src="/js/jquery.lightbox-0.5.min.js"></script>
		<script type="text/javascript">
		$(function() {
			$('#gallery a').lightBox({fixedNavigation:true});
			});
		</script>

  		<!-- Asynchronous Google Analytics snippet. Change UA-XXXXX-X to be your site's ID.
       			mathiasbynens.be/notes/async-analytics-snippet -->
		<script>
			var _gaq=[['_setAccount','UA-6164762-7'],['_trackPageview'],['_trackPageLoadTime']];
    			(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
    			g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
    			s.parentNode.insertBefore(g,s)}(document,'script'));
  		</script>

  		<!-- Prompt IE 6 users to install Chrome Frame. Remove this if you want to support IE 6.
       			chromium.org/developers/how-tos/chrome-frame-getting-started -->
  		<!--[if lt IE 7 ]>
    			<script defer src="//ajax.googleapis.com/ajax/libs/chrome-frame/1.0.3/CFInstall.min.js"></script>
    			<script defer>window.attachEvent('onload',function(){CFInstall.check({mode:'overlay'})})</script>
  		<![endif]-->
	</body>
</html>'''
