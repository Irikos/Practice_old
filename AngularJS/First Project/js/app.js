(function() {
  var app = angular.module('store', []);

  app.controller('MinorSwingStoreController', function(){
    this.products = hammocks;
  });

  app.controller('PanelController', function(){
    this.tab = 1;
    this.selectTab = function(setTab) {
      this.tab = setTab;
    }
    this.isSelected = function(checkTab) {
      return this.tab === checkTab;
    }
  });
  var hammocks = [{
    name: 'Ultralight',
    price: 2.95,
    description: '...',
    canPurchase: true,
    soldOut: false,
    images: [
      {
        logo: 'http://www.minorswing.ro/wp-content/uploads/2014/01/logo.png',
        small: 'http://www.minorswing.ro/wp-content/uploads/2016/04/Purple_1-300x300.jpg'
      },
      {
        logo: 'http://www.minorswing.ro/wp-content/uploads/2014/01/logo.png',
        small: 'http://www.minorswing.ro/wp-content/uploads/2015/05/IMG_0614-Edit-300x300.jpg'
      }
    ],
    reviews: [
      {
        author: "ben@example.com",
        stars: 5,
        body: "This is a fucking awesome product!"
      },
      {
        author: "jen@example.com",
        stars: 4,
        body: "Pretty good, but I prefer the Lightweight version"
      }
    ]
  },
  {
    name: "Lightweight",
    price: 5.95,
    description: "...",
    canPurchase: true,
    soldOut: false,
    images: [
      {
        logo: 'http://www.minorswing.ro/wp-content/uploads/2014/01/logo.png',
        small: 'http://www.minorswing.ro/wp-content/uploads/2015/05/IMG_0614-Edit-300x300.jpg'
      }
    ],
    reviews: [
      {
        author: "Tracy@example.com",
        stars: 5,
        body: "This is a ok product!"
      },
      {
        author: "Jared@example.com",
        stars: 4,
        body: "Pretty good, but I need a bigger version"
      }
    ]
  },
  {
    name: "Big Swing",
    price: 5,
    description: "...",
    canPurchase: true,
    soldOut: false,
    images: [
      {
        logo: 'http://www.minorswing.ro/wp-content/uploads/2014/01/logo.png',
        small: 'http://www.minorswing.ro/wp-content/uploads/2015/02/MG_2158-193x193.jpeg'
      }
    ],
    reviews: [
      {
        author: "ben@example.com",
        stars: 3,
        body: "Good when comparing price-quality, but the quality itself is not as good as the comptetitors!"
      },
      {
        author: "jen@example.com",
        stars: 2,
        body: "Meh"
      }
    ]
  }
];
})();
