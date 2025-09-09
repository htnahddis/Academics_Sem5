"use client";

import Image from "next/image";
import { motion } from "framer-motion";
import { ArrowRight } from "lucide-react";

export default function Banner() {
  return (
    <section className="relative w-full min-h-screen bg-blue-700 text-white overflow-hidden flex items-center justify-center px-8 py-16">
      {/* Content Wrapper */}
      <div className="relative grid grid-cols-1 md:grid-cols-2 gap-12 items-center max-w-7xl w-full">
        
        {/* Left Side Text */}
        <div className="space-y-6">
          <motion.h1
            initial={{ y: 40, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ duration: 0.6 }}
            className="text-6xl md:text-8xl font-extrabold uppercase leading-none relative"
          >
            {/* Outline effect background text */}
            <span className="absolute -top-6 left-0 text-transparent stroke-white opacity-20 select-none">
              Creative
            </span>
            Creative <br />
            Agency
          </motion.h1>

          {/* Stats */}
          <div className="space-y-4 mt-10">
            <p className="text-xl font-semibold">500+ Happy Clients</p>
            <p className="text-xl font-semibold">125+ Projects Done</p>
            <p className="text-xl font-semibold">450+ Media Features</p>
          </div>

          {/* CTA */}
          <div className="mt-6">
            <button className="flex items-center gap-2 bg-white text-blue-700 px-6 py-3 rounded-2xl font-semibold hover:bg-gray-200 transition">
              Get Started <ArrowRight size={20} />
            </button>
          </div>
        </div>

        {/* Right Side Image */}
        <div className="flex justify-center relative">
          <Image
            src="/banner-person.png" // replace with your image in public/
            alt="Creative Agency"
            width={500}
            height={500}
            className="rounded-2xl object-cover"
            priority
          />
        </div>
      </div>

      {/* Bottom Scrolling Strip */}
      <motion.div
        initial={{ x: "100%" }}
        animate={{ x: "-100%" }}
        transition={{ repeat: Infinity, duration: 15, ease: "linear" }}
        className="absolute bottom-6 left-0 w-full bg-yellow-400 text-black py-3 text-lg font-bold whitespace-nowrap"
      >
        BRANDING &nbsp; | &nbsp; GRAPHIC DESIGN &nbsp; | &nbsp; WEB DESIGN &nbsp; | &nbsp; DIGITAL MARKETING &nbsp; | &nbsp;
      </motion.div>
    </section>
  );
}
