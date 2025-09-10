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
    <section className="relative w-full min-h-screen  text-white overflow-hidden flex items-center justify-center px-6 md:px-12">
    

 <div className="absolute inset-0 z-20 flex mx-[8vw] my-[2vh]  items-end justify-start pointer-events-none">
  <div className="pointer-events-autorounded-xl px-6 py-6 text-white ">
    <div className="text-start py-2">
      <h2 className="text-5xl font-bold">Full-Stack Developer</h2>
    
    </div>

    <div className="w-[25vw]  border-t my-3" />

    <div className="text-start py-2">
      <h2 className="text-5xl font-bold">Marketing Head</h2>
      <h4 className="text-2xl ">DJS SKYLARK</h4>
    </div>

    <div className="w-[25vw]  border-t my-3" />

    <div className="text-start py-2">
      <h2 className="text-5xl font-bold">Secretary</h2>
      <h4 className="text-2xl ">DJS ACM SIGAI</h4>
    </div>
  </div>

</div>


 <div className="absolute inset-0 z-20 flex mx-[8vw] my-[7vh]  items-end justify-end pointer-events-none">
  <div className="pointer-events-autorounded-xl px-6 py-6 text-white ">
    <div className="text-justify py-2">
      <h2 className="text-1xl w-[25vw] font-mono">I’m a curious, adaptable learner with hands-on experience across web development, Android, marketing, operations, and content creation. My journey spans both technical and creative domains—building frontends, designing interfaces, promoting events, engaging sponsors, and crafting social media content.
</h2>
    
    </div>

    <div className="w-[25vw]  border-t my-3" />

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
      


     <div className="flex justify-center relative items-center w-fullz-10">
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


     
    </section>
  );
}
