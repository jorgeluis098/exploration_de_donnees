$(document).ready(function (){

	$("#button_pearson").click(function(event){
		event.preventDefault();
		var formData = new FormData($('#form_pearson')[0]);
		$.ajax({
			url: '/read_pearson',
			data: formData,
			type: 'POST',
			contentType: false,
			processData: false,
			success: function(response){
				$('#matrizPearson').html(response['keyPearson'])				
			},
			error: function(error){
				console.log(error);
				event.preventDefault();
			}
		});    
	});


});


