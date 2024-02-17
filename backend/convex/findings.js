import { mutation, query } from './_generated/server'
import { v } from "convex/values"

export const getAll = query({
  handler: async (ctx) => {
    return await ctx.db.query("food_halls").collect()
  }
})

export const updateFoodHall = mutation({
  args: {
    id: v.id("food_halls"),
    name: v.optional(v.string()),
    location: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const { id, name, location } = args
    await ctx.db.patch(id, {
      name: name,
      location: location,
    })
  }
})

export const createFoodHall = mutation({
  args: {
    name: v.string(),
    location: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const { name, location } = args
    await ctx.db.insert("food_halls", {
      name: name,
      location: location
    })
  }
})
