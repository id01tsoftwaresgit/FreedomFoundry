/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './*.html',
    './app/**/*.html',
    './assets/js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#1E40AF', // A strong, trustworthy blue
        'secondary': '#FBBF24', // A vibrant, optimistic yellow/gold
        'neutral': '#1F2937', // A deep, modern gray
        'light-gray': '#F3F4F6',
        'success': '#10B981',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'], // A clean, modern sans-serif font
      },
    },
  },
  plugins: [],
}
