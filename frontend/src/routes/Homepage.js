import "bootstrap/dist/css/bootstrap.min.css";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import Alert from "react-bootstrap/Alert";

function Homepage() {
  return (
    <>
      <Navbar expand="lg" style={{ backgroundColor: `#e3f2fd` }}>
        <Container fluid>
          <Navbar.Brand href="/">Bruhforum</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="/create">Create</Nav.Link>
              <Nav.Link href="/settings/main/">Forum settings</Nav.Link>
            </Nav>
            <Navbar.Text>
              Signed in as:{" "}
              <a className="text-decoration-none" href="#login">
                Test user
              </a>
            </Navbar.Text>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      <br />
      <Container>
        <Alert variant="primary">
          <strong>Note:</strong> This branch is work-in-progress. No function
          that require backend working on here
        </Alert>
      </Container>
    </>
  );
}

export default Homepage;