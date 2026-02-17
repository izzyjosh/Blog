"use client";

import Link from "next/link";
import { useState } from "react";
import MenuIcon from "@/components/icons/menuIcon";

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="relative">
      {/* Desktop Menu */}
      <ul className="hidden md:flex items-center gap-4 justify-evenly text-white">
        <li>
          <Link href="/">Features</Link>
        </li>
        <li>
          <Link href="/">Trending</Link>
        </li>
        <li>
          <Link href="/">About</Link>
        </li>
        <li>
          <Link href="/contact">Contact</Link>
        </li>
      </ul>

      {/* Mobile Menu Button */}
      <button
        className="md:hidden p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white text-white"
        onClick={() => setIsOpen((prev) => !prev)}
        aria-label="Toggle menu"
      >
        <MenuIcon />
      </button>

      {/* Mobile Dropdown */}
      {isOpen && (
        <div className="absolute right-0 mt-3 w-40 rounded shadow-md bg-white text-black z-50 md:hidden">
          <ul className="flex flex-col">
            <li className="p-3 hover:bg-gray-100">
              <Link href="/" onClick={() => setIsOpen(false)}>
                Features
              </Link>
            </li>
            <li className="p-3 hover:bg-gray-100">
              <Link href="/" onClick={() => setIsOpen(false)}>
                Trending
              </Link>
            </li>
            <li className="p-3 hover:bg-gray-100">
              <Link href="/" onClick={() => setIsOpen(false)}>
                About
              </Link>
            </li>
            <li className="p-3 hover:bg-gray-100">
              <Link href="/contact" onClick={() => setIsOpen(false)}>
                Contact
              </Link>
            </li>
          </ul>
        </div>
      )}
    </nav>
  );
}
