// api.test.js
const request = require('supertest');
const app = require('./api');

describe('index page', () => {
    it('should return correct status code', (done) => {
        request(app)
            .get('/')
            .expect(200)
            .end((err, res) => {
                if (err) return done(err);
                done();
            });
    });

    it('should return correct message', (done) => {
        request(app)
            .get('/')
            .expect('Welcome to the payment system')
            .end((err, res) => {
                if (err) return done(err);
                done();
            });
    });

    it('should return correct content type', (done) => {
        request(app)
            .get('/')
            .expect('Content-Type', /text\/html/)
            .end((err, res) => {
                if (err) return done(err);
                done();
            });
    });
});