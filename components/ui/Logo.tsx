import Link from "next/link";

export default function Logo() {
  return (
    <Link href="/" aria-label="Home">
      <div className="text-2xl md:text-3xl font-bold text-gray-800">Izzy</div>
    </Link>
  );
}
