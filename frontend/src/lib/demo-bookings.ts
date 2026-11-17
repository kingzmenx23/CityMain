export type DemoBooking = {
  id: string;
  itemId: string;
  itemTitle: string;
  category: string;
  date: string;
  time: string;
  quantity: number;
  service: string;
  status: "demo" | "cancelled";
  createdAt: string;
};
const KEY = "city-main-demo-bookings-v1";
export function getDemoBookings(): DemoBooking[] {
  if (typeof window === "undefined") return [];
  try { const data: unknown = JSON.parse(window.localStorage.getItem(KEY) || "[]"); return Array.isArray(data) ? data as DemoBooking[] : []; }
  catch { return []; }
}
export function saveDemoBooking(booking: Omit<DemoBooking,"id"|"status"|"createdAt">): DemoBooking {
  const result: DemoBooking = {
    ...booking, id:`DEMO-${Date.now().toString(36).toUpperCase()}-${Math.random().toString(36).slice(2,6).toUpperCase()}`,
    status:"demo", createdAt:new Date().toISOString(),
  };
  window.localStorage.setItem(KEY,JSON.stringify([result,...getDemoBookings()]));
  return result;
}
export function cancelDemoBooking(id:string):void {
  const data=getDemoBookings().map(b=>b.id===id?{...b,status:"cancelled" as const}:b);
  window.localStorage.setItem(KEY,JSON.stringify(data));
}
