"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import logo from "../../public/images/claimshawk_logo_with_transparent_background_more_robotic.jpeg";
import { cn } from "@/lib/utils";
const navLinks = [
  {
    href: "/",
    label: "Home",
  },
  {
    href: "/admin",
    label: "Admin",
  },
];

export default function Header() {
  const pathname = usePathname();

  return (
    <header className="flex justify-center items-center py-4 px-7 border-b">
      <NavigationMenu>
        <NavigationMenuList className="px-4">
          {navLinks.map((link) => (
            <NavigationMenuItem key={link.href}>
              <Link
                href={link.href}
                legacyBehavior
                passHref
              >
                <NavigationMenuLink
                  className={cn(
                    navigationMenuTriggerStyle(),
                    "text-lg font-medium",
                    pathname === link.href && "text-primary"
                  )}
                  active={pathname === link.href}
                >
                  {link.label}
                </NavigationMenuLink>
              </Link>
            </NavigationMenuItem>
          ))}
        </NavigationMenuList>
      </NavigationMenu>
    </header>
  );
}
// /*
// <Link href="/" className="flex items-center gap-2">
// <Avatar>
//   <AvatarImage src={logo.src} alt="Logo" />
//   <AvatarFallback>CH</AvatarFallback>
// </Avatar>
// {/* <span className="font-semibold text-lg">ClaimsHawk</span> */}
// // </Link>
