$('.carr2').slick({
    centerMode: true,
    centerPadding: '60px',
    autoplay: true,
    autoplaySpeed: 500,
    slidesToShow: 5,
    arrows: false,
    pauseOnHover:false,
    responsive: [
      {
        breakpoint: 768,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: '40px',
          pauseOnHover:false,
          slidesToShow: 3
        }
      },
      {
        breakpoint: 480,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: '40px',
          pauseOnHover:false,
          slidesToShow: 1
        }
      }
    ]
  });