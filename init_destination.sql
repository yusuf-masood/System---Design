CREATE TABLE recommendation (
    customer_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    score FLOAT NOT NULL
);
