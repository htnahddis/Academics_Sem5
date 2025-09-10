"use client";

import Image from "next/image";
import { motion } from "framer-motion";
import { ArrowRight } from "lucide-react";
import { Anton } from "next/font/google";
const anton = Anton({
  subsets: ["latin"],
  weight: "400",
});

export default function Banner() {
  return (
    <section className="relative w-full min-h-screen  text-white overflow-hidden flex items-center justify-center px-6 md:px-12 border-red-600 border-4">
      {/* Giant Background Text */}

 <div className="absolute inset-0 z-20 flex mx-[10vw] my-[4vh]  items-end justify-start pointer-events-none">
  <div className="pointer-events-autorounded-xl px-6 py-6 text-white ">
    <div className="text-center py-2">
      <h2 className="text-3xl font-bold">Full-Stack Developer</h2>
    
    </div>

    <div className="w-16 mx-auto border-t my-3" />

    <div className="text-center py-2">
      <h2 className="text-3xl font-bold">Marketing Head</h2>
      <h4 className="text-lg mt-1">DJS SKYLARK</h4>
    </div>

    <div className="w-16 mx-auto border-t my-3" />

    <div className="text-center py-2">
      <h2 className="text-3xl font-bold">Secretary</h2>
      <h4 className="text-lg mt-1">DJS ACM SIGAI</h4>
    </div>
  </div>

</div>

<div>
      <h1
        className="${anton.className} absolute inset-0 flex my-[18vh]
        text-[18.5vw] md:text-[10.5vw] font-extrabold uppercase 
        text-[#C9FE05] leading-none select-none text-center z-0 "
      >
        Siddhanth Chapade
      </h1>
        <h1
        className="${anton.className} absolute inset-0  my-[19vh]
        text-[18.5vw] md:text-[10.5vw] font-extrabold uppercase text-transparent
        leading-none select-none text-center z-0 [-webkit-text-stroke:2px_#C9FE05] [text-stroke:1px_#C9FE05]"
      >
        Siddhanth Chapade
      </h1>
      


     <div className="flex justify-center relative items-center w-full border-red-500 border-4 z-10">
  <Image
    src="/profile_main.png"
    alt="Creative Agency"
    width={900}   // larger natural size
    height={900}
    className="rounded-2xl object-cover w-[600px] md:w-[500px] lg:w-[900px] h-auto"
    priority
  />
</div>
</div>

{/* 
      <motion.div
        initial={{ x: "100%" }}
        animate={{ x: "-100%" }}
        transition={{ repeat: Infinity, duration: 15, ease: "linear" }}
        className="absolute bottom-6 left-0 w-full bg-yellow-400 text-black py-3 text-sm md:text-lg font-bold whitespace-nowrap"
      >
        BRANDING &nbsp; | &nbsp; GRAPHIC DESIGN &nbsp; | &nbsp; WEB DESIGN &nbsp; | &nbsp; DIGITAL MARKETING &nbsp; | &nbsp;
      </motion.div> */}
    </section>
  );
}
