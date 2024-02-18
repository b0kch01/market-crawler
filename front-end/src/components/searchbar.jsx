import React from 'react'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

const SearchBar = () => {
  return (
    <div className="flex w-full h-[50px] items-center gap-2 space-x-2 py-10">
        <div className="flex grow items-center h-[56px] px-5 bg-white rounded-2xl">
        <img src='glass.svg' alt='Search' className='w-6 h-6' />
        <input 
            className='outline-none text-base border-none h-[56px] w-full px-4 py-2 rounded-2xl' 
            type="email" 
            placeholder="Search Food Hall..."
        />
        </div>   
        <Button className='h-[56px] w-[139px] gap-2 bg-[#FF6B00] rounded-2xl 'type="submit"><img src='sparkle.svg'></img><span className='text-base'>Search</span></Button> 
    </div>
  )
}

export default SearchBar