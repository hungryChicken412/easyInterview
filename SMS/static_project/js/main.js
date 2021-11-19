$(document).ready(function () {

  $(window).scroll(function () {
    let scroll = $(window).scrollTop();
    if (scroll > 70) {
      $(".nav-parent").addClass("nav-changeColor")
    }
    else {
      $(".nav-parent").removeClass("nav-changeColor")
    }
  });

  $(".hamburger").click(function () {
    $(".bar1").toggleClass("bar1-open")
    $(".bar2").toggleClass("bar2-open")
    $(".bar3").toggleClass("bar3-open")
    $(".nav-menu").toggleClass("menu-open")

    let scroll = $(window).scrollTop();
    if (scroll < 70) {
      $(".nav-parent").toggleClass("nav-changeColor")
    }
  })

  $(".nav-item").click(function () {

    $(".bar1").toggleClass("bar1-open")
    $(".bar2").toggleClass("bar2-open")
    $(".bar3").toggleClass("bar3-open")
    $(".nav-menu").toggleClass("menu-open")
  })

  // slick 

  $('.our-game-slider-parent').slick({
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    adaptiveHeight: true
  });


})
