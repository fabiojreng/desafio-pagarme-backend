CREATE DATABASE IF NOT EXISTS pagarme;

CREATE TABLE IF NOT EXISTS `pagarme`.`clients` (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS `pagarme`.`transactions` (
    id VARCHAR(50) PRIMARY KEY,
    transaction_value DECIMAL(10, 2) NOT NULL,
    client_id VARCHAR(50) NOT NULL, 
    transaction_description VARCHAR(255) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    card_number VARCHAR(20) NOT NULL,
    cardholder_name VARCHAR(100) NOT NULL,
    card_expiration VARCHAR(7) NOT NULL,
    cvv VARCHAR(4) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

CREATE TABLE IF NOT EXISTS `pagarme`.`payables` (
    id VARCHAR(50) PRIMARY KEY,
    client_id VARCHAR(50) REFERENCES clients(id),
    amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    payment_date DATE NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id)
);