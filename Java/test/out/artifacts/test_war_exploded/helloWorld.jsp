<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<%@ page import="java.util.*" %>
<%
    Cookie[] cookies = request.getCookies();
    String color = request.getParameter("color");
    if (color == null)
        color = "white";

    if (request.getParameter("format") != null && request.getParameter("format").equals("json"))
    {
        response.setContentType("application/json");
    }
    else
        if (request.getParameter("format") != null && request.getParameter("format").equals("xml"))
        {
            response.setContentType("application/xml");
        }

%>
<body BGCOLOR="<%= color %>">
<div>
    <%!
        private String message = "Hello World!";
        private String comment = "(ass sin thru da JSP I's)";
        private int times = 0;
    %>
    <p><%= message %></p>
    <p><%= comment %></p>
    <div>
        <ul>
            <li> <%= new java.util.Date() %> </li>
            <li> <%= request.getRemoteHost() %> </li>
            <li> <%= session.getId() %> </li>
            <li> <%= "You've been here " + ++times + " times" %></li>
            <% if (request.getParameter("test") != null && request.getParameter("test").equals("redirect")) { %>
                <jsp:forward page="index.jsp" />
            <% } else { %>
                <li> <%= request.getParameter("test") %></li>
            <% } %>
        </ul>

    </div>
    <div>
        <%
            if (request.getParameter("include") != null && request.getParameter("include").equals("index")) {
        %>
        <jsp:include page="index.jsp" />
        <% } %>
    </div>
</div>
</body>
</html>