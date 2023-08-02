import 'bootstrap/dist/css/bootstrap.min.css';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';

function Homepage() {
  return (
    <>
      <Navbar expand="lg" style={{backgroundColor: `#e3f2fd`}}>
        <Container fluid>
          <Navbar.Brand href="/">Bruhforum</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="/create">Create</Nav.Link>
              <Nav.Link href="#overview">Forum settings</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      <Container>
        <h1>Hello world</h1>
      </Container>
    </>
  );
}

export default Homepage;
