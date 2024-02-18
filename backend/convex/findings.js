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
    fields: v.object({
      name: v.optional(v.string()),
      location: v.optional(v.string()),
      city: v.optional(v.string()),
      state: v.optional(v.string()),
      year_established: v.optional(v.number()),
      population_density: v.optional(v.union(v.string(), v.number())),
      median_income: v.optional(v.string()),
      age_distribution: v.optional(v.any()),
      annual_visitor_count: v.optional(v.number()),
      composition: v.optional(v.array(v.string())),
      foot_traffic: v.optional(v.string()),
      square_footage: v.optional(v.union(v.number(), v.string(), v.null())),
      public_transport: v.optional(v.array(v.string())),
      lease_rates: v.optional(v.string()),
      food: v.optional(v.union(v.number(), v.null())),
      bars: v.optional(v.union(v.number(), v.null())),
      retail: v.optional(v.union(v.number(), v.null())),
      management_company: v.optional(v.string()),
      parking_spots: v.optional(v.number()),
      parking_fees: v.optional(v.union(v.string(), v.null())),
      peak_time_availability: v.optional(v.string()),
      contact: v.optional(v.string()),
      owner: v.optional(v.string()),
      images: v.optional(v.array(v.object({
        url: v.string(),
        alt: v.optional(v.string()),
      }))),
      sources: v.optional(v.array(v.object({
        source: v.string(),
        label: v.optional(v.string()),
      }))),
      occupancy_rate: v.optional(v.string()),
      types_of_food_stalls: v.optional(v.array(v.string())),
    })
  },
  handler: async (ctx, args) => {
    const { id, fields } = args
    await ctx.db.patch(id, fields)
  }
})

export const createFoodHall = mutation({
  args: {
    name: v.string(),
    location: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const { name, location } = args
    const newID = await ctx.db.insert("food_halls", {
      name: name,
      location: location
    })
    return newID
  }
})
