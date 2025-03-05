const request = require("request");
const app = require("./api");
const chai = require("chai");
const expect = chai.expect;

const url = "http://localhost:7865/";

describe("API Endpoints", () => {
  // Available Payments Tests
  describe("GET /", () => {
    it("should return status 200", function (done) {
      request('http://localhost:7865/', function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        done();
      });
    });
    
    it("should return Welcome to the payment system", function (done) {
      request('http://localhost:7865/', function (error, response, body) {
        expect(body).to.equal("Welcome to the payment system");
        done();
      });
    });
  });

  it("should return status 200", function (done) {
    request(url + "cart/1", function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });
  it("should return 404 with wrong id type", function (done) {
    request(url + "cart/a", function (error, response, body) {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
  it("should return the correct content", function (done) {
    request(url + 'cart/124', function (error, response, body) {
      expect(body).to.equal("Payment methods for cart 124");
      done();
    });
  });

  describe("GET /available_payments", () => {
    it("should return payment methods", (done) => {
      request.get(
        "http://localhost:7865/available_payments",
        { json: true },
        (error, response, body) => {
          expect(response.statusCode).to.equal(200);
          // expect(body).toHaveProperty("payment_methods");
          expect(body.payment_methods).to.equal({
            credit_cards: true,
            paypal: false,
          });
          done();
        }
      );
    });
  });

  describe("/login endpoint", () => {
    it("should welcome the user", (done) => {
      request.post(
        { url: `http://localhost:7865/login`, 
          json: true, 
          body: { userName: "Betty" } 
        },
        (error, response, body) => {
          if(error) {
            console.log(error);
          }
          // expect(response.statusCode).to.equal(200);
          expect(body.message).to.equal("Welcome Betty");
          done();
        }
      );
    });
  });
});
