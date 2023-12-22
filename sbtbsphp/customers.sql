-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 07, 2022 at 05:49 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sbtbsphp`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(100) NOT NULL,
  `customer_id` varchar(255) NOT NULL,
  `customer_name` varchar(30) NOT NULL,
  `customer_phone` varchar(10) NOT NULL,
  `customer_created` datetime NOT NULL DEFAULT current_timestamp(),
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `customer_id`, `customer_name`, `customer_phone`, `customer_created`, `email`) VALUES
(34, 'CUST-2114034', 'Dfirst Dlast', '7002001200', '2021-10-16 22:09:12', ''),
(35, 'CUST-8996235', 'Willian Hobbs', '4012222222', '2021-10-17 22:30:23', ''),
(36, 'CUST-2017936', 'George Watts', '7011111111', '2021-10-17 22:30:53', ''),
(37, 'CUST-5585037', 'Bobb Horn', '1111111110', '2021-10-17 22:31:20', ''),
(38, 'CUST-9474738', 'Alan Moore', '7900000000', '2021-10-18 09:32:02', ''),
(39, 'CUST-4031139', 'Jamie Rhoades', '1003000010', '2021-10-18 09:33:08', ''),
(40, 'CUST-9997540', 'Demo Customer', '7777777700', '2021-10-18 09:39:10', ''),
(41, 'CUST-5235041', 'Akshay Kalushe', '8390509507', '2022-05-11 21:55:21', ''),
(42, 'CUST-6717742', 'Viraj Shimpi', '4545595466', '2022-05-16 15:29:40', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
