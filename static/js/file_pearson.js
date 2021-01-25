$(document).ready(function (){
	// $("#button_apriory").click(function(){
	// 	console.log("Hola bebe");
	// 	event.preventDefault();
	// });

	$("#button_pearson").click(function(event){
		event.preventDefault();
		var formData = new FormData($('#form_pearson')[0]);
		console.log("Hola bebe entre a leer el archivo");
		$.ajax({
			url: '/read_pearson',
			data: formData,
			type: 'POST',
			contentType: false,
			processData: false,
			success: function(response){
				console.log(response)
				console.log(response['keyPearson']);
				$('#matrizPearson').html(response['keyPearson'])				
			},
			error: function(error){
				console.log(error);
				event.preventDefault();
			}
		});    
	});


});


