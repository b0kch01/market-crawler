import React, { useState } from 'react';

const Carousel = ({ children }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const count = React.Children.count(children);

  const goToPrevious = () => {
    setCurrentIndex((prevState) => (prevState - 1 + count) % count);
  };

  const goToNext = () => {
    setCurrentIndex((prevState) => (prevState + 1) % count);
  };

  return (
    <div className="relative">
      <div className="overflow-hidden">
        <div className="flex transition-transform duration-500" style={{ transform: `translateX(-${currentIndex * 100}%)` }}>
          {children}
        </div>
      </div>
      <button onClick={goToPrevious} className="absolute top-1/2 left-0 transform -translate-y-1/2 bg-gray-800 text-white p-2">
        Prev
      </button>
      <button onClick={goToNext} className="absolute top-1/2 right-0 transform -translate-y-1/2 bg-gray-800 text-white p-2">
        Next
      </button>
    </div>
  );
};

export default Carousel;
