# Author:      Luca Postregna <luca.postregna@gmail.com>
# License:     CC, see LICENSE for details

import datetime

src_dir = "source"
dst_dir = "."
src_ext = {"markdown": "md", "textile": "textile"}
dst_ext = "html"
hidden = set(["404.textile"])
home = " "
path_separator = " "
current_time = datetime.datetime.now()

def header(node):
	"""Builds the header and returns it to a string."""

	return '''
	<!DOCTYPE HTML>
	<html>
	<head>
		<link rel="shortcut icon" href="/images/fav.ico" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" /> 
		<meta content="text/html; charset=UTF-8" http-equiv="content-type" />
		<meta name="author" content="Luca Postregna" />
		<meta name="keywords" content="teresa, postregna, bed, breakfast, b&amp;b, casa, vacanze, ferienhaus, dormire, camere, zimmer, stregna, valli, natisone, cividale, friuli" />
		<meta name="description" content="bed and breakfast e casa vacanze di Teresa Postregna, dormire a Stregna nelle Valli del Natisone in provincia di Udine " />
		<script type="text/javascript" src="/js/jquery.js" ></script>
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
		<title>Draha Oasi di Pace - b&amp;b</title>
	</head>
	<body>
		<div id="top" class="container_12">
			<div id="social" class="grid_3 prefix_1">	
				<g:plusone size="medium" count="false" href="http://bb.draha.it"></g:plusone>
				<a href="http://twitter.com/share" class="twitter-share-button"
					data-url="http://bb.draha.it"
					data-text="@bb_draha_it #bb #casavacenze #stregna #vallidelnatisone"
					data-count="none">
				Tweet</a> 
			</div>
			<div id="lang" class="prefix_4 grid_3 clearfix">
				<a href="/it"><div id="flag" class="it"></div></a><a href="/de"><div id="flag" class="de"></div></a>
			</div> 
			<div class="clear"></div>
		</div>
		<div id="container" class="container_12">
	'''
def footer(node):
	"""Builds the footer and returns it to a string."""
	return '''
		<div id="footer" class="grid_8 prefix_2">
				&copy; ''' + str(current_time.year) + ''' <a href="http://luca.postregna.name">Luca Postregna</a> ::
				update: ''' + str(current_time.strftime("%Y%m%d")) + ''' ::
				<a href="http://validator.w3.org/check?uri=referer">xhtml</a> <a href="http://jigsaw.w3.org/css-validator/check/referer">css</a>
			</div><!-- chiuso footer -->
			<div class="clear"></div>
		</div>
	</body>
</html>'''
