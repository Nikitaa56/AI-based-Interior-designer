import React from "react";
import { motion } from "framer-motion";
import { Sparkles } from "lucide-react";

const STYLES = [
  {
    id: "modern",
    name: "Modern Luxury",
    prompt: "a modern luxury interior with matte textures, soft golden light, marble surfaces, and clean geometry",
    image: "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80"
  },
  {
    id: "minimal",
    name: "Minimal Elegance",
    prompt: "minimalist soft interior with gentle warm tones, airy atmosphere and natural decor",
    image: "https://images.unsplash.com/photo-1540574163026-643ea20ade25?q=80"
  },
  {
    id: "boho",
    name: "Boho Chic",
    prompt: "bohemian interior with plants, woven textures, warm earthy lighting and handcrafted details",
    image: "https://images.unsplash.com/photo-1615874959474-d609969a20ed?q=80"
  },
  {
    id: "vintage",
    name: "Vintage Royal",
    prompt: "royal vintage interior with deep warm colors, ornate textures, velvet furniture and golden details",
    image: "https://images.unsplash.com/photo-1615529182904-14819cba4420?q=80"
  }
];

export default function StylePicker({ selectedStyle, onStyleSelect }) {
  return (
    <div className="w-full space-y-4">
      <h2 className="text-3xl font-bold mb-3 brand-gradient">Choose a Style</h2>

      <div className="grid grid-cols-2 gap-5">
        {STYLES.map((style) => (
          <motion.div
            key={style.id}
            whileHover={{ scale: 1.03 }}
            onClick={() => onStyleSelect(style)}
            className={`relative rounded-2xl overflow-hidden cursor-pointer border
              ${selectedStyle?.id === style.id ? "border-gold/80 shadow-lg shadow-gold/30" : "border-white/10"}
            `}
          >
            {/* Image */}
            <img
              src={style.image}
              alt={style.name}
              className="w-full h-40 object-cover opacity-90"
            />

            {/* Overlay */}
            <div className="absolute inset-0 bg-black/40 flex items-end p-3">
              <p className="text-white font-semibold text-lg">{style.name}</p>
            </div>

            {/* Selected icon */}
            {selectedStyle?.id === style.id && (
              <div className="absolute top-3 right-3 bg-gold p-1 rounded-full">
                <Sparkles size={20} className="text-black" />
              </div>
            )}
          </motion.div>
        ))}
      </div>
    </div>
  );
}
