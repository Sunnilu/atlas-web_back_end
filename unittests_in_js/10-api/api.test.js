const request = require("request");
const app = require("./api");
const chai = require("chai");
const expect = chai.expect;

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

  describe("GET /available_payments", () => {
    it("should return payment methods", (done) => {
      request.get(
        "http://localhost:7865/available_payments",
        { json: true },
        (error, response, body) => {
          expect(response.statusCode).to.equal(200);
          expect(body).toHaveProperty("payment_methods");
          expect(body.payment_methods).toEqual({
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
        { url: `http://localhost:7865/login`, json: { userName: "Betty" } },
        (error, response, body) => {
          expect(response.statusCode).to.equal(200);
          expect(body).to.equal("Welcome Betty");
          done();
        }
      );
    });
  });
});
