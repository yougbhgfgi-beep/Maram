import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { copyFileSync, mkdirSync } from 'node:fs'
import { resolve, dirname } from 'node:path'

const ASSETS = ['photo1.jpg', 'photo2.jpg', 'photo3.jpg', 'photo4.jpg', 'song.mp3', 'video.mp4', 'manifest.json', 'sw.js', 'icon-192.png', 'icon-512.png', 'apple-touch-icon.png', 'favicon.png', 'favicon.ico']

function copyAssetsToDist() {
  return {
    name: 'copy-assets-to-dist',
    apply: 'build',
    closeBundle() {
      const out = resolve(__dirname, 'dist')
      mkdirSync(out, { recursive: true })
      for (const f of ASSETS) {
        try {
          copyFileSync(resolve(__dirname, f), resolve(out, f))
          console.log(`copied ${f} -> dist`)
        } catch (e) {
          console.warn(`skip ${f}: ${e.message}`)
        }
      }
    }
  }
}

export default defineConfig({
  plugins: [react(), copyAssetsToDist()],
  base: './',
})