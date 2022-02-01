module.exports = {
  apps : [{
    name: "Mongo-Express GUI",
    script: 'node_modules/mongo-express/app.js',
    env: {
      "ME_CONFIG_BASICAUTH_USERNAME": "admin",
      "ME_CONFIG_BASICAUTH_PASSWORD": "turnkeypw",
      "ME_CONFIG_MONGODB_ENABLE_ADMIN": "true",
      "ME_CONFIG_SITE_BASEURL": "/mongo",
      "ME_CONFIG_SITE_SSL_ENABLED": "true",
      "ME_CONFIG_SITE_COOKIESECRET": "turnkey1",
      "ME_CONFIG_SITE_SESSIONSECRET": "turnkey2"
    }
  }, {
    name: "TurnKey Linux CP",
    script: './tklweb-cp.js'
  }],

  deploy : {
  }
};
