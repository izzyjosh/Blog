import Logo from "@/components/ui/Logo";
import Navbar from "./Navbar";
import Image from "next/image";

export default function Header() {
  return (
    <header className="relative w-full p-3 text-white">
      {/* Background Image */}
      <Image
        src="/header.jpg"
        alt="Header background"
        fill
        priority
        className="object-cover"
      />

      {/* Overlay (optional but recommended) */}
      <div className="absolute inset-0 bg-black/40" />

      {/* Content */}
      <div className="relative z-10 flex h-full items-center justify-between px-6 text-white">
        <Logo />
        <Navbar />
      </div>
    </header>
  );
}
