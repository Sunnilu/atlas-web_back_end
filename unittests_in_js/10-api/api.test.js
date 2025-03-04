const request = require('supertest');
const app = require('./api');

describe('API Endpoints', () => {
    // Existing tests remain unchanged...

    describe('GET /available_payments', () => {
        it('should return available payment methods', async () => {
            const response = await request(app)
                .get('/available_payments')
                .expect('Content-Type', /json/)
                .expect(200);

            expect(response.body).toHaveProperty('payment_methods');
            expect(response.body.payment_methods).toEqual({
                credit_cards: true,
                paypal: false
            });
        });
    });

    describe('POST /login', () => {
        it('should return welcome message with valid username', async () => {
            const response = await request(app)
                .post('/login')
                .send({ userName: 'testUser' })
                .expect('Content-Type', /json/)
                .expect(200);

            expect(response.body).toHaveProperty('message');
            expect(response.body.message).toBe('Welcome testUser');
        });

        it('should return error for missing username', async () => {
            const response = await request(app)
                .post('/login')
                .send({})
                .expect('Content-Type', /json/)
                .expect(400);

            expect(response.body).toHaveProperty('error');
            expect(response.body.error).toBe('Username is required');
        });
    });
});