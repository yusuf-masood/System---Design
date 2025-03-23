CREATE TABLE recommendation (
    customer_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    score FLOAT NOT NULL
);

INSERT INTO recommendation (product_id, score) VALUES
(101, 4.5),
(102, 3.8),
(103, 5.0);
