import Link from "next/link";
import Image from "next/image";

const mainFeatures=[
  {title:"Event Booking",text:"Discover music, art and local experiences in Kochi.",href:"/events",cta:"Browse events",emoji:"▣",image:"/images/feature-event.webp",theme:"event"},
  {title:"Salon Booking",text:"Choose a salon, a service and your preferred time.",href:"/salons",cta:"Find salons",emoji:"✂",image:"/images/feature-salon.webp",theme:"salon"},
  {title:"Local Store Booking",text:"Arrange store visits, consultations and pickup slots.",href:"/stores",cta:"Explore stores",emoji:"▤",image:"/images/feature-store.webp",theme:"store"},
  {title:"Restaurants & Hotels",text:"Explore places to dine or stay and try demo table requests.",href:"/restaurants-hotels",cta:"Explore stays & dining",emoji:"♨",image:"/images/restaurant.webp",theme:"dining"},
];
const places=[
  {name:"Fort Kochi",kind:"Historic streets",img:"/images/place-fort-kochi.webp"},
  {name:"Chinese Fishing Nets",kind:"Waterfront landmark",img:"/images/place-nets.webp"},
  {name:"Mattancherry Palace",kind:"Heritage site",img:"/images/place-palace.webp"},
];
const highlights=[
  {name:"Kochi Music Evening",sub:"Sample event · Dec 12",img:"/images/highlight-music.webp"},
  {name:"Kochi Art Walk",sub:"Sample event · Dec 19",img:"/images/highlight-art.webp"},
  {name:"Harbour Gallery Day",sub:"Sample event · Dec 26",img:"/images/highlight-boat.webp"},
];
export default function Dashboard(){return <div className="dashboard">
 <section className="hero" aria-label="Welcome to City Main"><div className="hero-copy"><span className="eyebrow dark-blue">WELCOME TO CITY MAIN <span className="pill-light">📍 Kochi first</span></span><h1>Your Kochi.<br/><span>All in one place.</span></h1><p>Discover events, book services, explore neighbourhoods, restaurants and hotels — all in one city dashboard.</p><Link href="/places" className="primary-btn">Explore Kochi <span aria-hidden>→</span></Link></div><div className="hero-art" role="img" aria-label="Illustration of Kochi waterfront and Chinese fishing nets"/></section>
 <div className="section-heading"><div><span className="eyebrow">START HERE</span><h2>What would you like to book?</h2></div><span className="section-helper">Four main experiences in the city</span></div>
 <section className="feature-grid" aria-label="Core booking categories">{mainFeatures.map(f=><article key={f.title} className={`feature-card ${f.theme}`}><div className="feature-copy"><span className="feature-icon" aria-hidden>{f.emoji}</span><h3>{f.title}</h3><p>{f.text}</p><Link href={f.href} className="feature-button">{f.cta}<span aria-hidden>→</span></Link></div><Image className="feature-illustration" src={f.image} alt="" width={245} height={215}/></article>)}</section>
 <div className="quick-actions"><span>Quick access</span><div className="quick-links"><Link href="/bookings">▦ My Bookings</Link><Link href="/events">🎟 Events</Link><Link href="/salons">✂ Salons</Link><Link href="/stores">▤ Local Stores</Link><Link href="/restaurants-hotels">♨ Restaurants & Hotels</Link><Link href="/places">◎ Explore Kochi</Link></div></div>
 <section className="dashboard-bottom">
  <div className="panel places-panel"><div className="panel-head"><h2>📍 Places to visit in Kochi</h2><Link href="/places">View all →</Link></div><div className="place-list">{places.map(p=><Link href="/places" className="place-tile" key={p.name}><div className="place-thumb"><Image src={p.img} alt="" fill sizes="200px" style={{objectFit:"cover"}}/></div><strong>{p.name}</strong><span>{p.kind}</span></Link>)}</div></div>
  <div className="panel dining-panel"><div className="panel-head"><h2>🍽️ Restaurants & Hotels</h2><Link href="/restaurants-hotels">View all →</Link></div><div className="dining-cards"><Link href="/restaurants-hotels" className="dining-tile"><Image src="/images/restaurant.webp" alt="" fill sizes="220px" style={{objectFit:"cover"}}/><div><strong>Restaurants</strong><span>Find dining options</span></div></Link><Link href="/restaurants-hotels" className="dining-tile"><Image src="/images/hotel.webp" alt="" fill sizes="220px" style={{objectFit:"cover"}}/><div><strong>Hotels</strong><span>Explore places to stay</span></div></Link></div></div>
  <div className="side-panels"><div className="panel mini-panel"><div className="panel-head"><h2>🌤️ Kochi Weather</h2></div><p className="stat-placeholder">Weather data not connected</p><Link href="/weather" className="tiny-link">Weather & notices →</Link></div><div className="panel mini-panel"><div className="panel-head"><h2>🚌 Transport in Kochi</h2><Link href="/transport">See more →</Link></div><div className="transport-icons"><span>🚌<small>Bus</small></span><span>🚇<small>Metro</small></span><span>⛴️<small>Ferry</small></span><span>🚕<small>Taxi</small></span></div></div></div>
  <div className="panel highlights-panel"><div className="panel-head"><h2>📅 Upcoming highlights</h2><Link href="/events">Browse events →</Link></div><div className="highlight-row">{highlights.map(h=><Link href="/events" key={h.name} className="highlight"><div className="highlight-image"><Image src={h.img} fill alt="" sizes="90px" style={{objectFit:"cover"}}/></div><div><strong>{h.name}</strong><span>{h.sub}</span></div></Link>)}</div></div>
  <div className="panel promise-panel"><h2>Explore more of Kochi</h2><p>City Main brings discovery and booking into one place. We&apos;re building the full product one working feature at a time.</p><div className="promise-tags"><span>✓ Events</span><span>✓ Salons</span><span>✓ Local stores</span><span>✓ Restaurants & Hotels</span></div><p className="small muted">All current reservations are demo-only and are not accepted by real businesses.</p></div>
 </section>
 </div>}
