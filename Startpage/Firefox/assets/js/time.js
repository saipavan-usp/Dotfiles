const displayTime = () => {
	var date = new Date();
	var hh = date.getHours();
	var mm = date.getMinutes();
	var ss = date.getSeconds();
	var dt = date.toDateString();

	document.querySelector("#hours").innerHTML = formatTime(hh);
	document.querySelector("#mins").innerHTML = formatTime(mm);
	document.querySelector("#secs").innerHTML = formatTime(ss);
	document.querySelector("#date").innerHTML = dt;
	document.querySelector("#sep1").innerHTML = ":";
	document.querySelector("#sep2").innerHTML = ":";

	setTimeout(displayTime, 1000);
};

const formatTime = (n) => {
	return n < 10 ? "0" + n : n;
};

window.onload = displayTime();
