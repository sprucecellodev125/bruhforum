import "bootstrap/dist/css/bootstrap.min.css";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";

function Forumsettings() {
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
        <Row>
          <Col xs={3}>
            <Button>
              Button with top margin
            </Button>
            <Button style={{ marginTop: "1rem" }}>
              Button with top margin
            </Button>
            <Button style={{ marginTop: "1rem" }}>
              Button with top margin
            </Button>
          </Col>
          <Col xs={8}>Test</Col>
        </Row>
      </Container>
    </>
  );
}

export default Forumsettings;
