// components/Layout.tsx
import React from 'react';
import styled from 'styled-components';

const Wrapper = styled.div`
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
`;

const Layout = ({ children }: { children: React.ReactNode }) => {
  return (
    <Wrapper>
      <header>
        <h1>My Awesome App</h1>
      </header>
      <main>{children}</main>
      <footer>© {new Date().getFullYear()} Powered by Next.js</footer>
    </Wrapper>
  );
};

export default Layout;
