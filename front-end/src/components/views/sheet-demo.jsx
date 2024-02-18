import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
	Sheet,
	SheetClose,
	SheetContent,
	SheetDescription,
	SheetFooter,
	SheetHeader,
	SheetTitle,
	SheetTrigger,
} from "@/components/ui/sheet"
import NeighborhoodsInfo from "./neighborhoods-info"
import { ChevronsRight } from "lucide-react"

export function SheetDemo() {
	return (
		<Sheet>
			<SheetTrigger asChild>
				<Button variant="outline">Open</Button>
			</SheetTrigger>

			<SheetContent className="overflow-y-scroll h-full p-0">
				<SheetClose className="absolute top-0 z-30 p-4">
					<ChevronsRight className="bg-white shadow-md border rounded" />
				</SheetClose>
				<NeighborhoodsInfo />
			</SheetContent>
		</Sheet>
	)
}

