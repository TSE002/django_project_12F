window.addEventListener("load", function() {
	let user = document.getElementById("login_felhasznalo");
	let password = document.getElementById("login_jelszo");
	let button = document.getElementById("login_btn");

	user.addEventListener("keyup", function(event) {
		if(event.keyCode == 13) {
			event.preventDefault();
			button.click();
		}
	})

	password.addEventListener("keyup", function(event) {
		if(event.keyCode == 13) {
			event.preventDefault();
			button.click();
		}
	});
});

