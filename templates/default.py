author = "Luca Postregna"
path_separator = "/"
prefix = "/"
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
		<meta name="keywords" content="''' + keywords + '''" />
		<meta name="description" content="''' + description + '''" />
		<meta content="text/html; charset=UTF-8" http-equiv="content-type" />
		<link rel="shortcut icon" href="/images/fav.ico" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" /> 
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
		<script type="text/javascript" src="/js/hashgrid.js" ></script> 
		<script type="text/javascript" src="/js/block.js" ></script> 
		<script type="text/javascript" src="/js/jquery.prettyPhoto.js" ></script>
		<script type="text/javascript" src="/js/pretty-init.js" ></script>
		<script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>
		<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
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
				<a href="/" title="switch to italian language"><p class="hide">it</p></a> 
			</div>
			<div class="grid_1" id="flagde">
				<a href="/de" title="switch to deutsch language"><p class="hide">de</p></a> 
			</div>
			<div id="clear"></div>
		</div><!-- end top -->
		<div id="container" class="container_12">
	'''
def footer(node):
	"""Builds the footer and returns it to a string."""
	return '''
			<div id="footer" class="grid_8 prefix_2">
				&copy; ''' + str(current_time.year) + ''' <a title="il blog di Luca Postregna" href="http://luca.postregna.name">Luca Postregna</a> ::
				update: ''' + str(current_time.strftime("%Y%m%d")) + ''' ::
				<a title="xhtml validator" href="http://validator.w3.org/check?uri=referer">xhtml</a> <a title="css validator" href="http://jigsaw.w3.org/css-validator/check/referer">css</a>
			</div><!-- chiuso footer -->
			<div class="clear"></div>
		</div>
	</body>
</html>'''
