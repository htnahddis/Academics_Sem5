import { motion } from "framer-motion";

export default function MovingStrip () {
    return (
        <>
         <div className="relative top-0 flex items-center left-0 w-full h-[15vh] overflow-hidden bg-[#C9FE05] text-[#252525] py-3 text-5xl md:text-6xl font-bold">
      <motion.div
        className="flex whitespace-nowrap"
        initial={{ x: "0%" }}
        animate={{ x: "-50%" }}
        transition={{ repeat: Infinity, duration: 80, ease: "linear" }} // slower speed
      >
        <span className="mr-10">
          Learn &nbsp; | &nbsp; Create &nbsp; | &nbsp; Repeat &nbsp; | &nbsp;
        </span>
        <span className="mr-10">
          Learn &nbsp; | &nbsp; Create &nbsp; | &nbsp; Repeat &nbsp; | &nbsp;
        </span>
        <span className="mr-10">
          Learn &nbsp; | &nbsp; Create &nbsp; | &nbsp; Repeat &nbsp; | &nbsp;
        </span>
        <span className="mr-10">
          Learn &nbsp; | &nbsp; Create &nbsp; | &nbsp; Repeat &nbsp; | &nbsp;
        </span>
        <span className="mr-10">
          Learn &nbsp; | &nbsp; Create &nbsp; | &nbsp; Repeat &nbsp; | &nbsp;
        </span>
        <span className="mr-10">
          Learn &nbsp; | &nbsp; Create &nbsp; | &nbsp; Repeat &nbsp; | &nbsp;
        </span>
        <span className="mr-10">
          Learn &nbsp; | &nbsp; Create &nbsp; | &nbsp; Repeat &nbsp; | &nbsp;
        </span>
        <span className="mr-10">
          Learn &nbsp; | &nbsp; Create &nbsp; | &nbsp; Repeat &nbsp; | &nbsp;
        </span>
        <span className="mr-10">
          Learn &nbsp; | &nbsp; Create &nbsp; | &nbsp; Repeat &nbsp; | &nbsp;
        </span>
        <span className="mr-10">
          Learn &nbsp; | &nbsp; Create &nbsp; | &nbsp; Repeat &nbsp; | &nbsp;
        </span>
        <span className="mr-10">
          Learn &nbsp; | &nbsp; Create &nbsp; | &nbsp; Repeat &nbsp; | &nbsp;
        </span>
        <span className="mr-10">
          Learn &nbsp; | &nbsp; Create &nbsp; | &nbsp; Repeat &nbsp; | &nbsp;
        </span>
        
      </motion.div>
    </div>
    </>
    )
}