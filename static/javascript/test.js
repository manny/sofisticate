document.addEventListener('DOMContentLoaded', function(){
	var button = document.getElementById('sofisticate');
	button.addEventListener('click', function(){
		FB.login(function(){
			FB.api('me/feed', 'post', {message: 'This is a test!'});
		}, {scope: 'publish_actions'});	
	});
});
