const sass = require('node-sass');
const NAME_APP = "dataforseo"
module.exports = function (grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    // Task configuration goes here.
    concat: {
      app: {
        src: ['../dev/js/app/**/*.js'],
        dest: '../static/dataforseo/js/app.js'
      },
      vendor: {
        src: ['../dev/js/vendor/**/*.js'],
        dest: '../static/dataforseo/js/lib.js'
      }
    },
    uglify: {
      app: {
        files: { '../static/dataforseo/js/app.min.js': ['../dev/js/app/**/*.js'] }
      },
      vendor: {
        files: { '../static/dataforseo/js/lib.min.js': ['../dev/js/vendor/**/*.js'] }
      }
    },
    sass: {
      dev: {
        options: {
          implementation: sass,
          outputStyle: 'expanded',
          sourceMap: true,
          quiet: true // stop depreciation errors
        },
        files: {
          '../static/dataforseo/css/main.css': '../dev/scss/main.scss'
        }
      },
      deploy: {
        options: {
          implementation: sass,
          outputStyle: 'compressed',
          sourceMap: true,
          quiet: true // stop depreciation errors
        },
        files: {
          '../static/dataforseo/css/main.min.css': '../dev/scss/main.scss'
        }
      }
    },
    watch: {
      options: { livereload: true },
      javascript: {
        files: ['../dev/js/app/**/*.js'],
        tasks: ['concat']
      },
      sass: {
        files: '../dev/scss/**/*.scss',
        tasks: ['sass:dev']
      }
    }
  });

  // Load plugins here.
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Register tasks here.
  grunt.registerTask('default', []);

};
