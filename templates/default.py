author = "Luca Postregna"
path_separator = "/"
home = "/"
src_ext = {"textile": "textile"}
dst_ext = "html"
hidden = set(["404.textile", "500.textile"])
current_time = datetime.datetime.now()

def header(node):
	"""Builds the header and returns it to a string."""

	return '''
	<!DOCTYPE HTML>
	<html lang="''' + language + '''">
	<head>
		<title>''' + site_name + ' | ' + node.name + '''</title>
		<meta name="author" content="''' + author + '''" />
		<meta name="keywords" content="''' + keywords + ',' + node.name + '''" />
		<meta name="description" content="''' + description + ',' + node.name + '''" />
		<meta content="text/html; charset=UTF-8" http-equiv="content-type" />
		<link rel="shortcut icon" href="/images/fav.ico" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" /> 
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
		<script type="text/javascript" src="/js/hashgrid.js" ></script> 
		<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
		<script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>
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
			<nav class="grid_4"> 
				<a title="home" href="''' + prefix + '''"> 
					<div id="logo" class="alpha grid_2 pull_1"> 
						<h1> Draha <br/>Casa Vacanze</h1> 
						<img src="/images/logo.png" alt="" />
						<h1>Oasi di Pace <br/> B&amp;B</h1> 
					</div>
				</a> 
				<menu class="omega grid_2 pull_1 clearfix"> 
					%%%MENU%%%
				</menu>
				<div class="clear"></div>
			</nav>
			<footer class="grid_8 prefix_2">
				&copy; ''' + str(current_time.year) + ''' <a title="il blog di Luca Postregna" href="http://luca.postregna.name">Luca Postregna</a> ::
				<a title="Creative Commons licenes" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">license</a> ::
				update: ''' + str(current_time.strftime("%Y%m%d")) + ''' ::
				<a title="xhtml validator" href="http://validator.w3.org/check?uri=referer">xhtml</a> <a title="css validator" href="http://jigsaw.w3.org/css-validator/check/referer">css</a>
			</footer>
			<div class="clear"></div>
		</article>
	</body>
</html>'''
