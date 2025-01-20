


def messageInterview(data,alamat,date):

	defaultPesan = f""" 
	<div id="container" style="backgroundcolor: #f4f4f9; width: 100%; margin: auto; padding: 20px; backgroundcolor: #ffffff; boxshadow: 0 4px 8px rgba(0, 0, 0, 0.1); borderradius: 8px;">
	<h1>Panggilan Interview</h1>
	<br />
	<p>Halo <b id="nameKandidat">{data.user.complete_name}</b>,</p>
	<br />

	<p>Anda cocok dengan kualifikasi lowongan <b id="nameLowongan">{data.to.title}</b>yang kami butuhan dan Kami senang mengundang Anda untuk mengikuti sesi interview dengan tim kami.</p>
	<p><strong>Detail Interview:</strong></p>
	<br />
	<ul>
	<li><strong>Tanggal:</strong>{date.strftime("%d %B %G")}</li>
	<li><strong>Waktu:</strong>{date.strftime('%H.%M')} WIB</li>
	<li><strong>Tempat:</strong>{alamat}</li>
	</ul>
	<br />
	<p>Harap membawa dokumen yang diperlukan dan persiapkan diri Anda sebaik mungkin.</p>
	<br />
	<ul>
	<li><strong>Foto Copy KTP</strong></li>
	<li><strong>Ijazah / SKL</strong></li>
	<li><strong>Photo Formal</strong></li>
	<li><strong>Resume / CV</strong></li>
	<ul/>
	<br/>
	<p>Terima kasih, dan kami tunggu kehadiran Anda!</p>
	</div>

	"""
	return defaultPesan