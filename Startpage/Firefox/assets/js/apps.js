const displayApps = () => {
	var categories = {
		Social: {
			Quora: "https://www.quora.com",
			Reddit: "https://www.reddit.com",
			Twitter: "https://www.twitter.com",
			WhatsApp: "https://web.whatsapp.com",
			Instagram: "https://www.instagram.com",
		},
		Entertainment: {
			IMDb: "https://www.imdb.com",
			Netflix: "https://www.netflix.com",
			Hotstar: "https://www.hotstar.com",
			Justwatch: "https://www.justwatch.com",
			WatchSeries: "https://www.watchseries.pub",
		},
		Google: {
			Maps: "https://maps.google.com",
			Keep: "https://keep.google.com",
			Drive: "https://drive.google.com",
			Photos: "https://photos.google.com",
			Youtube: "https://www.youtube.com",
		},
		Finance: {
			SBI: "https://retail.onlinesbi.com/retail/login.htm",
			HDFC: "https://netbanking.hdfcbank.com/netbanking/",
			Paytm: "https://paytm.com/",
			Wazirx: "https://wazirx.com/exchange/BTC-INR",
			BookMyShow: "https://in.bookmyshow.com/explore/home/bhimavaram",
		},
		Mail: {
			General: "https://mail.google.com/mail/u/0/",
			College: "https://mail.google.com/mail/u/1/",
			Personal: "https://mail.google.com/mail/u/2/",
			Outlook: "https://outlook.office365.com/mail/",
			TempMail: "https://temp-mail.org/en/",
		},
	};

	const apps_div = document.querySelector(".apps");

	for (const category in categories) {
		let cat = document.createElement("div");
		cat.className = "category";
		let app_html = "";
		for (const app in categories[category]) {
			app_html += `<a href=${categories[category][app]}><img class=app-icon src="https://www.google.com/s2/favicons?domain=${categories[category][app]}">${app}</a>`;
		}
		console.log(app_html);
		cat.innerHTML = `<h3>${category}</h3>`;
		cat.innerHTML += app_html;
		apps_div.appendChild(cat);
	}
};

window.onload = displayApps();
