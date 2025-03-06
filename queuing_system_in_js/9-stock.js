const express = require('express');
const Redis = require('ioredis');
const app = express();

// Middleware to parse JSON bodies
app.use(express.json());

// Create Redis client
const redis = new Redis({
  host: 'localhost',
  port: 6379,
  maxRetriesPerRequest: 1
});

// Products array
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Function to get item by ID
function getItemById(id) {
  return listProducts.find(product => product.id === id);
}

// Function to reserve stock
async function reserveStockById(itemId, stock) {
  try {
    // Set stock in Redis with key format: item.ITEM_ID
    await redis.set(`item.${itemId}`, stock.toString());
    return true;
  } catch (error) {
    console.error('Error reserving stock:', error);
    return false;
  }
}

// Function to get current reserved stock
async function getCurrentReservedStockById(itemId) {
  try {
    const stock = await redis.get(`item.${itemId}`);
    return stock ? parseInt(stock) : null;
  } catch (error) {
    console.error('Error getting stock:', error);
    return null;
  }
}

// Route to get product details
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  
  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = currentStock !== null ? product.stock - currentStock : product.stock;

  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: currentQuantity
  });
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const availableStock = currentStock !== null ? product.stock - currentStock : product.stock;

  if (availableStock <= 0) {
    return res.json({ 
      status: 'Not enough stock available',
      itemId: itemId 
    });
  }

  // Reserve one item
  const newStock = currentStock !== null ? currentStock + 1 : 1;
  await reserveStockById(itemId, newStock);

  res.json({ 
    status: 'Reservation confirmed',
    itemId: itemId 
  });
});

// Start the server
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});