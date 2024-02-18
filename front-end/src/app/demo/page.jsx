'use client'
import { DataTableDemo } from '@/components/views/datatable-demo'
import { SheetDemo } from '@/components/views/sheet-demo'
import Navbar from '@/components/navbar'
import SearchBar from '@/components/searchbar'

export default function DemoPage() {
  return (
    <div className='bg-[#F4F4F4] flex flex-col p-25px h-[100vh]'>
      <Navbar />
      <div className='px-[10vw]'> 
        <SearchBar />
        <DataTableDemo />
        <SheetDemo />
      </div>
    </div>
  )
}