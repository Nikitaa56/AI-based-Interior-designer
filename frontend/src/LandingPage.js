import React from "react";
import { motion } from "framer-motion";
import { ArrowRight } from "lucide-react";
import "./index.css";

export default function LandingPage({ onStart }) {
  return (
    <div className="landing-bg flex flex-col items-center justify-center min-h-screen text-white px-6">
      <motion.h1
        className="landing-title"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
      >
        Serene Spaces
      </motion.h1>

      <p className="landing-subtitle">
        Calm. Crafted. AI-designed interiors for peaceful living.
      </p>

      <motion.button
        className="luxury-btn mt-8 flex items-center gap-2"
        onClick={onStart}
        whileTap={{ scale: 0.97 }}
      >
        Start Designing <ArrowRight size={18} />
      </motion.button>
    </div>
  );
}
