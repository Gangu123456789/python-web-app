async function load(){
 const res = await fetch('/api/data');
 const data = await res.json();
 document.getElementById('title').innerText=data.site_overview.name;
 document.getElementById('desc').innerText=data.site_overview.description;
 const area=document.getElementById('solutions');
 data.solutions_catalog.forEach(c=>c.services.forEach(s=>{
   const el=document.createElement('div');
   el.className='card';
   el.innerHTML=`<h3>${s.title}</h3><p>${s.short_description}</p>`;
   area.appendChild(el);
 }));
}
load();