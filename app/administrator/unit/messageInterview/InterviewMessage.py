


def messageInterview(data):

	defaultPesan = f""" 
							<div id="container"
                            style="
                            backgroundColor:#f4f4f9;
                            width: 80%;
                            margin: auto;
                            padding: 20px;
                            backgroundColor:#ffffff;
                            boxShadow:0 4px 8px rgba(0, 0, 0, 0.1);
                            borderRadius:8px;
                            " 
                            >
                                <h1>Panggilan Interview</h1>
                                <br>
                                <p>Halo <b id="nameKandidat">[Nama Kandidat]</b>,</p><br>

                                <p>Anda cocok dengan kualifikasi lowongan <b  id="nameLowongan">[Nama Lowongan]</b>yang kami butuhan dan Kami senang mengundang Anda untuk mengikuti sesi interview dengan tim kami.</p>
                                <p><strong>Detail Interview:</strong></p>
                                <br>
                                <ul>
                                    <li><strong>Tanggal:</strong> 12 Januari 2025</li>
                                    <li><strong>Waktu:</strong> 10:00 AM</li>
                                    <li><strong>Tempat:</strong> Kantor XYZ, Jl. Raya No. 123</li>
                                </ul><br>
                                <p>Harap membawa dokumen yang diperlukan dan persiapkan diri Anda sebaik mungkin.</p><br>
                                <ul>
                                    <li><strong>KTP:</strong></li>
                                    <li><strong>Waktu:</strong></li>
                                    <li><strong>Tempat:</strong></li>
                                </ul>
                                <br>
                                <p>Terima kasih, dan kami tunggu kehadiran Anda!</p>
                                <button id="confirmButton">Konfirmasi Kehadiran</button>
                            </div>
		"""
	return defaultPesan