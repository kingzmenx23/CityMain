export type Category = "events" | "salons" | "stores" | "restaurants-hotels" | "places";

export type DirectoryItem = {
  id: string;
  category: Category;
  title: string;
  subtitle: string;
  area: string;
  image: string;
  tag: string;
  description: string;
  detail: string;
  bookable?: boolean;
  demoDate?: string;
  times?: string[];
};

// All events, businesses and booking slots are illustrative demo data.
// Attractions are real place names but the app does not currently verify hours or restrictions.
export const items: DirectoryItem[] = [
  { id:"music-evening", category:"events",title:"Kochi Music Evening",subtitle:"Live music · Sample event",area:"Fort Kochi",image:"/images/highlight-music.webp",tag:"Free demo ticket",description:"Explore a sample music-event booking experience.",detail:"Example event for testing booking UI. This is not a real event or available reservation.",bookable:true,demoDate:"2026-12-12",times:["18:00"] },
  { id:"art-walk",category:"events",title:"Kochi Art Walk",subtitle:"Arts · Sample event",area:"Mattancherry",image:"/images/highlight-art.webp",tag:"Free demo ticket",description:"Browse a guided art-walk example.",detail:"Illustrative event information. Not an advertised real event.",bookable:true,demoDate:"2026-12-19",times:["10:00","16:00"] },
  { id:"harbour-gallery",category:"events",title:"Harbour Gallery Day",subtitle:"Exhibition · Sample event",area:"Ernakulam",image:"/images/highlight-boat.webp",tag:"Free demo ticket",description:"Try the event flow using this example listing.",detail:"For user-interface testing only; the date and venue are fictitious.",bookable:true,demoDate:"2026-12-26",times:["11:00","15:00"] },
  { id:"salon-studio",category:"salons",title:"Harbour Hair Studio (Demo)",subtitle:"Haircut and grooming",area:"Panampilly Nagar",image:"/images/feature-salon.webp",tag:"Demo appointment",description:"Choose a grooming service and reserve a sample time slot.",detail:"This example business is not connected to a real provider.",bookable:true,times:["10:00","11:30","14:00","16:00"] },
  { id:"salon-beauty",category:"salons",title:"Kochi Beauty Lounge (Demo)",subtitle:"Beauty and wellness",area:"Kakkanad",image:"/images/feature-salon.webp",tag:"Demo appointment",description:"Experience the appointment workflow.",detail:"Illustrative provider, services and availability only.",bookable:true,times:["09:30","12:00","15:30"] },
  { id:"local-pickup",category:"stores",title:"Local Craft Corner (Demo)",subtitle:"Pickup reservation and store visits",area:"Fort Kochi",image:"/images/feature-store.webp",tag:"Demo store booking",description:"Reserve a visit or pickup timeslot.",detail:"Store booking prototype; no products or inventory are reserved in real life.",bookable:true,times:["10:00","12:30","15:00"] },
  { id:"local-showroom",category:"stores",title:"Neighbourhood Showroom (Demo)",subtitle:"Personal shopping appointment",area:"Edappally",image:"/images/feature-store.webp",tag:"Demo store booking",description:"Book a store consultation slot.",detail:"Example booking only. No live business integration.",bookable:true,times:["11:00","13:00","17:00"] },
  { id:"restaurant-bistro",category:"restaurants-hotels",title:"Waterfront Bistro (Demo)",subtitle:"Restaurant · Dining",area:"Marine Drive",image:"/images/restaurant.webp",tag:"Demo table request",description:"Explore restaurant details and a sample table request.",detail:"Sample restaurant listing; requests are saved only in this browser.",bookable:true,times:["12:30","13:30","19:00","20:30"] },
  { id:"hotel-harbour",category:"restaurants-hotels",title:"Harbour Stay (Demo)",subtitle:"Hotel · Accommodation",area:"Fort Kochi",image:"/images/hotel.webp",tag:"Discovery only",description:"Explore a hotel listing; room availability is not yet supported.",detail:"Hotel bookings require verified room inventory and will be connected in a later phase.",bookable:false },
  { id:"fort-kochi",category:"places",title:"Fort Kochi",subtitle:"Heritage neighbourhood",area:"Fort Kochi",image:"/images/place-fort-kochi.webp",tag:"Place to visit",description:"Explore colonial-era streets and the waterfront.",detail:"Check official sources for access restrictions, changes and opening times.",bookable:false },
  { id:"chinese-nets",category:"places",title:"Chinese Fishing Nets",subtitle:"Waterfront landmark",area:"Fort Kochi",image:"/images/place-nets.webp",tag:"Place to visit",description:"See one of Kochi's best-known waterfront landmarks.",detail:"Access conditions can change; no live advisory data is connected.",bookable:false },
  { id:"mattancherry-palace",category:"places",title:"Mattancherry Palace",subtitle:"Heritage attraction",area:"Mattancherry",image:"/images/place-palace.webp",tag:"Place to visit",description:"Discover an important heritage site.",detail:"Verify opening information and any restrictions before traveling.",bookable:false },
];

export const directoryMeta: Record<Category,{title:string;intro:string;emoji:string;action:string}> = {
  events:{title:"Events in Kochi",intro:"Discover experiences and test a free-ticket reservation flow.",emoji:"🎟️",action:"Try booking"},
  salons:{title:"Salon Booking",intro:"Explore sample salons, services and appointment times.",emoji:"✂️",action:"Choose time"},
  stores:{title:"Local Store Booking",intro:"Try a store visit, consultation or pickup-time reservation.",emoji:"🏬",action:"Reserve visit"},
  "restaurants-hotels":{title:"Restaurants & Hotels",intro:"Explore dining and stays in Kochi. Restaurant requests are a browser-only demo; hotel bookings are not live.",emoji:"🍽️",action:"View details"},
  places:{title:"Places to Visit",intro:"Discover Kochi attractions and check advisories before visiting.",emoji:"📍",action:"Learn more"}
};
