import { mutation } from './_generated/server'
import { v } from "convex/values"

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