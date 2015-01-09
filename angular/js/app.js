	// the app module
	var mainApp = angular.module('mainApp', ['ngRoute','ngResource']);

	// configured routes
	mainApp.config(function($routeProvider) {
		$routeProvider

		// projectlist dashboard view
		.when('/', {
			templateUrl: 'views/projectlist.html',
			controller: 'mainController'
		})

		// project view
		.when('/project', {
			templateUrl: 'views/project.html',
			controller: 'projectController'
		})

		// new project view
		.when('/new-project', {
			templateUrl: 'views/new-project.html',
			controller: 'new-projectController'
		})

		// recent bills view
		.when('/recentbills', {
			templateUrl: 'views/recentbills.html',
			controller: 'recentbillsController'
		})

		// upcoming bills view
		.when('/upcomingbills', {
			templateUrl: 'views/upcomingbills.html',
			controller: 'upcomingbillsController'
		})

		// list of api's view
		.when('/apilist', {
			templateUrl: 'views/apilist.html',
			controller: 'apilistController'
		})

		// about syncform
		.when('/about', {
			templateUrl: 'views/about.html',
			controller: 'aboutController'
		})

		// legal
		.when('/legal', {
			templateUrl: 'views/legal.html',
			controller: 'legalController'
		})

		// credentials
		.when('/credentials', {
			templateUrl: 'views/credentials.html',
			controller: 'credentialsController'
		})

		// list of api's view
		.when('/monitoring', {
			templateUrl: 'views/monitoring.html',
			controller: 'monitoringController'
		})

		// add contacts view
		.when('/contacts/add', {
			templateUrl: 'views/add.html',
			controller: 'addController'
		})

		// contact cards
		.when('/contacts/:name', {
			templateUrl: 'views/card.html',
			controller: 'cardController'
		})

		// contacts edit
		.when('/contacts/:name/edit', {
			templateUrl: 'views/editor.html',
			controller: 'editorController'
		})

		// admin view
		.when('/admin', {
			templateUrl: 'views/admin.html',
			controller: 'adminController'
		});
	});

	mainApp.controller('mainController', function($scope) {
		$scope.title = 'Cuore Tech';
		$scope.slogan = 'Sync Your World';
		$scope.navStatus = false;
		$scope.barchart = {
		    data: [
				{ y: 'Jan', a: 100, b: 90 },
				{ y: 'Feb', a: 75,  b: 65 },
				{ y: 'Mar', a: 50,  b: 40 },
				{ y: 'Apr', a: 75,  b: 65 },
				{ y: 'May', a: 50,  b: 40 },
				{ y: 'Jun', a: 75,  b: 65 },
				{ y: 'Jul', a: 30, b: 25 },
				{ y: 'Aug', a: 40, b: 35 },
				{ y: 'Sep', a: 20, b: 15 },
				{ y: 'Oct', a: 50, b: 40 },
				{ y: 'Nov', a: 80, b: 55 }
		    ],
		    xkey: 'y',
		    ykeys: ['a', 'b'],
		    gridTextColor: '#fff',
		    labels: ['Hot', 'Warm'],
		    barColors: ['#fff', '#cfcfcf']
		};

		$scope.linechart = {
		    data: [
		      { y: '2008', a: 30, b: 10 },
		      { y: '2009', a: 45,  b: 15 },
		      { y: '2010', a: 50,  b: 5 },
		      { y: '2011', a: 60,  b: 35 },
		      { y: '2012', a: 40,  b: 20 },
		      { y: '2013', a: 60,  b: 30 },
		      { y: '2014', a: 20, b: 10 }
		    ],
		    xkey: 'y',
		    ykeys: ['a', 'b'],
		    gridTextColor: '#fff',
		    labels: ['Series A', 'Series B'],
		    lineColors: ['#fff', '#ccc']
		};

		$scope.donutchart = {
			data: [
				{label: "Percent Used", value: 23},
				{label: "Percent Free", value: 77}
			],
			labelColor: '#fff',
  			colors: ['#a90d15','#efefef','#a90d15']
		};

		$scope.title = 'Project List';
		$scope.slogan = 'Your List of Open Projects';
		$scope.projectlists = [
		{createdate:"12-22-2014", projectname:"Leo's Project", projectid:"021292", requests:"100000", errors:"0", charges:"0"},
		{createdate:"12-15-2014", projectname:"Thomas's Project", projectid:"072793", requests:"50000", errors:"0", charges:"0"},
		{createdate:"12-22-2014", projectname:"Leo's Project", projectid:"021292", requests:"100000", errors:"0", charges:"0"},
		{createdate:"12-22-2014", projectname:"Leo's Project", projectid:"021292", requests:"100000", errors:"0", charges:"0"},
		{createdate:"12-22-2014", projectname:"Leo's Project", projectid:"021292", requests:"100000", errors:"0", charges:"0"},
		]
	});

	mainApp.controller('projectController', function($scope) {
		$scope.title = 'Project';
		$scope.slogan = 'Singular Project View';
		// $scope.billings = get_billings.get();
		// $scope.billings = get_billings.query();
		$scope.billings = [
		{billdate:"12-08-2014", amount:500, requests:100000, startdate:"11-01-2014", enddate:"11-30-2014"},
		{billdate:"11-08-2014", amount:500, requests:100000, startdate:"10-01-2014", enddate:"10-31-2014"},
		{billdate:"10-08-2014", amount:500, requests:100000, startdate:"09-01-2014", enddate:"09-30-2014"},
		{billdate:"09-08-2014", amount:500, requests:100000, startdate:"08-01-2014", enddate:"08-31-2014"},
		{billdate:"08-08-2014", amount:500, requests:100000, startdate:"07-01-2014", enddate:"07-30-2014"},
		{billdate:"07-08-2014", amount:500, requests:100000, startdate:"06-01-2014", enddate:"06-30-2014"},
		{billdate:"06-08-2014", amount:500, requests:100000, startdate:"05-01-2014", enddate:"05-31-2014"},
		]

		$scope.apilists = [
		{name:"NameOfAPI", inputname:"switch1", id:"checked"},
		{name:"NameOfAPI", inputname:"switch2", idoff:"checked"},
		{name:"NameOfAPI", inputname:"switch3", id:"checked"},
		{name:"NameOfAPI", inputname:"switch4", idoff:"checked"},
		{name:"NameOfAPI", inputname:"switch5", id:"checked"},
		]

	});

	mainApp.controller('new-projectController', function($scope) {
		$scope.title = 'New-Project';
		$scope.slogan = 'Create Your New Project';
	});

	mainApp.controller('recentbillsController', function($scope) {
		$scope.title = 'Recent Bills';
		$scope.slogan = 'What You Been Spendin Yo Money On?';
	});

	mainApp.controller('upcomingbillsController', function($scope) {
		$scope.title = 'Upcoming Bills';
		$scope.slogan = 'What You Be Spendin Yo Money On Next';
	});

	mainApp.controller('apilistController', function($scope) {
		$scope.title = 'API List';
		$scope.slogan = 'What APIs You Be Usin';
	});

	mainApp.controller('aboutController', function($scope) {
		$scope.title = 'About';
		$scope.slogan = 'About Us';
	});

	mainApp.controller('legalController', function($scope) {
		$scope.title = 'Legal';
		$scope.slogan = 'Legal';
	});

	mainApp.controller('credentialsController', function($scope) {
		$scope.title = 'Credentials';
		$scope.slogan = 'Oauth and Public Access Keys for your Project';
	});

	mainApp.controller('addController', function($scope) {
		$scope.title = 'Add Contacts';
		$scope.slogan = 'Staying in Touch Made Easy';
	});

	mainApp.controller('cardController', function($scope) {
		$scope.title = 'Single Contact';
		$scope.slogan = 'Staying in Touch Made Easy';
	});

	mainApp.controller('editorController', function($scope) {
		$scope.title = 'Edit Single Contact';
		$scope.slogan = 'Staying in Touch Made Easy';
	});

	mainApp.controller('adminController', function($scope) {
		$scope.title = 'Admin Panel for Managers and Configs';
		$scope.slogan = 'Staying in Touch Made Easy';
	});

	mainApp.directive('barchart', function(){
	  
	  function createChart(el_id, options) {
	    options.element = el_id;
	    var r = new Morris.Bar(options);
	    return r;
	  }

	  return {
	    restrict: 'E',
	    scope: {
	      options: '='
	    },
	    replace: true,
	    template: '<div></div>',
	    link: function link(scope, element, attrs) {
	      return createChart(attrs.id, scope.options);
	    }
	  };
	});

	mainApp.directive('linechart', function() {

	    function createChart(el_id, options) {
	      options.element = el_id;
	      var r = new Morris.Line(options);
	      return r;
	    }

	    return {
	      restrict: 'E',
	      scope:  {
	        options: '='
	      },
	      replace: true,
	      template: '<div></div>',
	      link: function(scope, element, attrs) {
	        return createChart(attrs.id, scope.options)
	      }
	    }
	});

	mainApp.directive('donutchart', function() {

	    function createChart(el_id, options) {
	      options.element = el_id;
	      var r = new Morris.Donut(options);
	      return r;
	    }

	    return {
	      restrict: 'E',
	      scope:  {
	        options: '='
	      },
	      replace: true,
	      template: '<div></div>',
	      link: function(scope, element, attrs) {
	        return createChart(attrs.id, scope.options)
	      }
	    }
	});

  // mainApp.factory('Job',function($resource){
  //   return $resource('http://localhost:8000/api/jobs/:name',{name:'@name'},{
  //       update: {
  //           method: 'PUT'
  //       }
  //   });
  // });

