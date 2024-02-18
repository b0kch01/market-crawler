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
    squareFootage: v.optional(v.number()),
    foodStalls: v.optional(v.number()),
    typesOfFoodStalls: v.optional(v.array(v.string())),
    demographics: v.optional(v.string()),
    localAreaComposition: v.optional(v.string()),
    accessibility: v.optional(v.object({
      wheelchairAccess: v.optional(v.boolean()),
      publicTransportAccess: v.optional(v.boolean()),
      parking: v.optional(v.boolean())
    })),
    footTraffic: v.optional(v.number()),
    annualVisitorCount: v.optional(v.number()),
    leaseRates: v.optional(v.object({
      averagePerSquareFoot: v.optional(v.number()),
      rangePerSquareFoot: v.optional(v.string()),
    })),
    occupancyRates: v.optional(v.number()),
    yearEstablished: v.optional(v.number()),
    renovationHistory: v.optional(v.array(v.object({
      year: v.optional(v.number()),
      details: v.optional(v.string())
    }))),
    owner: v.optional(v.array(v.object({
      name: v.optional(v.string()),
      contact: v.optional(v.string())
    }))),
    company: v.optional(v.object({
      name: v.optional(v.string()),
      contact: v.optional(v.string())
    })),
    images: v.optional(v.array(v.object({
      url: v.optional(v.string()),
      description: v.optional(v.string())
    }))),
    relevantURLs: v.optional(v.array(v.object({
      url: v.optional(v.string()),
      description: v.optional(v.string())
    })))
  },
  handler: async (ctx, args) => {
    const { id } = args
    await ctx.db.patch(id, args)
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
