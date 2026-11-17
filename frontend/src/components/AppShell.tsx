"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";

const links=[
 {href:"/",icon:"⌂",label:"Dashboard"},
 {href:"/bookings",icon:"▦",label:"My Bookings"},
 {href:"/places",icon:"◉",label:"Places to Visit"},
 {href:"/events",icon:"▣",label:"Events"},
 {href:"/salons",icon:"✂",label:"Salons"},
 {href:"/stores",icon:"▤",label:"Local Stores"},
 {href:"/restaurants-hotels",icon:"♧",label:"Restaurants & Hotels"},
 {href:"/transport",icon:"▥",label:"Transport"},
 {href:"/weather",icon:"☁",label:"Weather & Notices"},
];
export default function AppShell({children}:{children:React.ReactNode}) {
 const pathname=usePathname(); const [mobileOpen,setMobileOpen]=useState(false);
 return <div className="app-layout">
  <aside className={`sidebar ${mobileOpen?"sidebar-open":""}`}>
   <Link href="/" className="brand" onClick={()=>setMobileOpen(false)}><span className="brand-mark">▥</span><span>City Main</span></Link>
   <div className="sidebar-title">EXPLORE CITY MAIN</div>
   <nav aria-label="Main navigation" className="side-nav">{links.map(link=><Link key={link.href} href={link.href} onClick={()=>setMobileOpen(false)} className={`side-link ${pathname===link.href?"active":""}`}><span className="nav-icon" aria-hidden>{link.icon}</span><span>{link.label}</span></Link>)}</nav>
   <div className="sidebar-spacer"/>
   <div className="sidebar-scope"><span className="mini-pill">Version 1</span><strong>Built for Kochi</strong><p>Plan your city, explore local places and try sample booking journeys.</p></div>
   <div className="sidebar-footer">Frontend prototype · Demo data</div>
  </aside>
  {mobileOpen&&<button aria-label="Close navigation" className="mobile-overlay" onClick={()=>setMobileOpen(false)}/>}
  <div className="main-column">
   <header className="topbar">
    <button className="menu-toggle" aria-label="Open navigation" onClick={()=>setMobileOpen(v=>!v)}>☰</button>
    <form className="top-search" role="search" action="/search" method="get"><span aria-hidden>⌕</span><input name="q" aria-label="Search City Main" placeholder="Search events, salons, stores, restaurants, hotels and places..."/></form>
    <div className="location-pill">📍 <strong>Kochi</strong><small>V1</small></div>
    <Link href="/bookings" className="profile-bubble" aria-label="My demo bookings">◯</Link>
   </header>
   <div className="demo-banner"><span className="demo-dot"/> Development prototype — listings, availability and bookings are examples, not live services.</div>
   <div className="page-container">{children}</div>
   <footer className="app-footer">City Main · Kochi-first city guide · Frontend demo only</footer>
  </div>
 </div>;
}
