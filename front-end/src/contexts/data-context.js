"use client"

import { createContext } from 'react'
import { ConvexReactClient, ConvexProvider } from 'convex/react'

const DataContext = createContext()

const convex = new ConvexReactClient(process.env.NEXT_PUBLIC_CONVEX_URL)

export const DataContextProvider = ({ children }) => {
  return <ConvexProvider client={convex}>{children}</ConvexProvider>
}

export const useDataContext = () => {
  const context = useContext(DataContext)
  if (!context) {
    throw new Error('useDataContext must be used within a DataContextProvider')
  }
  return context
}