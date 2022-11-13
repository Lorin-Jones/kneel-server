CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `timestamp` NUMERIC(10) NOT NULL,
    FOREIGN KEY(`size_id`) REFERENCES `Size`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Style`(`id`),
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`)
);
    
    
    

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` INTEGER NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(30),
    `price` NUMERIC(10)
);

INSERT INTO `Metals` VALUES (null, "Sterling Silver", 12.42);
INSERT INTO `Metals` VALUES (null, "14K Gold", 736.4);
INSERT INTO `Metals` VALUES (null, "24K Gold", 1258.9);
INSERT INTO `Metals` VALUES (null, "Platinum", 795.45);
INSERT INTO `Metals` VALUES (null, "Palladium", 1241.0)

INSERT INTO `Sizes` VALUES (null, 0.5, 405);
INSERT INTO `Sizes` VALUES (null, 0.75, 782);
INSERT INTO `Sizes` VALUES (null, 1, 1470);
INSERT INTO `Sizes` VALUES (null, 1.5, 1997);
INSERT INTO `Sizes` VALUES (null, 2, 3638)

INSERT INTO `Styles` VALUES (null, "Classic", 500);
INSERT INTO `Styles` VALUES (null, "Modern", 710);
INSERT INTO `Styles` VALUES (null, "Vintage", 965)

INSERT INTO `Orders` VALUES (null, 3, 2, 3, 1614659931693);
SELECT * FROM Metals

SELECT
    o.metal_id,
    o.style_id,
    o.size_id,
    o.timestamp,
    m.metal,
    m.price
    -- You select the rest of the columns from the joined tables here
FROM `Orders` o
JOIN Metals m ON m.id = o.metal_id
-- You write the rest of the JOIN clauses here

