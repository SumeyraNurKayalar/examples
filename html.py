<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Google</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      background: white;
      text-align: center;
    }

    .logo {
      margin-top: 100px;
    }

    .search-box {
      margin-top: 30px;
    }

    input[type="text"] {
      width: 550px;
      height: 44px;
      padding: 0 20px;
      border: 1px solid #dcdcdc;
      border-radius: 24px;
      font-size: 16px;
      outline: none;
      transition: box-shadow 0.3s ease-in-out;
    }

    input[type="text"]:focus {
      box-shadow: 0 0 5px #4285f4;
    }

    .buttons {
      margin-top: 20px;
    }

    button {
      background-color: #f8f9fa;
      border: 1px solid #f8f9fa;
      border-radius: 4px;
      color: #3c4043;
      font-size: 14px;
      padding: 10px 20px;
      margin: 5px;
      cursor: pointer;
    }

    button:hover {
      border: 1px solid #dadce0;
      box-shadow: 0 1px 1px rgba(0,0,0,0.1);
    }

    footer {
      position: absolute;
      bottom: 20px;
      width: 100%;
      font-size: 12px;
      color: #999;
    }
  </style>
</head>
<body>

  <div class="logo">
    <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" alt="Google Logo" width="272" height="92">
  </div>

  <div class="search-box">
    <input type="text" id="searchInput" placeholder="Search Google or type a URL">
  </div>

  <div class="buttons">
    <button onclick="searchGoogle()">Google Search</button>
    <button onclick="feelingLucky()">I'm Feeling Lucky</button>
    <button onclick="searchImages()">Image Search</button>
  </div>

  <footer>
    This is a Google homepage clone for educational purposes.
  </footer>

  <script>
    function getSearchQuery() {
      return document.getElementById('searchInput').value.trim();
    }

    function searchGoogle() {
      const query = getSearchQuery();
      if (query) {
        window.location.href = `https://www.google.com/search?q=${encodeURIComponent(query)}`;
      }
    }

    function feelingLucky() {
      const query = getSearchQuery();
      if (query) {
        window.location.href = `https://www.google.com/search?q=${encodeURIComponent(query)}&btnI=1`;
      }
    }

    function searchImages() {
      const query = getSearchQuery();
      if (query) {
        window.location.href = `https://www.google.com/search?tbm=isch&q=${encodeURIComponent(query)}`;
      }
    }

    // Enter tuşuna basınca arama yap
    document.getElementById("searchInput").addEventListener("keydown", function(event) {
      if (event.key === "Enter") {
        searchGoogle();
      }
    });
  </script>
</body>
</html>
