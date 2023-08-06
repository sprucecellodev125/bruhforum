import "bootstrap/dist/css/bootstrap.min.css";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";

function Createpost() {
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
        <h3>Create new post</h3>
        <Form>
          <Form.Group className="mb-3" controlId="formTitle">
            <Form.Label>Title</Form.Label>
            <Form.Control type="text" />
          </Form.Group>
          <Form.Group className="mb-3" controlId="formText">
            <Form.Label>Message</Form.Label>
            <Form.Control as="textarea" rows={5} />
          </Form.Group>
          <Button variant="primary" type="submit">
            Submit
          </Button>
        </Form>
      </Container>
    </>
  );
}

export default Createpost;
