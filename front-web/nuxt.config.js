export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s - abocados',
    title: 'abocados',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@fortawesome/fontawesome-svg-core/styles.css'
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    '~/plugins/services.plugin.js',
    '~/plugins/filter.plugin.js',
    '~/plugins/init.client.js',
    '~plugins/modal.plugin.js',
    '~plugins/route.plugin.js',
    '~plugins/fontawesome.plugin.js',
    '~plugins/material.plugin.js'
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: {
    dirs: [
      '~/components',
      '~/components/common/',
      '~/components/layout/',
      '~/components/recipe/',
      '~/components/meal/',
      '~/components/search/'
    ]
  },

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
    '@nuxtjs/google-fonts',
    // https://github.com/nuxt-community/device-module
    '@nuxtjs/device'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/i18n',
    'cookie-universal-nuxt'
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {},

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    treeShake: true,
    theme: {
      options: {
        customProperties: true
      },
      themes: {
        light: {
          primary: '#8fcb42',
          secondary: '#3a3b3b',
          accent: '#2e8449',
          orangee: '#FF4322'
        }
      }
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  },

  i18n: {
    locales: [
      { code: 'es', name: 'Español', file: 'es.js' },
      { code: 'en', name: 'English', file: 'en.js' }
      // { code: 'ko', name: '한국어', file: 'kr.js' }
    ],
    defaultLocale: 'en',
    langDir: '~/locales/',
    skipSettingLocaleOnNavigate: true,
    strategy: 'no_prefix'
  },

  googleFonts: {
    families: {
      'Nanum+Pen+Script': [400, 700],
      'Nanum+Gothic': [400, 700],
      Raleway: [100, 400, 700],
      Roboto: [100, 400, 700, 900],
      Exo: [100, 400, 700, 900],
      Poppins: [100, 400, 700, 900]
    }
  },

  server: {
    host: '0', // default: localhost,
    port: 3000, // default: 3000
    watch: {
      usePolling: true,
    },
  },

  ssr: true,
  target: 'server',

  publicRuntimeConfig: {
    s3: process.env.AWS_S3_ENDPOINT_URL,
    server: process.env.SERVER_ENDPOINT,
  },

  eslint: {
    fix: true
  },
}
