$(document).ready(function() {
	//Quando la pagina viene caricata
	$(".blocco-tab").hide(); //nascondi tutti i contenuti delle tabs
	$("ul.tabs li:first").addClass("active").show(); //Attiva la prima tab
	$(".blocco-tab:first").show(); //Mostra il contenuto della prima tab

	//Al click sulla linguetta della tab
	$("ul.tabs li").click(function() {
		$("ul.tabs li").removeClass("active"); //Rimuovi ogni classe "active"
		$(this).addClass("active"); //E aggiungila solo a quella su cui ho cliccato
		$(".blocco-tab").hide(); //Nascondi tutti i contenuti delle tab
	
		var activeTab = $(this).find("a").attr("href"); //Trova l'href per identificare in modo univoco la tab ed il contenuto
		$(activeTab).fadeIn(1000); //Mostrami quest'ultimo con effetto di fadeIn
		return false;
	});
});	
