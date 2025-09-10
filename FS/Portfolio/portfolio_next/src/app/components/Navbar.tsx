const Navbar = () => {
  return (
    <nav className="absolute top-[3vh] left-0 w-full z-20 text-white">
      <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto px-6 py-5">
        <a
          href="#"
          className="flex items-center space-x-3 rtl:space-x-reverse"
        >
          <span className="self-center text-5xl font-bold whitespace-nowrap dark:text-white">
            Portfolio
          </span>
        </a>

        <div className="flex items-center md:order-2 space-x-5 md:space-x-0 rtl:space-x-reverse text-white">
          <button
            type="button"
            className="flex text-sm text-white bg-gray-800 rounded-full md:me-0 focus:ring-4 focus:ring-gray-300 dark:focus:white"
            id="user-menu-button"
            aria-expanded="false"
          >
            <span className="sr-only">Open user menu</span>
            <img
              className="w-10 h-10 rounded-full"
              src="/profile_pic_siddhanth.jpg"
              alt="user photo"
            />
          </button>

          <button
            data-collapse-toggle="navbar-user"
            type="button"
            className="inline-flex items-center p-3 w-12 h-12 justify-center text-lg text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200"
            aria-controls="navbar-user"
            aria-expanded="false"
          >
            <span className="sr-only">Open main menu</span>
            <svg
              className="w-6 h-6"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 17 14"
            ></svg>
          </button>
        </div>

        <div
          className="items-center justify-between hidden w-full md:flex md:w-auto md:order-1 text-white"
          id="navbar-user"
        >
          <ul className="flex flex-col font-medium text-lg p-4 md:p-0 mt-4 border border-gray-100 rounded-lg md:space-x-10 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0">
            <li>
              <a
                href="/"
                className="block py-2 text-3xl px-4 text-white bg-[#C9FE05] rounded-sm md:bg-transparent md:text-[#C9FE05] md:p-0"
                aria-current="page"
              >
                Home
              </a>
            </li>
            <li>
              <a
                href="/experience"
                className="block py-2 px-4 rounded-sm  text-3xl md:hover:bg-transparent hover:text-[#C9FE05] md:p-0 dark:text-white"
              >
                Experience
              </a>
            </li>
            <li>
              <a
                href="#"
                className="block py-2 px-4  rounded-sm text-3xl  md:hover:bg-transparent hover:text-[#C9FE05] md:p-0 dark:text-white"
              >
                Contact
              </a>
            </li>
          </ul>
        </div>
      </div>
         <div className="w-auto flex justify-center border-t mx-[10vw] my-[2vh] " />
    </nav>
  );
};

export default Navbar;
