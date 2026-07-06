import {
  BookOpen,
  Boxes,
  FileText,
  FolderOpen,
  Home,
  Image,
  Settings,
} from "lucide-react";

export type NavigationItem = {
  title: string;
  href: string;
  icon: React.ElementType;
};

export const navigation: NavigationItem[] = [
  {
    title: "Dashboard",
    href: "/",
    icon: Home,
  },
  {
    title: "Products",
    href: "/products",
    icon: Boxes,
  },
  {
    title: "Knowledge",
    href: "/knowledge",
    icon: BookOpen,
  },
  {
    title: "Import",
    href: "/import",
    icon: FolderOpen,
  },
  {
    title: "Documents",
    href: "/documents",
    icon: FileText,
  },
  {
    title: "Media",
    href: "/media",
    icon: Image,
  },
  {
    title: "Settings",
    href: "/settings",
    icon: Settings,
  },
];
