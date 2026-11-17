"use client";
import { useEffect,useState } from "react";
import type { DirectoryItem } from "@/lib/content";
import {saveDemoBooking} from "@/lib/demo-bookings";

export default function BookingDialog({item,onClose}:{item:DirectoryItem,onClose:()=>void}) {
 const [date,setDate]=useState(item.demoDate||"");
 const [time,setTime]=useState(item.times?.[0]||"10:00");
 const [quantity,setQuantity]=useState(1);
 const [service,setService]=useState(item.category==="salons"?"Haircut / service consultation":item.category==="stores"?"Store visit / consultation":item.category==="restaurants-hotels"?"Table request":"Free event seat");
 const [reference,setReference]=useState("");
 const [error,setError]=useState("");
 useEffect(()=>{function key(e:KeyboardEvent){if(e.key==="Escape")onClose();} window.addEventListener("keydown",key);return()=>window.removeEventListener("keydown",key);},[onClose]);
 function submit(e:React.FormEvent<HTMLFormElement>){ e.preventDefault();setError("");
  if(!date||!time){setError("Choose a date and time to continue.");return;}
  if(item.demoDate&&date!==item.demoDate){setError("Use the sample event date shown for this demo.");return;}
  const b=saveDemoBooking({itemId:item.id,itemTitle:item.title,category:item.category,date,time,quantity,service});setReference(b.id);
 }
 return <div className="modal-backdrop" onMouseDown={e=>{if(e.target===e.currentTarget)onClose();}}><section role="dialog" aria-modal="true" aria-labelledby="booking-title" className="modal-panel">
  <button className="modal-close" aria-label="Close" onClick={onClose}>×</button>
  {reference ? <div className="confirmation"><div className="confirm-icon">✓</div><h2 id="booking-title">Demo booking saved</h2><p>Your sample booking appears in My Bookings on this browser.</p><div className="reference">{reference}</div><p className="muted small">No real ticket, appointment, table or availability was reserved.</p><a href="/bookings" className="primary-btn">View My Bookings →</a></div> : <>
   <span className="eyebrow">BROWSER-ONLY BOOKING DEMO</span><h2 id="booking-title">{item.title}</h2><p className="muted">{item.detail}</p>
   <form onSubmit={submit} className="booking-fields">
    {item.category!=="events"&&<label>Service or request<select value={service} onChange={e=>setService(e.target.value)}>
     {(item.category==="salons"?["Haircut / service consultation","Styling consultation","Beauty service consultation"]:item.category==="stores"?["Store visit / consultation","Pickup appointment","Personal shopping"]:["Table request","Dining inquiry"]).map(v=><option key={v}>{v}</option>)}
    </select></label>}
    <div className="form-grid"><label>Date<input required type="date" min={item.demoDate||new Date(Date.now()-new Date().getTimezoneOffset()*60000).toISOString().slice(0,10)} max={item.demoDate||undefined} value={date} onChange={e=>setDate(e.target.value)}/></label><label>Time<select value={time} onChange={e=>setTime(e.target.value)}>{(item.times||["10:00"]).map(t=><option value={t} key={t}>{t}</option>)}</select></label></div>
    <label>{item.category==="events"?"Demo seats":item.category==="restaurants-hotels"?"Guests":"People"}<select value={quantity} onChange={e=>setQuantity(Number(e.target.value))}>{[1,2,3,4].map(n=><option key={n} value={n}>{n}</option>)}</select></label>
    {error&&<p role="alert" className="form-error">{error}</p>}
    <div className="privacy-note">This prototype does not verify availability, collect payments or contact a provider. Demo reservations are stored locally in your browser.</div>
    <button className="primary-btn full-width" type="submit">Save demo booking →</button>
   </form>
  </>}
 </section></div>;
}
