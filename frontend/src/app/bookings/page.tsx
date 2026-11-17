"use client";
import Link from "next/link";
import {useEffect,useState} from "react";
import {cancelDemoBooking,getDemoBookings,type DemoBooking} from "@/lib/demo-bookings";
export default function BookingsPage(){
 const [bookings,setBookings]=useState<DemoBooking[]>([]);const [loaded,setLoaded]=useState(false);
 useEffect(()=>{setBookings(getDemoBookings());setLoaded(true);},[]);
 function cancel(id:string){cancelDemoBooking(id);setBookings(getDemoBookings());}
 return <><div className="inner-header"><Link href="/" className="back-link">← Dashboard</Link><div className="eyebrow">YOUR CITY MAIN</div><h1>My Bookings</h1><p>Review the sample bookings saved on this device.</p></div><div className="notice-note">These bookings exist only in your browser. They are <strong>not real reservations</strong> and will not notify any organizer, salon, restaurant or store.</div>
 {!loaded?<div className="empty-state">Loading local demo bookings…</div>:bookings.length===0?<div className="empty-state"><div className="large-emoji">▦</div><h2>No demo bookings yet</h2><p>Try the event or appointment booking flow to see how reservations will be displayed.</p><Link href="/events" className="primary-btn">Browse sample events →</Link></div>:<div className="booking-list">{bookings.map(b=><article key={b.id} className="booking-record"><div><span className={`status-chip ${b.status==='cancelled'?'cancelled':''}`}>{b.status==='cancelled'?'Cancelled':'Demo only'}</span><h2>{b.itemTitle}</h2><p className="muted">{b.date} at {b.time} · {b.quantity} {b.quantity===1?'person':'people'}</p><p className="small muted">{b.service}</p><code>{b.id}</code></div>{b.status==='demo'&&<button className="secondary-btn" onClick={()=>cancel(b.id)}>Cancel demo</button>}</article>)}</div>}
 </>;
}
