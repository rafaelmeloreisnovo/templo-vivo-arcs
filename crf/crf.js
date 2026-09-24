"use strict";
const state={data:null,filter:"ALL",query:""};

function asText(value){
  if(Array.isArray(value)) return value.length ? value.join("\n") : "";
  if(value===null || value===undefined) return "";
  return String(value);
}
function make(tag,className,text){
  const el=document.createElement(tag);
  if(className) el.className=className;
  if(text!==undefined) el.textContent=text;
  return el;
}
function field(label,value){
  const box=make("div","field");
  box.append(make("strong","",label));
  const text=asText(value);
  box.append(text ? make("code","",text) : make("span","empty","TOKEN_VAZIO / não materializado"));
  return box;
}
function render(){
  if(!state.data) return;
  const q=state.query.trim().toLowerCase();
  const rows=state.data.items.filter(item=>{
    const matchFilter=state.filter==="ALL" || item.readiness===state.filter;
    const hay=[item.id,item.title,item.kind,item.expression,...(item.gaps||[])].join(" ").toLowerCase();
    return matchFilter && (!q || hay.includes(q));
  });
  const host=document.querySelector("#items");
  host.replaceChildren();
  for(const item of rows){
    const card=make("article","card");
    const head=make("div","card-head");
    const left=make("div");
    left.append(make("span","id",item.id),make("div","kind",item.kind));
    head.append(left,make("span","badge badge-"+item.readiness,item.readiness));
    card.append(head,make("h3","",item.title),make("code","formula",item.expression));

    const details=make("details");
    details.append(make("summary","","Abrir cadeia de formalização"));
    const grid=make("div","grid");
    grid.append(
      field("Source",item.source),
      field("Code",item.code),
      field("Test",item.test),
      field("Evidence",item.evidence),
      field("Prior art",item.prior_art),
      field("Gaps",item.gaps)
    );
    details.append(grid);
    card.append(details);
    host.append(card);
  }
  document.querySelector("#result-count").textContent=rows.length+" item(ns) visível(is)";
}
async function boot(){
  const response=await fetch("page_data.json",{cache:"no-store"});
  if(!response.ok) throw new Error("PAGE_DATA indisponível: "+response.status);
  const data=await response.json();
  if(data.schema!=="rll.crf_page_data.v1" || data.claim_allowed!==false) throw new Error("Contrato PAGE_DATA inválido.");
  state.data=data;
  document.querySelector("#count-total").textContent=data.counts.total;
  document.querySelector("#count-a").textContent=data.counts.A;
  document.querySelector("#count-b").textContent=data.counts.B;
  document.querySelector("#count-c").textContent=data.counts.C;
  document.querySelectorAll(".filter").forEach(btn=>btn.addEventListener("click",()=>{
    document.querySelectorAll(".filter").forEach(x=>x.classList.remove("active"));
    btn.classList.add("active");
    state.filter=btn.dataset.filter;
    render();
  }));
  document.querySelector("#search").addEventListener("input",e=>{state.query=e.target.value;render();});
  render();
}
boot().catch(err=>{
  const host=document.querySelector("#items");
  host.replaceChildren(make("p","empty","Falha fail-closed ao carregar o artifact: "+err.message));
});
