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
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `id` int(100) NOT NULL,
  `booking_id` varchar(255) NOT NULL,
  `customer_id` varchar(255) NOT NULL,
  `route_id` varchar(255) NOT NULL,
  `customer_route` varchar(200) NOT NULL,
  `booked_amount` int(100) NOT NULL,
  `booked_seat` varchar(100) NOT NULL,
  `booking_created` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`id`, `booking_id`, `customer_id`, `route_id`, `customer_route`, `booked_amount`, `booked_seat`, `booking_created`) VALUES
(60, 'TBZJ360', 'CUST-2114034', 'RT-1908653', 'CITY1 &rarr; CITY2', 100, '3', '2021-10-16 22:15:13'),
(61, 'QK0MT61', 'CUST-2017936', 'RT-9941455', 'EDROISCHESTER &rarr; BRUGOW', 110, '15', '2021-10-17 22:36:10'),
(62, 'A8L5662', 'CUST-5585037', 'RT-3835554', 'ZEKA &rarr; ZREGOW', 70, '2', '2021-10-18 00:08:51'),
(63, 'QDNGC63', 'CUST-8996235', 'RT-3835554', 'ZEKA &rarr; ZREGOW', 70, '15', '2021-10-18 09:31:30'),
(64, 'X34RW64', 'CUST-9474738', 'RT-3835554', 'ZEKA &rarr; ZREGOW', 70, '6', '2021-10-18 09:32:21'),
(65, 'JKZVT65', 'CUST-4031139', 'RT-3835554', 'ZEKA &rarr; ZREGOW', 70, '18', '2021-10-18 09:33:36'),
(66, 'HIIAN66', 'CUST-9997540', 'RT-5887160', 'FLORIA &rarr; ARKBY', 118, '16', '2021-10-18 09:40:16'),
(67, 'QLOE167', 'CUST-9997540', 'RT-3835554', 'ZEKA &rarr; ZREGOW', 70, '12', '2021-10-18 09:41:01'),
(69, 'ALRSG69', 'CUST-6717742', 'RT-423661', 'NAGAR &rarr; PUNE', 300, '1', '2022-05-16 15:31:25');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
