<%block name="html_tag">
<html>
</%block>

<%inherit file="syncform:templates/head.html"/>

<%block name="body_tag">
<body>
</%block>

<%inherit file="syncform:templates/header.html"/>
<%inherit file="syncform:templates/nav.html"/>

<img src="${request.static_url('syncform:images/user_thumbnail.jpg')}" /> </div>

%for row in range(1,2):
	<a href="${request.route_url('Login')}">Login<a></br>
	<a href="${request.route_url('Registration')}">Registration<a></br>
	<a href="${request.route_url('AdminPanel')}">Admin Panel<a></br>
	<a href="${request.route_url('Blog')}">Blog<a></br>
	<a href="${request.route_url('Calendar')}">Calendar<a></br>
	<a href="${request.route_url('Directory')}">Directory<a></br>
	<a href="${request.route_url('Files')}">Files<a></br>
	<a href="${request.route_url('Profile')}">Profile<a></br>
	<a href="${request.route_url('Tasks')}">Tasks<a></br>
	<a href="${request.route_url('Workspace')}">Workspace<a></br>
%endfor

<%inherit file="syncform:templates/footer.html"/>

<%block name="body_tag">
</body>
</%block>
<%block name="html_tag">
</html>
</%block>