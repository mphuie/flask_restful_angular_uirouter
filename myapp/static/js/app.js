var app = angular.module('plunker', ['ui.router']);


app.config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise('/home');
  $stateProvider
    .state('home', {
      url: '/home',
      templateUrl:'/static/partials/home.html'
    })
})

app.controller('MainCtrl', function($scope) {
  $scope.name = 'World';
});
