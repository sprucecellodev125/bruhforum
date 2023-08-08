import React, { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import Alert from "react-bootstrap/Alert";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Card from "react-bootstrap/Card";
import axios from "axios";

const Homepage = () => {
  const [data, setData] = useState({
    allpost: [],
    name: "",
    rules: "",
    about: "",
  });

  useEffect(() => {
    homepageData();
  }, []);

  const homepageData = async () => {
    try {
      const response = await axios.get("http://localhost:8000/"); // Replace with your API endpoint
      setData(response.data); // Update the state with the fetched data
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };
  return (
    <>
      <Navbar expand="lg" style={{ backgroundColor: `#e3f2fd` }}>
        <Container fluid>
          <Navbar.Brand href="/">{data.name}</Navbar.Brand>
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
          <Alert variant="primary">
            <strong>Note:</strong> This branch is work-in-progress. Some feature
            will be missing for now
          </Alert>
          <Col sm={8}>
            {data.allpost.length > 0 ? (
              data.allpost.map((post) => (
                <Col md={12} key={post.id}>
                  <Card>
                    <Card.Body>
                      <Card.Title>{post.posttitle}</Card.Title>
                      <Card.Subtitle className="text-muted">
                        Posted by {post.postusername} at {post.postdate}
                      </Card.Subtitle>
                      <Card.Text>{post.postmessage}</Card.Text>
                    </Card.Body>
                  </Card>
                </Col>
              ))
            ) : (
              <div className="col-sm-8">
                <p>There's nothing to see here</p>
              </div>
            )}
          </Col>
          <Col sm={4}>
            <Container fluid>
              <h4>Rules</h4>
              <p>{data.rules}</p>
            </Container>
            <Container fluid>
              <h4>About</h4>
              <p>{data.about}</p>
            </Container>
          </Col>
        </Row>
      </Container>
    </>
  );
};

export default Homepage;
