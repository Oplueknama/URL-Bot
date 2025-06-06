chrome.proxy.settings.set(
  {
    value: {
      mode: "pac_script",
      pacScript: {
        data: `
          function FindProxyForURL(url, host) {
            if (
              host.indexOf('google-analytics.com') != -1 ||
              host.indexOf('analytics.google.com') != -1
            ) {
              return "PROXY 127.0.0.1:5858";
            }
            if (host.indexOf('go.telegramlink.in') != -1) {
              return "PROXY 127.0.0.1:8989"; // Block
            }
            return "DIRECT";
          }
        `,
        mandatory: true,
      },
    },
    scope: "regular",
  },
  function () {
    console.log("Proxy settings applied");
  }
);
