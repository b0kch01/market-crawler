import { DataTableDemo } from '@/components/views/datatable-demo'
import { SheetDemo } from '@/components/views/sheet-demo'

export default function DemoPage() {
  return (
    <main className="flex flex-col justify-center items-center min-h-screen w-full">
      <DataTableDemo />
      <SheetDemo />
    </main>
  )
}