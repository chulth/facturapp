const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    // ... Configuración de empaquetado
    entry: './src/index.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js',
    },
    mode: 'development', 
    resolve: {
        extensions:['.js','.jsx']
    },
    module: {
        // ... Lista de reglas respecto a los loaders	
        rules : [
            // Reglas para babel
            {
                test: /\.(js | jsx)$/,
                use: { loader: 'babel-loader'},
                exclude: /node_modules/
            },
            // Reglas para HTML loader
            {
		test: /\.html$/,
		use: [{ loader: 'html-loader'}]
           }

        ]

    },
    plugins: [
	    //... Configuración de plugins
        new HtmlWebpackPlugin(
		{ 
      		template: './public/index.html', 
		filename: './index.html'   
		}
	)
	]
}
