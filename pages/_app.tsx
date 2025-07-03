// pages/_app.tsx
import type { AppProps } from 'next/app';
import { ThemeProvider } from 'styled-components';
import { Analytics } from '@vercel/analytics/next';
import Layout from '../components/Layout';

const theme = {
  colors: {
    primary: '#0070f3',
    background: '#f0f0f0',
    text: '#333'
  }
};

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ThemeProvider theme={theme}>
      <Layout>
        <Component {...pageProps} />
        <Analytics />
      </Layout>
    </ThemeProvider>
  );
}

export default MyApp;

// import type { AppProps } from 'next/app';
// import { Analytics } from '@vercel/analytics/next';
 
// function MyApp({ Component, pageProps }: AppProps) {
//   return (
//     <>
//       <Component {...pageProps} />
//       <Analytics />
//     </>
//   );
// }
 
// export default MyApp;