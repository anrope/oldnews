var fb = null;
angular.module('starter.controllers', [])

.controller('AppCtrl', function($scope, $ionicModal, $timeout, $rootScope, $location) {
  
  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //$scope.$on('$ionicView.enter', function(e) {
  //});
  
  $rootScope.location = $location;
  var URL = location.hash;
  var trimmedURL = URL.split('/')[3]
 
  fb = new Firebase("https://blazing-torch-4098.firebaseIO.com/users/anrope-test");

  function zeropad(n){ return n<10 ? '0'+n : n; }

  $rootScope.playlists = 'hi'

  for (var i = 0; i < 10; i++){
 
    var today = new Date();
    var month = zeropad(today.getMonth());
    var day = zeropad(today.getDate());
    var year = today.getFullYear() - i;
    var fullDate = year+'-'+month+'-'+day;

    fb.orderByChild('timestamp').on('value', function(snapshot){
      var values = snapshot.val();
      values.id = i;
      $rootScope.playlists = values;

      $.each(values, function(item){
        values[item].hash = encodeURIComponent(values[item].title.substring(values[item].title.length - 7));
      })
    });
  }
  
  
  // Form data for the login modal
  $scope.loginData = {};

  // Create the login modal that we will use later
  $ionicModal.fromTemplateUrl('templates/login.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modal = modal;
  });

  // Triggered in the login modal to close it
  $scope.closeLogin = function() {
    $scope.modal.hide();
  };

  // Open the login modal
  $scope.login = function() {
    $scope.modal.show();
  };

  // $scope.disableVerticalScrolling = function() {
  //   var scrollPos = $ionicScrollDelegate.getScrollPosition().top;
  //   $ionicScrollDelegate.scrollTo(0, scrollPos, false);
  // } 

  // Perform the login action when the user submits the login form
  $scope.doLogin = function() {
    console.log('Doing login', $scope.loginData);

    // Simulate a login delay. Remove this and replace with your login
    // code if using a login system
    $timeout(function() {
      $scope.closeLogin();
    }, 1000);
  };
})




.controller('PlaylistsCtrl', function($scope) {

  

  

  // $scope.playlists = [
  //   { title: 'Revealed: how Whisper app tracks anonymous users', id: 1, img: "https://my.vetmatrixbase.com/clients/12679/images/cats-animals-grass-kittens--800x960.jpg", desc: "This is a fake descripttion", date:"09/12/2013" },
  //   { title: 'Revealed: how Whisper app tracks anonymous users', id: 2, img: "https://my.vetmatrixbase.com/clients/12679/images/cats-animals-grass-kittens--800x960.jpg", desc: "This is a fake descripttion", date:"09/12/2013" },
  //   { title: 'Revealed: how Whisper app tracks anonymous users', id: 3, img: "https://my.vetmatrixbase.com/clients/12679/images/cats-animals-grass-kittens--800x960.jpg", desc: "This is a fake descripttion", date:"09/12/2013" },
  //   { title: 'Revealed: how Whisper app tracks anonymous users', id: 4, img: "https://my.vetmatrixbase.com/clients/12679/images/cats-animals-grass-kittens--800x960.jpg", desc: "This is a fake descripttion", date:"09/12/2013" },

    
  // ];

  // $scope.weeks = [
  //   { title: 'Revealed: how Whisper app tracks anonymous users', id: 1, img: "https://my.vetmatrixbase.com/clients/12679/images/cats-animals-grass-kittens--800x960.jpg", desc: "This is a fake descripttion", date:"09/12/2013" },
  //   { title: 'Revealed: how Whisper app tracks anonymous users', id: 2, img: "https://my.vetmatrixbase.com/clients/12679/images/cats-animals-grass-kittens--800x960.jpg", desc: "This is a fake descripttion", date:"09/12/2013" },
  //   { title: 'Revealed: how Whisper app tracks anonymous users', id: 3, img: "https://my.vetmatrixbase.com/clients/12679/images/cats-animals-grass-kittens--800x960.jpg", desc: "This is a fake descripttion", date:"09/12/2013" },
  //   { title: 'Revealed: how Whisper app tracks anonymous users', id: 4, img: "https://my.vetmatrixbase.com/clients/12679/images/cats-animals-grass-kittens--800x960.jpg", desc: "This is a fake descripttion", date:"09/12/2013" },

    
  // ];

  
})

.controller('PlaylistCtrl', function($scope, $stateParams) {
  $scope.location = window.location;
  var URL = location.hash;
  var trimmedURL = URL.split('/')[3]
  console.log(trimmedURL)

  console.log('+++ playlists from single view', $scope.playlists)

  $.each($scope.playlists, function(idx, val) {
    console.log('+++ playlist item', idx, val)
    if (val.hash == trimmedURL) {
      $scope.thisArticle = val;
    }
  })

  console.log('+++ thisArticle', $scope.thisArticle)
});
