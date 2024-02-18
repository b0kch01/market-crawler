'use client'
import { DataTableDemo } from '@/components/views/datatable-demo'
import { SheetDemo } from '@/components/views/sheet-demo'
import Navbar from '@/components/navbar'
import SearchBar from '@/components/searchbar'

export default function DemoPage() {
  return (
    <div className='flex flex-col p-25px pb-40'>
      <Navbar />
      <div className='px-[10vw]'>
        <SearchBar />
        <DataTableDemo />
        <SheetDemo />
      </div>
    </div>
  )
}