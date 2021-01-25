$(document).ready(function (){
	// $("#button_apriory").click(function(){
	// 	console.log("Hola bebe");
	// 	event.preventDefault();
	// });

	$("#button_distancias").click(function(event){
		event.preventDefault();
		var formData = new FormData($('#form_distancias')[0]);
		formData.append('distances', $('#select_distancias').val() )
		console.log("Hola bebe entre a leer el archivo");
		$.ajax({
			url: '/read_distancias',
			data: formData,
			type: 'POST',
			contentType: false,
			processData: false,
			success: function(response){
				console.log(response)
				console.log(response['keyDistancias']);
				$('#matrizDistancias').html(response['keyDistancias'])	
				$('#matrizDistanciass').DataTable();			
			},
			error: function(error){
				console.log(error);
				event.preventDefault();
			}
		});    
	});


});


