import * as esbuild from 'esbuild'

await esbuild.build({
    entryPoints: ['ipywidget/anywidget.js'],
    bundle: true,
    format: "esm",
    minify: true,
    outfile: 'anywidget-bindings/openlayers.anywidget.dev.js',
})
