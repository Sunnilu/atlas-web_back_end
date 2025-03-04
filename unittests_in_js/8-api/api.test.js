// api.test.js
const request = require("request");
const chai = require("chai");
const expect = chai.expect;

describe("cart page", () => {
  it("should return status 200", function (done) {
    request(url, function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it("should return 404 when id is not a number", (done) => {
    request(app)
      .get("/cart/abc")
      .expect(404)
      .end((err, res) => {
        if (err) return done(err);
        done();
      });
  });

  it("should return correct payment methods when id is valid", (done) => {
    request(app)
      .get("/cart/123")
      .expect(200)
      .expect({
        methods: ["Credit Card", "PayPal", "Bank Transfer"],
      })
      .end((err, res) => {
        if (err) return done(err);
        done();
      });
  });

  it("should return error message when id is invalid", (done) => {
    request(app)
      .get("/cart/abc")
      .expect(404)
      .expect("Invalid cart ID")
      .end((err, res) => {
        if (err) return done(err);
        done();
      });
  });
});
