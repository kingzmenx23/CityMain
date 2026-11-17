import type { Metadata } from "next";
import AppShell from "@/components/AppShell";
import "./globals.css";
export const metadata: Metadata = {title:"City Main | Explore Kochi",description:"Kochi-first city exploration and booking platform — frontend prototype."};
export default function RootLayout({children}:Readonly<{children:React.ReactNode}>){return <html lang="en"><body><AppShell>{children}</AppShell></body></html>}
