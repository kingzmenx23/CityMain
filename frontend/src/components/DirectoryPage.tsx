"use client";
import {useState} from "react";
import Image from "next/image";
import Link from "next/link";
import BookingDialog from "@/components/BookingDialog";
import {directoryMeta,items,type Category,type DirectoryItem} from "@/lib/content";

export default function DirectoryPage({category}:{category:Category}){
 const meta=directoryMeta[category]; const [selected,setSelected]=useState<DirectoryItem|null>(null);const [query,setQuery]=useState("");
 const filtered=items.filter(x=>x.category===category&&`${x.title} ${x.subtitle} ${x.area}`.toLowerCase().includes(query.toLowerCase()));
 return <><div className="inner-header"><Link href="/" className="back-link">← Dashboard</Link><div className="eyebrow">DISCOVER KOCHI</div><h1><span className="heading-emoji">{meta.emoji}</span> {meta.title}</h1><p>{meta.intro}</p></div>
 <div className="directory-toolbar"><label className="directory-search">⌕ <input aria-label={`Filter ${meta.title}`} placeholder="Filter by name or area..." value={query} onChange={e=>setQuery(e.target.value)}/></label><span className="muted small">{filtered.length} sample results</span></div>
 <div className="directory-grid">{filtered.map(x=><article key={x.id} className="listing-card"><div className="listing-image"><Image src={x.image} alt="" fill sizes="(max-width:700px) 100vw, 33vw" style={{objectFit:"cover"}}/></div><div className="listing-content"><span className="content-tag">{x.tag}</span><h2>{x.title}</h2><p className="small muted">📍 {x.area} · {x.subtitle}</p><p>{x.description}</p><div className="listing-actions">{x.bookable?<button className="primary-btn" onClick={()=>setSelected(x)}>{meta.action} →</button>:<button onClick={()=>setSelected(x)} className="secondary-btn">View details →</button>}</div></div></article>)}</div>
 {filtered.length===0&&<div className="empty-state">No sample listings match your search. Try another keyword.</div>}
 {selected&&(selected.bookable?<BookingDialog key={selected.id} item={selected} onClose={()=>setSelected(null)}/>:<div className="modal-backdrop" onMouseDown={e=>{if(e.target===e.currentTarget)setSelected(null);}}><div className="modal-panel" role="dialog" aria-modal="true"><button onClick={()=>setSelected(null)} aria-label="Close" className="modal-close">×</button><span className="eyebrow">INFORMATIONAL LISTING</span><h2>{selected.title}</h2><p>{selected.description}</p><p className="muted">{selected.detail}</p><button className="secondary-btn" onClick={()=>setSelected(null)}>Close</button></div></div>)}
 </>;
}
