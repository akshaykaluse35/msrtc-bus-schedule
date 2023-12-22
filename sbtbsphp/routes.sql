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
-- Table structure for table `routes`
--

CREATE TABLE `routes` (
  `id` int(100) NOT NULL,
  `route_id` varchar(255) NOT NULL,
  `bus_no` varchar(155) NOT NULL,
  `route_cities` varchar(255) NOT NULL,
  `route_dep_date` date NOT NULL,
  `route_dep_time` time NOT NULL,
  `route_step_cost` int(100) NOT NULL,
  `route_created` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `routes`
--

INSERT INTO `routes` (`id`, `route_id`, `bus_no`, `route_cities`, `route_dep_date`, `route_dep_time`, `route_step_cost`, `route_created`) VALUES
(53, 'RT-1908653', 'MVL1000', 'CITY1,CITY2', '2021-10-17', '22:05:00', 100, '2021-10-16 22:05:42'),
(54, 'RT-3835554', 'MMM9969', 'ZEKA,ZREGOW', '2021-10-19', '23:13:00', 70, '2021-10-16 22:12:32'),
(55, 'RT-9941455', 'RDH4255', 'EDROISCHESTER,BRUGOW', '2021-10-18', '10:00:00', 110, '2021-10-17 22:34:47'),
(56, 'RT-9069556', 'XYZ7890', 'ANTALAND,ZREGOW', '2021-10-19', '11:40:00', 85, '2021-10-17 23:39:57'),
(57, 'RT-775557', 'ABC0010', 'ENCEFORD,VLIRGINIA', '2021-10-19', '13:30:00', 131, '2021-10-17 23:42:12'),
(58, 'RT-753558', 'TTH8888', 'ARKBY,VEIM', '2021-10-20', '12:04:00', 55, '2021-10-18 00:04:42'),
(59, 'RT-6028759', 'LLL7699', 'BELRITH,ARKBY', '2021-10-20', '13:50:00', 166, '2021-10-18 00:07:50'),
(60, 'RT-5887160', 'CAS3300', 'FLORIA,ARKBY', '2021-10-19', '10:30:00', 118, '2021-10-18 09:38:30'),
(61, 'RT-423661', 'MH17DS1552', 'NAGAR,PUNE', '2022-05-12', '11:08:00', 300, '2022-05-11 23:07:53'),
(62, 'RT-8863562', 'MH17DS1555', 'NEW,DELHI', '2022-05-14', '18:25:00', 100, '2022-05-12 00:25:18'),
(64, 'RT-7909164', 'MH20AL1552', 'JALGAON,NASHIK', '2022-05-20', '13:40:00', 200, '2022-05-19 11:37:42');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `routes`
--
ALTER TABLE `routes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `routes`
--
ALTER TABLE `routes`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
