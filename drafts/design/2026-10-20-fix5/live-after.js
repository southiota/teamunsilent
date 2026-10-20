(()=>{
const V=[['ktrl-ttuk','한강 뚝섬','DR.KTRL','한강 뚝섬 사일런트 디스코, DR.KTRL 현장 영상'],
['lify-calling','한강 반포','LiFY','한강 반포 사일런트 디스코, LiFY 현장 영상'],
['kali-jamsu','한강 잠수교 · 밤','KALI','한강 잠수교 사일런트 디스코, KALI 현장 영상'],
['ktrl-incheon','밤마다 인천 FESTA','DR.KTRL','밤마다 인천 FESTA 무소음 DJ 파티, DR.KTRL 현장 영상'],
['lify-seori','서초 서리풀 페스티벌','LiFY','서초 서리풀 페스티벌, LiFY 현장 영상'],
['kali-apt','한강 마포대교','KALI','한강 마포대교 사일런트 디스코, KALI 현장 영상']];
document.querySelector('.vids').innerHTML=V.map(v=>`<figure class="vid rv in"><video data-src="vid/clips/${v[0]}.mp4" poster="vid/clips/${v[0]}.jpg" muted loop playsinline preload="none" aria-label="${v[3]}"></video><span class="tag">LIVE</span><figcaption>${v[1]}<small>${v[2]} · 사일런트 디스코</small></figcaption></figure>`).join('');
const T1=['live2/c180','live2/kt20','live3/kali_sac_crowd','live2/c048','live3/lify_banpo_night','live2/c050','live2/c073','live2/c123','live3/lify_mapo_point','live3/team_cheonan'];
const T2=['live2/c112','live/e_gwang_ktrl','live2/c077','live/e_seori2','live3/lify_cheonan1','live2/c014','live2/c080','live/s_k1','live2/kt12','live2/c352'];
const tr=document.querySelectorAll('.track');
const f=(a)=>a.map(s=>`<figure><img src="img/${s}.webp" alt=""></figure>`).join('')+a.map(s=>`<figure aria-hidden="true"><img src="img/${s}.webp" alt=""></figure>`).join('');
tr[0].innerHTML=f(T1);tr[1].innerHTML=f(T2);
})()
