import React, { useState } from "react";
import { motion } from "framer-motion";

export default function BeforeAfterSlider({ beforeImage, afterImage }) {
  const [position, setPosition] = useState(50);

  return (
    <div className="relative w-full h-[420px] rounded-2xl overflow-hidden shadow-2xl border border-white/10 backdrop-blur-xl">

      {/* BEFORE IMAGE */}
      <img
        src={beforeImage}
        alt="Before"
        className="absolute inset-0 w-full h-full object-cover"
      />

      {/* AFTER IMAGE (masked) */}
      <div
        className="absolute inset-0 overflow-hidden"
        style={{ width: `${position}%` }}
      >
        <img
          src={afterImage}
          alt="After"
          className="absolute inset-0 w-full h-full object-cover"
        />
      </div>

      {/* SLIDER LINE */}
      <div
        className="absolute top-0 bottom-0 w-1 bg-gold/80 cursor-col-resize shadow-lg"
        style={{ left: `${position}%` }}
        onMouseDown={() => {
          const move = (e) => {
            let pct = (e.clientX / window.innerWidth) * 100;
            if (pct > 0 && pct < 100) setPosition(pct);
          };
          const up = () => {
            window.removeEventListener("mousemove", move);
            window.removeEventListener("mouseup", up);
          };
          window.addEventListener("mousemove", move);
          window.addEventListener("mouseup", up);
        }}
      ></div>

      {/* LABELS */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="absolute top-4 left-4 bg-black/40 px-4 py-1 rounded-full text-white text-sm backdrop-blur-xl"
      >
        Before
      </motion.div>

      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="absolute top-4 right-4 bg-gold px-4 py-1 rounded-full text-black text-sm font-semibold"
      >
        After ✨
      </motion.div>
    </div>
  );
}
