import gulp from "gulp";
import autoprefixer from "gulp-autoprefixer";
import htmlmin from "gulp-htmlmin";
import gulpSass from "gulp-sass";
import concat from "gulp-concat";
import terser from "gulp-terser";
import sass from "sass";
import browserSync from "browser-sync";

const sassForTask = gulpSass(sass);

const routes = {
  html: {
    src: "client/templates/**/*.html",
    dest: "templates",
  },
  scss: {
    src: "client/scss/**/*.scss",
    dest: "static",
  },
  js: {
    src: "client/js/**/*.js",
    dest: "static",
  },
};

function MinifyHTML() {
  return gulp
    .src(routes.html.src)
    .pipe(
      htmlmin({ collapseWhitespace: true, collapseBooleanAttributes: true })
    )
    .pipe(gulp.dest(routes.html.dest))
    .pipe(browserSync.stream());
}

function SCSStoMinifyCSS() {
  return gulp
    .src(routes.scss.src)
    .pipe(
      sassForTask({ outputStyle: "compressed", sourceMap: true }).on(
        "error",
        sassForTask.logError
      )
    )
    .pipe(autoprefixer())
    .pipe(concat("style.min.css"))
    .pipe(gulp.dest(routes.scss.dest))
    .pipe(browserSync.stream());
}

function UglifyAndMinifyJS() {
  const terserOptions = {
    mangle: {
      toplevel: true,
      safari10: true,
      keep_classnames: true,
    },
  };

  return gulp
    .src(routes.js.src)
    .pipe(terser(terserOptions))
    .pipe(concat("main.min.js"))
    .pipe(gulp.dest(routes.js.dest))
    .pipe(browserSync.stream());
}

function Watch() {
  browserSync.init({
    notify: false,
    host: "127.0.0.1",
    port: 8000,
    ui: {
      host: "127.0.0.1",
      port: 8000,
    },
    proxy: "http://127.0.0.1:8000",
  });
  gulp.watch(routes.html.src, MinifyHTML).on("change", browserSync.reload);
  gulp.watch(routes.scss.src, SCSStoMinifyCSS).on("change", browserSync.reload);
  gulp.watch(routes.js.src, UglifyAndMinifyJS).on("change", browserSync.reload);
}

const compile = gulp.series([MinifyHTML, SCSStoMinifyCSS, UglifyAndMinifyJS]);
exports.dev = gulp.series([compile, Watch]);
