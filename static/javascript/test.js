document.addEventListener('DOMContentLoaded', function(){
	var button = document.getElementById('sofisticate');
	console.log(message);
	button.addEventListener('click', function(){
		FB.login(function(response){
			console.log(response)
			FB.getLoginStatus(function (response) {
				FB.api('me/feed', 'post',{message: message, link: link}, function(response){
					console.log(response);
				});
		});
		}, {scope: 'publish_actions,public_profile,email,publish_stream', return_scopes: true});	
	});
});
