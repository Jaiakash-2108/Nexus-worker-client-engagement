-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 09, 2026 at 01:44 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nexus`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(10) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'admin', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `booking_details`
--

CREATE TABLE `booking_details` (
  `id` int(100) NOT NULL,
  `Empname` varchar(30) NOT NULL,
  `Empemail` varchar(30) NOT NULL,
  `Empdesignation` varchar(30) NOT NULL,
  `Empcity` varchar(40) NOT NULL,
  `Empstreet` varchar(30) NOT NULL,
  `Empexperience` varchar(30) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `Useremail` varchar(30) NOT NULL,
  `Userstreet` varchar(30) NOT NULL,
  `Usercity` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL,
  `amount` int(10) NOT NULL,
  `customer_type` varchar(30) NOT NULL,
  `no_of_worker` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `booking_details`
--

INSERT INTO `booking_details` (`id`, `Empname`, `Empemail`, `Empdesignation`, `Empcity`, `Empstreet`, `Empexperience`, `Username`, `Useremail`, `Userstreet`, `Usercity`, `status`, `amount`, `customer_type`, `no_of_worker`) VALUES
(1, 'Chandru', 'chandru2002@gmail.com', 'Carpenter', 'Madurai', 'pachampalayam', '7', 'yogesh', 'yogeshff92@gmail.com', 'morur', 'Namakkal', 'Completed', 350, 'General public', ''),
(2, 'jojii', 'joji@gmail.com', 'carpenter', 'Karur', 'american', '4', 'yogesh', 'jaiakash.it@gmail.com', 'morur', 'Namakkal', 'Completed', 300, 'General public', ''),
(3, 'jojii', 'joji@gmail.com', 'carpenter', 'Karur', 'american', '4', 'yogesh', 'jaiakash.it@gmail.com', 'morur', 'Namakkal', 'Completed', 300, 'General public', ''),
(4, 'Chandru', 'chandru2002@gmail.com', 'Carpenter', 'Madurai', 'pachampalayam', '7', 'yogesh', 'jaiakash.it@gmail.com', 'morur', 'Namakkal', 'Completed', 350, 'General public', ''),
(5, 'Chandru', 'chandru2002@gmail.com', 'Carpenter', 'Madurai', 'pachampalayam', '7', 'srinivas', 'jaiakash.it@gmail.com', 'saravanatheatre', 'Salem', 'Completed', 350, 'Contracter', '4'),
(6, 'Chandru', 'chandru2002@gmail.com', 'Carpenter', 'Madurai', 'pachampalayam', '7', 'srinivas', 'jaiakash.it@gmail.com', 'saravanatheatre', 'Salem', 'Accepted', 350, 'Contracter', '4');

-- --------------------------------------------------------

--
-- Table structure for table `emypregister`
--

CREATE TABLE `emypregister` (
  `id` int(100) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `dob` varchar(30) NOT NULL,
  `Gender` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `proof` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `street` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `state` varchar(30) NOT NULL,
  `country` varchar(30) NOT NULL,
  `designation` varchar(30) NOT NULL,
  `experience` int(3) NOT NULL,
  `Status` varchar(20) NOT NULL,
  `amount` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `emypregister`
--

INSERT INTO `emypregister` (`id`, `Name`, `dob`, `Gender`, `email`, `proof`, `password`, `street`, `city`, `state`, `country`, `designation`, `experience`, `Status`, `amount`) VALUES
(1, 'Sudhesh', '1999-02-18', 'Male', 'sudhesh418@gmail.com', 'photo3.jpeg', '01740', 'singampettai', 'Karur', 'Tamil Nadu', 'India', 'Electrician', 6, 'confirmed', 300),
(2, 'Ajithkumar', '1985-08-29', 'Male', 'ajithkumar2000@gmail.com', 'photo4.jpeg', '32372', 'ammannagar', 'Trichy', 'Tamil Nadu', 'India', 'Electrician', 18, 'confirmed', 400),
(3, 'Chandru', '1993-04-25', 'Male', 'chandru2002@gmail.com', 'photo5.jpeg', '90915', 'pachampalayam', 'Madurai', 'Tamil Nadu', 'India', 'Carpenter', 7, 'confirmed', 350),
(4, 'Kirankumar', '1987-07-25', 'Male', 'kirankumar1995@gmail.com', 'photo6.jpeg', '61690', 'muniappankovil', 'Covai', 'Tamil Nadu', 'India', 'Carpenter', 20, 'confirmed', 500),
(5, 'Deena', '1992-01-01', 'Male', 'deena177@gmail.com', 'photo7.jpeg', '92749', 'vattamalai', 'Theni', 'Tamil Nadu', 'India', 'Painter', 7, 'confirmed', 300),
(6, 'Naveen', '1997-08-29', 'Male', 'naveen1997@gmail.com', 'photo8.jpeg', '84707', 'guruvarettiyur', 'None', 'Tamil Nadu', 'India', 'Painter', 10, 'confirmed', 350),
(7, 'Palanisamy', '1996-05-31', 'Male', 'palanisamy1996@gmail.com', 'photo9.jpeg', '12774', 'ammapettai', 'Namakkal', 'Tamil Nadu', 'India', 'Plumber', 10, 'confirmed', 350),
(8, 'Kishore', '1989-12-12', 'Male', 'kishore2000@gmail.com', 'photo10.jpeg', '13872', 'komarapalyam', 'Salem', 'Tamil Nadu', 'India', 'Plumber', 16, 'confirmed', 400),
(9, 'josh', '2026-01-24', 'Male', 'josh@gmail.com', 'Screenshot 2025-10-29 150350.png', '52920', 'kovil', 'Chennai', 'Tamil Nadu', 'India', 'madurai', 6, 'confirmed', 500),
(10, 'jojii', '2023-05-16', 'Male', 'joji@gmail.com', 'Screenshot 2025-10-21 191411.png', '06344', 'american', 'Karur', 'Tamil Nadu', 'India', 'carpenter', 4, 'confirmed', 300);

-- --------------------------------------------------------

--
-- Table structure for table `feedback_form`
--

CREATE TABLE `feedback_form` (
  `id` int(30) NOT NULL,
  `name` varchar(30) NOT NULL,
  `designation` varchar(30) NOT NULL,
  `workingdays` int(10) NOT NULL,
  `description` varchar(30) NOT NULL,
  `rating` int(40) NOT NULL,
  `street` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `username` varchar(30) NOT NULL,
  `useremail` varchar(30) NOT NULL,
  `userstreet` varchar(30) NOT NULL,
  `usercity` varchar(30) NOT NULL,
  `customer_type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedback_form`
--

INSERT INTO `feedback_form` (`id`, `name`, `designation`, `workingdays`, `description`, `rating`, `street`, `city`, `username`, `useremail`, `userstreet`, `usercity`, `customer_type`) VALUES
(1, 'jojii', 'carpenter', 1, 'The work  was excellent', 5, 'morur', 'Karur', 'yogesh', 'jaiakash.it@gmail.com', 'morur', 'Namakkal', 'General public'),
(2, 'Chandru', 'Carpenter', 1, 'Good Work', 4, 'Madurai', 'Madurai', 'yogesh', 'jaiakash.it@gmail.com', 'morur', 'Namakkal', 'General public'),
(3, 'Chandru', 'Carpenter', 1, 'Excellent Completion', 1, 'Madurai', 'Madurai', 'srinivas', 'jaiakash.it@gmail.com', 'saravanatheatre', 'Salem', 'Contracter');

-- --------------------------------------------------------

--
-- Table structure for table `userregister`
--

CREATE TABLE `userregister` (
  `id` int(100) NOT NULL,
  `name` varchar(30) NOT NULL,
  `dob` varchar(30) NOT NULL,
  `gender` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `proof` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `street` varchar(30) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(30) NOT NULL,
  `country` varchar(40) NOT NULL,
  `customer_type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userregister`
--

INSERT INTO `userregister` (`id`, `name`, `dob`, `gender`, `email`, `proof`, `password`, `street`, `city`, `state`, `country`, `customer_type`) VALUES
(1, 'yogesh', '1999-11-12', 'Male', 'jaiakash.it@gmail.com', '1000000741.jpg', '1111', 'morur', 'Namakkal', 'Tamil Nadu', 'India', 'General public'),
(2, 'lokesh', '2002-05-28', 'Male', 'jaiakash.it@gmail.com', '.trashed-1725791774-IMG_20240809_154939.jpg', '2222', 'neikarapati', 'Erode', 'Tamil Nadu', 'India', 'General public'),
(3, 'srinivas', '2002-10-14', 'Male', 'jaiakash.it@gmail.com', 'photo1.jpeg', '3333', 'saravanatheatre', 'Salem', 'Tamil Nadu', 'India', 'Contracter'),
(4, 'subash', '2001-08-23', 'Male', 'jaiakash.it@gmail.com', 'photo2.jpeg', '4444', 'veppadai', 'Chennai', 'Tamil Nadu', 'India', 'Contracter'),
(5, 'Prabhu', '1998-01-12', 'Male', 'jaiakash.it@gmail.com', 'photo21.jpeg', '5555', 'ottanchatram', 'Trichy', 'Tamil Nadu', 'India', 'General public'),
(6, 'somu ', '1992-09-14', 'Male', 'jaiakash.it@gmail.com', 'photo22.jpeg', '6666', 'kavundanur', 'Namakkal', 'Tamil Nadu', 'India', 'Contracter'),
(7, 'nagamurugan', '2026-01-05', 'Male', 'jaiakash.it@gmail.com', 'Screenshot 2026-01-07 141007.png', '2108', 'nagama nagar', 'Madurai', 'Tamil Nadu', 'India', 'General public'),
(8, 'swetha', '2026-01-04', 'Female', 'swethasen06@gmail.com', 'Screenshot (1).png', '12345', 'neru nagar', 'Trichy', 'Tamil Nadu', 'India', 'General public'),
(9, 'siva', '2026-01-02', 'Female', 'sivapriya141005@gmail.com', 'Screenshot (1).png', '1111', 'mela street', 'Salem', 'Tamil Nadu', 'India', 'General public');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking_details`
--
ALTER TABLE `booking_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `emypregister`
--
ALTER TABLE `emypregister`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feedback_form`
--
ALTER TABLE `feedback_form`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userregister`
--
ALTER TABLE `userregister`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking_details`
--
ALTER TABLE `booking_details`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `emypregister`
--
ALTER TABLE `emypregister`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `feedback_form`
--
ALTER TABLE `feedback_form`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `userregister`
--
ALTER TABLE `userregister`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
