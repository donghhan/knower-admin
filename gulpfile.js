const { src, dest, series, parallel, watch } = require("gulp");
const browserySync = require("browser-sync").create();
const autoprefixer = require("gulp-autoprefixer");

const routes = {
  html: {
    src: "client/templates/**/*.html",
    dest: "templates",
  },
  css: {
    src: "client/scss/**/*.scss",
    dest: "static/css",
  },
  js: {
    src: "client/js/**/*.js",
    dest: "static/js",
  },
};

function MinifyHTML() {
  const htmlmin = require("gulp-htmlmin");

  return src(routes.html.src)
    .pipe(htmlmin({ collapseWhitespace: true }))
    .pipe(dest(routes.html.dest))
    .pipe(browserySync.stream());
}

function SCSStoCSS() {
  const sass = require("gulp-sass")(require("sass"));

  return src(routes.css.src)
    .pipe(
      sass({ outputStyle: "compressed", sourceMap: true }).on(
        "error",
        sass.logError
      )
    )
    .pipe(autoprefixer())
    .pipe(dest(routes.css.dest))
    .pipe(browserySync.reload({ stream: true }));
}

function MinifyJS() {
  const rename = require("gulp-rename");
  // const uglify = require("gulp-uglify-es").default;
  const uglify = require("gulp-uglify");
  const pipeline = require("stream/promises").pipeline;

  const uglifyOptions = {
    annotations: false,
    compress: {
      annotations: false,
      drop_console: true,
      awaits: true,
      arrows: true,
      arguments: true,
    },
    mangle: {
      eval: true,
      toplevel: true,
    },
  };

  return src(routes.js.src)
    .pipe(uglify(uglifyOptions))
    .pipe(dest(routes.js.dest));

  // return src(routes.js.src)
  //   .pipe(rename("bundle.min.js"))
  //   .pipe(uglify())
  //   .pipe(dest(routes.js.dest))
  //   .pipe(browserySync.reload({ stream: true }));
}

function Watch() {
  browserySync.init({
    notify: false,
    host: "127.0.0.1",
    port: 8000,
    ui: {
      host: "127.0.0.1",
      port: 8000,
    },
    proxy: "http://127.0.0.1:8000",
  });
  watch(routes.css.src, SCSStoCSS).on("change", browserySync.reload);
  watch(routes.js.src, MinifyJS).on("change", browserySync.reload);
}

const assets = series([MinifyHTML, SCSStoCSS, MinifyJS]);
const live = parallel([Watch]);

exports.dev = series([assets, live]);
