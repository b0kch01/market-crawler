'use client'

import React, { createContext, useState, useEffect } from 'react'

const DataContext = createContext()

export const DataContextProvider = ({ children }) => {
  return <DataContext.Provider value={data}>{children}</DataContext.Provider>
}

export const useDataContext = () => {
  const context = React.useContext(DataContext)
  if (!context) {
    throw new Error('useDataContext must be used within a DataContextProvider')
  }
  return context
}