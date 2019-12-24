<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style lang="scss">
  * {
    font-family: 'Roboto', sans-serif;
    touch-action: manipulation;
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    text-align: left;
    color: #212529;
  }

  body, html {
    height: 100%;
    background: #f0f0f0 !important;
  }

  .custom-control-input:checked ~ .custom-control-label::before {
    color: #fff;
    border-color: #00b46e;
    background-color: #00b46e;
  }

  .header-no-nav {
    position: -webkit-sticky;
    position: sticky;
    padding: 0.5rem 1rem;
    top: 0;
    background-color: #fff;
    z-index: 100;
    align-items: center;
    box-shadow: 0px 3px 20px rgba(0,0,0,0.08)
  }

  .contact-us-text {
    color: #00b46e;
    text-decoration: none;
    background-color: transparent;
  }

  .contact-us-text:hover {
    color: #00683f;
    text-transform: color 0.2s;
  }

  .top-nav-contact-us:hover {
    text-decoration: none;
    .contact-us-text {
      color: #00683f;
    }
    .icon-phone-square {
      color: #00683f;
    }
  }
</style>
