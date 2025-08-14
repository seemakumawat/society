-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 14, 2025 at 04:55 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `finalproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(1) NOT NULL,
  `name` varchar(10) NOT NULL,
  `email` varchar(25) NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `email`, `password`) VALUES
(1, 'dhara', 'dhara90@gmail.com', '7760'),
(2, 'rajesh', 'rajesh12@gmail.com', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `advertisement`
--

CREATE TABLE `advertisement` (
  `ADVERTISE_ID` int(3) NOT NULL,
  `MEMBER_ID` int(3) DEFAULT NULL,
  `DATE` date NOT NULL,
  `DESCRIPTION` varchar(50) NOT NULL,
  `STATUS` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `advertisement`
--

INSERT INTO `advertisement` (`ADVERTISE_ID`, `MEMBER_ID`, `DATE`, `DESCRIPTION`, `STATUS`) VALUES
(1, 1, '2021-05-06', 'need for cook', 'cancel'),
(2, 1, '2022-01-21', 'need for maid', 'cancel'),
(3, 3, '2023-07-26', 'need for caretaker', 'cancel'),
(4, 4, '2023-09-13', 'house sell', 'approve'),
(5, 3, '2024-04-18', 'need for maid', 'approve');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add advertisement', 7, 'add_advertisement'),
(26, 'Can change advertisement', 7, 'change_advertisement'),
(27, 'Can delete advertisement', 7, 'delete_advertisement'),
(28, 'Can view advertisement', 7, 'view_advertisement'),
(29, 'Can add booking', 8, 'add_booking'),
(30, 'Can change booking', 8, 'change_booking'),
(31, 'Can delete booking', 8, 'delete_booking'),
(32, 'Can view booking', 8, 'view_booking'),
(33, 'Can add booking detail', 9, 'add_bookingdetail'),
(34, 'Can change booking detail', 9, 'change_bookingdetail'),
(35, 'Can delete booking detail', 9, 'delete_bookingdetail'),
(36, 'Can view booking detail', 9, 'view_bookingdetail'),
(37, 'Can add committee', 10, 'add_committee'),
(38, 'Can change committee', 10, 'change_committee'),
(39, 'Can delete committee', 10, 'delete_committee'),
(40, 'Can view committee', 10, 'view_committee'),
(41, 'Can add committee details', 11, 'add_committeedetails'),
(42, 'Can change committee details', 11, 'change_committeedetails'),
(43, 'Can delete committee details', 11, 'delete_committeedetails'),
(44, 'Can view committee details', 11, 'view_committeedetails'),
(45, 'Can add complaint', 12, 'add_complaint'),
(46, 'Can change complaint', 12, 'change_complaint'),
(47, 'Can delete complaint', 12, 'delete_complaint'),
(48, 'Can view complaint', 12, 'view_complaint'),
(49, 'Can add deposit', 13, 'add_deposit'),
(50, 'Can change deposit', 13, 'change_deposit'),
(51, 'Can delete deposit', 13, 'delete_deposit'),
(52, 'Can view deposit', 13, 'view_deposit'),
(53, 'Can add expense', 14, 'add_expense'),
(54, 'Can change expense', 14, 'change_expense'),
(55, 'Can delete expense', 14, 'delete_expense'),
(56, 'Can view expense', 14, 'view_expense'),
(57, 'Can add function', 15, 'add_function'),
(58, 'Can change function', 15, 'change_function'),
(59, 'Can delete function', 15, 'delete_function'),
(60, 'Can view function', 15, 'view_function'),
(61, 'Can add income', 16, 'add_income'),
(62, 'Can change income', 16, 'change_income'),
(63, 'Can delete income', 16, 'delete_income'),
(64, 'Can view income', 16, 'view_income'),
(65, 'Can add items', 17, 'add_items'),
(66, 'Can change items', 17, 'change_items'),
(67, 'Can delete items', 17, 'delete_items'),
(68, 'Can view items', 17, 'view_items'),
(69, 'Can add maintenance', 18, 'add_maintenance'),
(70, 'Can change maintenance', 18, 'change_maintenance'),
(71, 'Can delete maintenance', 18, 'delete_maintenance'),
(72, 'Can view maintenance', 18, 'view_maintenance'),
(73, 'Can add member', 19, 'add_member'),
(74, 'Can change member', 19, 'change_member'),
(75, 'Can delete member', 19, 'delete_member'),
(76, 'Can view member', 19, 'view_member'),
(77, 'Can add member function', 20, 'add_memberfunction'),
(78, 'Can change member function', 20, 'change_memberfunction'),
(79, 'Can delete member function', 20, 'delete_memberfunction'),
(80, 'Can view member function', 20, 'view_memberfunction'),
(81, 'Can add member maintenance', 21, 'add_membermaintenance'),
(82, 'Can change member maintenance', 21, 'change_membermaintenance'),
(83, 'Can delete member maintenance', 21, 'delete_membermaintenance'),
(84, 'Can view member maintenance', 21, 'view_membermaintenance'),
(85, 'Can add notice', 22, 'add_notice'),
(86, 'Can change notice', 22, 'change_notice'),
(87, 'Can delete notice', 22, 'delete_notice'),
(88, 'Can view notice', 22, 'view_notice'),
(89, 'Can add occupant', 23, 'add_occupant'),
(90, 'Can change occupant', 23, 'change_occupant'),
(91, 'Can delete occupant', 23, 'delete_occupant'),
(92, 'Can view occupant', 23, 'view_occupant'),
(93, 'Can add auth group', 24, 'add_authgroup'),
(94, 'Can change auth group', 24, 'change_authgroup'),
(95, 'Can delete auth group', 24, 'delete_authgroup'),
(96, 'Can view auth group', 24, 'view_authgroup'),
(97, 'Can add auth group permissions', 25, 'add_authgrouppermissions'),
(98, 'Can change auth group permissions', 25, 'change_authgrouppermissions'),
(99, 'Can delete auth group permissions', 25, 'delete_authgrouppermissions'),
(100, 'Can view auth group permissions', 25, 'view_authgrouppermissions'),
(101, 'Can add auth permission', 26, 'add_authpermission'),
(102, 'Can change auth permission', 26, 'change_authpermission'),
(103, 'Can delete auth permission', 26, 'delete_authpermission'),
(104, 'Can view auth permission', 26, 'view_authpermission'),
(105, 'Can add auth user', 27, 'add_authuser'),
(106, 'Can change auth user', 27, 'change_authuser'),
(107, 'Can delete auth user', 27, 'delete_authuser'),
(108, 'Can view auth user', 27, 'view_authuser'),
(109, 'Can add auth user groups', 28, 'add_authusergroups'),
(110, 'Can change auth user groups', 28, 'change_authusergroups'),
(111, 'Can delete auth user groups', 28, 'delete_authusergroups'),
(112, 'Can view auth user groups', 28, 'view_authusergroups'),
(113, 'Can add auth user user permissions', 29, 'add_authuseruserpermissions'),
(114, 'Can change auth user user permissions', 29, 'change_authuseruserpermissions'),
(115, 'Can delete auth user user permissions', 29, 'delete_authuseruserpermissions'),
(116, 'Can view auth user user permissions', 29, 'view_authuseruserpermissions'),
(117, 'Can add django admin log', 30, 'add_djangoadminlog'),
(118, 'Can change django admin log', 30, 'change_djangoadminlog'),
(119, 'Can delete django admin log', 30, 'delete_djangoadminlog'),
(120, 'Can view django admin log', 30, 'view_djangoadminlog'),
(121, 'Can add django content type', 31, 'add_djangocontenttype'),
(122, 'Can change django content type', 31, 'change_djangocontenttype'),
(123, 'Can delete django content type', 31, 'delete_djangocontenttype'),
(124, 'Can view django content type', 31, 'view_djangocontenttype'),
(125, 'Can add django migrations', 32, 'add_djangomigrations'),
(126, 'Can change django migrations', 32, 'change_djangomigrations'),
(127, 'Can delete django migrations', 32, 'delete_djangomigrations'),
(128, 'Can view django migrations', 32, 'view_djangomigrations'),
(129, 'Can add django session', 33, 'add_djangosession'),
(130, 'Can change django session', 33, 'change_djangosession'),
(131, 'Can delete django session', 33, 'delete_djangosession'),
(132, 'Can view django session', 33, 'view_djangosession'),
(133, 'Can add admin', 34, 'add_admin'),
(134, 'Can change admin', 34, 'change_admin'),
(135, 'Can delete admin', 34, 'delete_admin'),
(136, 'Can view admin', 34, 'view_admin'),
(137, 'Can add cart', 35, 'add_cart'),
(138, 'Can change cart', 35, 'change_cart'),
(139, 'Can delete cart', 35, 'delete_cart'),
(140, 'Can view cart', 35, 'view_cart');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$wKsIcWwLPrD70lFC4DpDKf$AlwYltwYaTPTOutaA+Fgr6CIiZzQxWwNwL4YZtEOBpA=', '2024-02-07 12:38:46.082829', 1, 'seemakumawat', '', '', '', 1, 1, '2024-01-13 12:03:25.535684'),
(2, 'pbkdf2_sha256$720000$TB4ye1mEjCKHBbQfTGg1MV$vb0MI5f+ZlV3JL4h6MIITUd4MZ6Trx76w5d/T+rmxQY=', '2024-01-23 13:35:44.726698', 1, 'seema', '', '', '', 1, 1, '2024-01-23 13:34:34.054584');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `BOOKING_ID` int(3) NOT NULL,
  `MEMBER_ID` int(3) NOT NULL,
  `STARTING_DATE` datetime NOT NULL,
  `ENDING_DATE` datetime NOT NULL,
  `EVENT_NAME` varchar(15) NOT NULL,
  `BOOKING_DATE` date DEFAULT NULL,
  `STATUS` varchar(10) DEFAULT NULL,
  `TOTAL` int(7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`BOOKING_ID`, `MEMBER_ID`, `STARTING_DATE`, `ENDING_DATE`, `EVENT_NAME`, `BOOKING_DATE`, `STATUS`, `TOTAL`) VALUES
(1, 1, '2023-03-07 11:00:00', '2023-03-09 11:00:00', 'marriage', '2023-02-20', 'booked', 3200),
(2, 3, '2023-07-25 06:00:00', '2023-07-25 12:00:00', 'birthday', '2023-07-20', 'booked', 2100),
(3, 4, '2023-08-09 11:00:00', '2023-08-09 11:00:00', 'reception', '2023-08-09', 'pending', 4000),
(4, 9, '2023-09-03 06:00:00', '2023-09-03 09:00:00', 'ring ceramony', '2023-09-03', 'booked', 400),
(7, 1, '2024-02-28 10:02:00', '2024-02-29 10:02:00', 'event', '2024-03-20', 'Pending', 2630),
(8, 1, '2024-04-21 21:56:00', '2024-04-21 21:56:00', 'birthday', '2024-04-20', 'booked', 250),
(9, 1, '2024-04-26 16:53:00', '2024-04-26 20:00:00', 'ring ceremony', '2024-04-24', 'booked', 650),
(10, 1, '2024-04-27 11:05:00', '2024-04-15 11:05:00', 'ring ceremony', '2024-04-26', 'pending', 120);

-- --------------------------------------------------------

--
-- Table structure for table `booking_detail`
--

CREATE TABLE `booking_detail` (
  `BOOKING_DETAIL_ID` int(3) NOT NULL,
  `BOOKING_ID` int(3) NOT NULL,
  `ITEM_ID` int(3) NOT NULL,
  `QUANTITY` int(6) NOT NULL,
  `AMOUNT` int(7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking_detail`
--

INSERT INTO `booking_detail` (`BOOKING_DETAIL_ID`, `BOOKING_ID`, `ITEM_ID`, `QUANTITY`, `AMOUNT`) VALUES
(1, 1, 1, 20, 1000),
(2, 1, 3, 10, 200),
(3, 2, 1, 20, 400),
(4, 2, 3, 10, 200),
(5, 1, 5, 1, 2000),
(6, 2, 6, 1, 1500),
(7, 4, 2, 10, 400),
(8, 3, 4, 200, 4000),
(10, 7, 1, 3, 150),
(11, 7, 2, 12, 480),
(12, 7, 5, 1, 2000),
(13, 8, 1, 5, 250),
(14, 9, 1, 5, 250),
(15, 9, 2, 10, 400),
(16, 10, 1, 2, 100),
(17, 10, 3, 1, 20);

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `cart_id` int(2) NOT NULL,
  `member_id` int(2) NOT NULL,
  `item_id` int(2) NOT NULL,
  `quantity` int(5) NOT NULL,
  `rate` int(5) NOT NULL,
  `total` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`cart_id`, `member_id`, `item_id`, `quantity`, `rate`, `total`) VALUES
(1, 6, 2, 3, 40, 120);

-- --------------------------------------------------------

--
-- Table structure for table `committee`
--

CREATE TABLE `committee` (
  `COMMITTEE_ID` int(3) NOT NULL,
  `WORK_OF_COMMITTEE` varchar(30) NOT NULL,
  `NO._OF_MEMBERS` int(2) NOT NULL,
  `COMMITTEE_CREATION_DATE` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `committee`
--

INSERT INTO `committee` (`COMMITTEE_ID`, `WORK_OF_COMMITTEE`, `NO._OF_MEMBERS`, `COMMITTEE_CREATION_DATE`) VALUES
(1, 'financial', 1, '2018-01-01'),
(2, 'complaint solution', 2, '2018-01-01'),
(3, 'cultural activity', 4, '2018-01-01'),
(4, 'chairman', 2, '2018-01-02');

-- --------------------------------------------------------

--
-- Table structure for table `committee_details`
--

CREATE TABLE `committee_details` (
  `COMMITTEE_DETAIL_ID` int(3) NOT NULL,
  `COMMITTEE_ID` int(3) DEFAULT NULL,
  `MEMBER_ID` int(3) DEFAULT NULL,
  `MEMBER_JOINING_DATE` date NOT NULL,
  `MEMBER_LEAVING_DATE` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `committee_details`
--

INSERT INTO `committee_details` (`COMMITTEE_DETAIL_ID`, `COMMITTEE_ID`, `MEMBER_ID`, `MEMBER_JOINING_DATE`, `MEMBER_LEAVING_DATE`) VALUES
(1, 1, 1, '2018-08-01', '2021-10-18'),
(2, 1, 3, '2018-08-01', '0000-00-00'),
(3, 2, 2, '2019-10-09', '0000-00-00'),
(4, 2, 7, '2018-08-01', '2024-03-09'),
(5, 2, 8, '2018-08-01', '2020-08-01'),
(6, 3, 5, '2018-08-01', '2021-08-04'),
(7, 3, 6, '2018-08-01', '0000-00-00'),
(8, 3, 9, '2018-08-01', '0000-00-00'),
(9, 3, 10, '2018-08-01', '0000-00-00'),
(10, 4, 7, '2018-08-01', '0000-00-00');

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE `complaint` (
  `COMPLAINT_ID` int(3) NOT NULL,
  `MEMBER_ID` int(3) DEFAULT NULL,
  `DESCRIPTION` varchar(50) NOT NULL,
  `COMPLAINT_DATE` date NOT NULL,
  `STATUS` varchar(10) DEFAULT NULL,
  `SOLUTION_DATE` date DEFAULT NULL,
  `COMMITTEE_DETAIL_ID` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`COMPLAINT_ID`, `MEMBER_ID`, `DESCRIPTION`, `COMPLAINT_DATE`, `STATUS`, `SOLUTION_DATE`, `COMMITTEE_DETAIL_ID`) VALUES
(1, 1, 'sweeper do not work well', '2022-07-20', 'solved', '2022-07-24', 3),
(2, 3, 'problem of water supply', '2022-08-10', 'solved', '2022-08-11', 4),
(3, 7, 'lift not working', '2023-07-19', 'solved', '2023-07-20', 3),
(4, 3, 'neighbours play sounds louder', '2023-09-30', 'pending', '0000-00-00', NULL),
(5, 1, 'cleaning', '2024-01-01', 'pending', NULL, NULL),
(8, 1, 'parking', '2024-01-01', 'pending', NULL, NULL),
(9, 4, 'cleaning', '2024-02-07', 'pending', NULL, NULL),
(21, 1, 'parking', '2024-04-07', 'pending', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `deposit`
--

CREATE TABLE `deposit` (
  `DEPOSIT_ID` int(3) NOT NULL,
  `BANK_NAME` varchar(10) DEFAULT NULL,
  `DESCRIPTION` varchar(30) NOT NULL,
  `RATE` int(3) NOT NULL,
  `DEPOSIT_AMOUNT` int(7) NOT NULL,
  `DEPOSIT_DATE` date NOT NULL,
  `MATURITY_DATE` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `deposit`
--

INSERT INTO `deposit` (`DEPOSIT_ID`, `BANK_NAME`, `DESCRIPTION`, `RATE`, `DEPOSIT_AMOUNT`, `DEPOSIT_DATE`, `MATURITY_DATE`) VALUES
(1, 'sbi', 'for 3 year', 3, 200000, '2020-01-01', '2023-01-01'),
(2, 'sbi', 'for 2 year', 3, 300000, '2021-01-01', '2023-01-01'),
(3, 'sbi', 'for 5 years', 2, 300000, '2022-01-01', '2027-01-01'),
(4, 'rbi', 'for 4 years', 3, 200000, '2023-01-01', '2026-01-01'),
(5, 'sbi', 'for 2 years', 2, 100000, '2024-01-01', '2026-01-01'),
(6, 'sbi', 'for 2 years', 2, 200000, '2024-02-02', '2026-02-02'),
(7, 'sbi', 'for 4 years', 2, 300000, '2024-02-01', '2028-02-01'),
(11, 'sbi', 'for 4 years', 2, 2000, '2024-04-06', '2028-04-06');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(34, 'societyapp', 'admin'),
(7, 'societyapp', 'advertisement'),
(24, 'societyapp', 'authgroup'),
(25, 'societyapp', 'authgrouppermissions'),
(26, 'societyapp', 'authpermission'),
(27, 'societyapp', 'authuser'),
(28, 'societyapp', 'authusergroups'),
(29, 'societyapp', 'authuseruserpermissions'),
(8, 'societyapp', 'booking'),
(9, 'societyapp', 'bookingdetail'),
(35, 'societyapp', 'cart'),
(10, 'societyapp', 'committee'),
(11, 'societyapp', 'committeedetails'),
(12, 'societyapp', 'complaint'),
(13, 'societyapp', 'deposit'),
(30, 'societyapp', 'djangoadminlog'),
(31, 'societyapp', 'djangocontenttype'),
(32, 'societyapp', 'djangomigrations'),
(33, 'societyapp', 'djangosession'),
(14, 'societyapp', 'expense'),
(15, 'societyapp', 'function'),
(16, 'societyapp', 'income'),
(17, 'societyapp', 'items'),
(18, 'societyapp', 'maintenance'),
(19, 'societyapp', 'member'),
(20, 'societyapp', 'memberfunction'),
(21, 'societyapp', 'membermaintenance'),
(22, 'societyapp', 'notice'),
(23, 'societyapp', 'occupant');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-01-02 22:02:21.801851'),
(2, 'auth', '0001_initial', '2024-01-02 22:02:33.684766'),
(3, 'admin', '0001_initial', '2024-01-02 22:02:38.123385'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-01-02 22:02:38.244975'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-01-02 22:02:38.350049'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-01-02 22:02:39.706474'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-01-02 22:02:40.835367'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-01-02 22:02:41.000286'),
(9, 'auth', '0004_alter_user_username_opts', '2024-01-02 22:02:41.073338'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-01-02 22:02:41.779702'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-01-02 22:02:41.842188'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-01-02 22:02:41.885887'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-01-02 22:02:42.078539'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-01-02 22:02:42.255150'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-01-02 22:02:42.378237'),
(16, 'auth', '0011_update_proxy_permissions', '2024-01-02 22:02:42.416766'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-01-02 22:02:42.644927'),
(18, 'sessions', '0001_initial', '2024-01-02 22:02:43.229371'),
(19, 'societyapp', '0001_initial', '2024-01-02 22:02:43.301858'),
(20, 'societyapp', '0002_admin', '2024-02-19 14:48:40.198893'),
(21, 'societyapp', '0003_cart', '2024-03-05 10:00:41.279355');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0ud1vvf5ynoh58a9i0k3b9adqar92r74', 'eyJpZCI6MX0:1s0FDD:KxKL6e6iFrgnmebO2CBRlclndane1vh29Wga2mVmtJg', '2024-05-10 06:37:35.087175'),
('6s0dodk1k4l921rj69fpj6t58zhols4g', 'eyJpZCI6MX0:1sHj4S:bFKeL3y-sfyX4uuGlJtN1_7GiSYbQjLp0SfoDMxM2u0', '2024-06-27 11:56:48.025718'),
('d3g0luvwg4o2bckhpwo6au9r2ejx1xp5', 'eyJpZCI6N30:1sHjim:VA4H_0EzX-KigaqPRoxB7UDqh3UlVeeh-6TDurWjOX0', '2024-06-27 12:38:28.309248'),
('dekyyjczpbq0xzbbzv70aapi8zv498ec', 'eyJpZCI6MX0:1sCEPi:bsl_6SeeG3EZHTs4zfSwfCtO3BTAAw7UXQwUIR7tl6w', '2024-06-12 08:12:02.782959'),
('e8xub5tzferacx77h90y0qzfycgnmgve', 'eyJpZCI6N30:1riygp:gD-z25AIRvR8RKmi_kT9UA7yXTjwFIRxBc3ej_XB0AM', '2024-03-23 15:32:47.759881'),
('l38obghh4s20d0634n3k20zf70wmianm', 'eyJpZCI6MX0:1rp3qm:z3HcrZGQ1NbJ7fyzgx85lZ89hsQ3sHpp-218wAte44U', '2024-04-09 10:16:12.944235'),
('tvfb7b1qkyly4cldwq0u8wy02c7rb479', 'eyJpZCI6MX0:1ryWAg:NSLR2nHyZULQNcqL1WE_CQ16Inug428LesB2JwQ9Rww', '2024-05-05 12:19:50.768128'),
('zqdshlfo080uj9grkarxux24wf2n53uq', 'eyJpZCI6MX0:1rfQNJ:98jILccB7P0FLQlfO4VNYjyAo2jXCvpN6Hmx9VzeiCE', '2024-03-13 20:17:57.612090');

-- --------------------------------------------------------

--
-- Table structure for table `expense`
--

CREATE TABLE `expense` (
  `EXPENCE_ID` int(3) NOT NULL,
  `FUNCTION_ID` int(3) DEFAULT NULL,
  `DATE` date NOT NULL,
  `AMOUNT` int(7) NOT NULL,
  `DESCRIPTION` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `expense`
--

INSERT INTO `expense` (`EXPENCE_ID`, `FUNCTION_ID`, `DATE`, `AMOUNT`, `DESCRIPTION`) VALUES
(1, 1, '2023-01-10', 1500, 'food'),
(2, NULL, '2023-09-10', 1000, 'working staff salary'),
(3, NULL, '2023-05-20', 10000, 'renovation cost'),
(4, NULL, '2023-08-10', 2000, 'lift repairing cost'),
(5, 1, '2024-01-14', 5000, 'food'),
(7, 2, '2024-01-01', 30000, 'decoration'),
(10, 2, '2024-02-01', 10000, 'decoration'),
(11, NULL, '2024-01-31', 9000, 'repairing cost');

-- --------------------------------------------------------

--
-- Table structure for table `function`
--

CREATE TABLE `function` (
  `FUNCTION_ID` int(3) NOT NULL,
  `FUNCTION_NAME` varchar(30) NOT NULL,
  `FUNCTION_PLACE` varchar(15) NOT NULL,
  `AMOUNT_PER_MEMBER` int(3) NOT NULL,
  `FDATE` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `function`
--

INSERT INTO `function` (`FUNCTION_ID`, `FUNCTION_NAME`, `FUNCTION_PLACE`, `AMOUNT_PER_MEMBER`, `FDATE`) VALUES
(1, 'uttrayaan celebration', 'common plot', 200, '2023-01-14'),
(2, 'navratri celebration', 'common plot', 150, '2023-09-01'),
(3, 'dashera celebration', 'common plot', 200, '2023-10-01'),
(4, 'diwali celebration', 'society ground', 200, '2023-11-02'),
(5, 'holi', 'society ground', 50, '2024-03-23'),
(6, 'Ganesh chaturthi celebration', 'society ground', 100, '2024-09-07'),
(7, 'Janmashtami celebration', 'society ground', 50, '2024-08-26'),
(8, 'Diwali celebration', 'society ground', 100, '2024-11-01');

-- --------------------------------------------------------

--
-- Table structure for table `income`
--

CREATE TABLE `income` (
  `INCOME_ID` int(3) NOT NULL,
  `MEMBER_MAINTENANCE_ID` int(3) DEFAULT NULL,
  `DEPOSIT_ID` int(3) DEFAULT NULL,
  `BOOKING_ID` int(3) DEFAULT NULL,
  `SOCIETY_EVENT_FUND` varchar(30) DEFAULT NULL,
  `DATE` date DEFAULT NULL,
  `AMOUNT` int(7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `income`
--

INSERT INTO `income` (`INCOME_ID`, `MEMBER_MAINTENANCE_ID`, `DEPOSIT_ID`, `BOOKING_ID`, `SOCIETY_EVENT_FUND`, `DATE`, `AMOUNT`) VALUES
(1, 1, NULL, NULL, NULL, '2023-08-05', 100),
(2, NULL, 1, NULL, NULL, '2022-01-11', 300),
(3, NULL, NULL, 1, NULL, '2023-03-09', 650),
(4, 3, NULL, NULL, NULL, '2023-08-30', 100),
(5, 2, NULL, NULL, NULL, '2024-01-01', 1234),
(10, NULL, NULL, NULL, '2(navratri celebration)', '2024-01-29', 2314),
(11, NULL, NULL, NULL, '4(uttrayaan celebration)', '2024-02-07', 757657),
(33, NULL, NULL, 7, NULL, '2024-03-20', 2630),
(34, NULL, NULL, 8, NULL, '2024-04-20', 250),
(35, NULL, NULL, 9, NULL, '2024-04-24', 650),
(36, NULL, NULL, 10, NULL, '2024-04-26', 120);

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `ITEM_ID` int(3) NOT NULL,
  `ITEM_NAME` varchar(20) NOT NULL,
  `TOTAL_QUANTITY` int(4) NOT NULL,
  `PRICE_PER_UNIT` int(3) NOT NULL,
  `IMAGE` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`ITEM_ID`, `ITEM_NAME`, `TOTAL_QUANTITY`, `PRICE_PER_UNIT`, `IMAGE`) VALUES
(1, 'table fans', 50, 50, '/pimages/tablefan.jpg'),
(2, 'lights', 50, 40, '/pimages/light.jpg'),
(3, 'tables', 50, 20, '/pimages/table.jpg'),
(4, 'chair', 50, 20, '/pimages/chair1.jpg'),
(5, 'common plot', 1, 2000, '/pimages/commanplot.jpg'),
(6, 'club house', 1, 1500, '/pimages/clubhouse_jtd7CpX.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `maintenance`
--

CREATE TABLE `maintenance` (
  `MAINTENANCE_ID` int(3) NOT NULL,
  `MONTH/YEAR` varchar(30) NOT NULL,
  `TOTAL_INCOME` int(10) NOT NULL,
  `TOTAL_EXPENCE` int(10) NOT NULL,
  `AMOUNT_REQUIRED` int(10) NOT NULL,
  `NO._OF_MEMBER` int(5) NOT NULL,
  `MAINTENANCE_AMOUNT` int(5) NOT NULL,
  `LAST_DATE` date NOT NULL,
  `LATE_CHARGES` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `maintenance`
--

INSERT INTO `maintenance` (`MAINTENANCE_ID`, `MONTH/YEAR`, `TOTAL_INCOME`, `TOTAL_EXPENCE`, `AMOUNT_REQUIRED`, `NO._OF_MEMBER`, `MAINTENANCE_AMOUNT`, `LAST_DATE`, `LATE_CHARGES`) VALUES
(1, '2023-07', 25000, 35000, 10000, 10000, 100, '2023-08-01', 40),
(2, '2023-08', 35000, 45000, 10000, 100, 100, '2023-09-01', 0),
(3, '2023-09', 20000, 25000, 5000, 100, 50, '2023-10-01', 50),
(4, '2023-10', 30000, 40000, 10000, 100, 100, '2023-11-01', 0);

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `MEMBER_ID` int(3) NOT NULL,
  `NAME` varchar(20) NOT NULL,
  `DATE_OF_BIRTH` date DEFAULT NULL,
  `EMAIL` varchar(25) NOT NULL,
  `PASSWORD` varchar(15) NOT NULL,
  `CONTACT_NO.` bigint(10) NOT NULL,
  `FLAT_NO.` int(11) NOT NULL,
  `BLOCK_NO.` varchar(1) NOT NULL,
  `GENDER` varchar(6) NOT NULL,
  `RELIGION` varchar(10) DEFAULT NULL,
  `HOUSE_STATUS` varchar(10) NOT NULL,
  `MEMBER_STATUS` varchar(10) NOT NULL,
  `COMMING_DATE` date NOT NULL,
  `LEAVING_DATE` date DEFAULT NULL,
  `FAMILY_MEMBER` int(2) DEFAULT NULL,
  `PROFILE` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`MEMBER_ID`, `NAME`, `DATE_OF_BIRTH`, `EMAIL`, `PASSWORD`, `CONTACT_NO.`, `FLAT_NO.`, `BLOCK_NO.`, `GENDER`, `RELIGION`, `HOUSE_STATUS`, `MEMBER_STATUS`, `COMMING_DATE`, `LEAVING_DATE`, `FAMILY_MEMBER`, `PROFILE`) VALUES
(1, 'rajesh', '1993-01-01', 'rajesh12@gmail.com', '1234', 8290169056, 101, 'A', 'male', 'hindu', 'own', 'Active', '2014-01-01', NULL, 4, '/pimages/m1.jpg'),
(2, 'mahesh', '1994-02-01', 'mahesh23@gmail.com', '8968', 9867452345, 102, 'A', 'male', 'hindu', 'own', 'Active', '2018-10-02', NULL, 3, '/pimages/m2.jpg'),
(3, 'hitesh', '1995-03-01', 'hitesh20@gmail.com', '8808', 9123456789, 301, 'C', 'male', 'hindu', 'own', 'active', '2011-02-01', NULL, 4, '/pimages/m3.jpg'),
(4, 'armaan', '1994-04-01', 'armaan43@gmail.com', '1102', 8760011234, 201, 'B', 'male', 'muslim', 'rent', 'active', '2020-02-19', NULL, 2, '/pimages/m4_jumHLN5.jpg'),
(5, 'harsh', '1992-05-01', 'harsh76@gmail.ccom', '1884', 9123880056, 204, 'B', 'male', 'hindu', 'rent', 'active', '2013-02-08', '0000-00-00', 4, '/pimages/m5.jpg'),
(6, 'aakash', '1994-06-01', 'aakash98@gmail.com', '2200', 8765009934, 106, 'A', 'male', 'sikh', '-', 'inactive', '2014-05-05', '2019-12-18', 3, '/pimages/m6.jpg'),
(7, 'dhara', '2001-07-01', 'dhara90@gmail.com', '7760', 9005612009, 202, 'B', 'female', 'Hindu', 'own', 'active', '2019-04-17', NULL, 2, '/pimages/m11.jpg'),
(8, 'pankaj', '1999-08-01', 'pankaj77@gmail.com', '1088', 9834567891, 302, 'C', 'male', 'hindu', 'own', 'active', '2012-12-20', NULL, 4, '/pimages/m7.jpg'),
(9, 'janvi', '2000-09-01', 'janvi88@gmail.com', '5656', 6754009987, 309, 'C', 'female', 'hindu', 'rent', 'active', '2014-10-05', NULL, 5, '/pimages/m12.jpg'),
(10, 'radha', '1999-10-01', 'radha66@gmail.com', '8900', 9090877654, 305, 'C', 'female', 'hindu', 'rent', 'active', '2011-09-26', '2012-09-26', 2, '/pimages/m13.jpg'),
(20, 'neha', '1998-11-02', 'nehakumawat3011@gmail.com', '3424', 1234567890, 205, 'B', 'female', '-', 'rent', 'Active', '2024-02-01', NULL, 3, ''),
(22, 'karina', NULL, 'karina3011@gmail.com', 'karina', 9234565437, 110, 'A', 'female', '-', 'own', 'active', '2024-02-01', NULL, 4, '/pimages/8.jpg'),
(23, 'jayesh', NULL, 'jayesh@gmail.com', 'jayesh', 7898789878, 320, 'C', 'male', NULL, 'own', 'active', '2020-01-01', NULL, NULL, '/pimages/3_QKVSJv4.jpg'),
(24, 'sahil', '1988-01-07', 'sahil78@gmail.com', '5600', 6789543465, 109, 'A', 'male', 'hindu', 'own', 'active', '2008-03-10', NULL, 4, '/pimages/6_VeuMxqf.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `member_function`
--

CREATE TABLE `member_function` (
  `MEMBER_FUNCTION_ID` int(3) NOT NULL,
  `FUNCTION_ID` int(3) NOT NULL,
  `MEMBER_ID` int(3) NOT NULL,
  `AMOUNT` int(5) NOT NULL,
  `PAY_DATE` date DEFAULT NULL,
  `NO._OF_PASS` int(2) NOT NULL,
  `STATUS` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `member_function`
--

INSERT INTO `member_function` (`MEMBER_FUNCTION_ID`, `FUNCTION_ID`, `MEMBER_ID`, `AMOUNT`, `PAY_DATE`, `NO._OF_PASS`, `STATUS`) VALUES
(1, 1, 1, 400, '2023-01-11', 2, 'paid'),
(2, 3, 3, 400, '2023-09-06', 2, 'paid'),
(3, 3, 3, 400, '2023-09-24', 2, 'paid'),
(4, 4, 7, 800, '2023-10-01', 4, 'paid'),
(5, 2, 6, 300, '2024-02-08', 2, 'paid'),
(6, 5, 4, 150, '2024-02-08', 2, 'paid'),
(8, 8, 1, 600, NULL, 6, 'unpaid'),
(9, 6, 1, 300, NULL, 3, 'unpaid'),
(10, 7, 7, 100, NULL, 2, 'unpaid');

-- --------------------------------------------------------

--
-- Table structure for table `member_maintenance`
--

CREATE TABLE `member_maintenance` (
  `MEMBER_MAINTENANCE_ID` int(3) NOT NULL,
  `MAINTENANCE_ID` int(3) NOT NULL,
  `MEMBER_ID` int(3) NOT NULL,
  `PAY_DATE` date NOT NULL,
  `AMOUNT` int(5) NOT NULL,
  `LATE_CHARGES` int(5) DEFAULT NULL,
  `TOTAL` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `member_maintenance`
--

INSERT INTO `member_maintenance` (`MEMBER_MAINTENANCE_ID`, `MAINTENANCE_ID`, `MEMBER_ID`, `PAY_DATE`, `AMOUNT`, `LATE_CHARGES`, `TOTAL`) VALUES
(1, 1, 1, '2023-08-05', 100, 50, 150),
(2, 1, 2, '2023-07-30', 100, 0, 100),
(3, 2, 3, '2023-08-30', 100, 0, 100),
(4, 2, 6, '2023-08-01', 100, 0, 100),
(5, 2, 5, '2023-09-01', 200, 0, 200),
(6, 2, 5, '2023-09-01', 200, 0, 200);

-- --------------------------------------------------------

--
-- Table structure for table `notice`
--

CREATE TABLE `notice` (
  `NOTICE_ID` int(3) NOT NULL,
  `COMMITTEE_ID` int(3) NOT NULL,
  `DESCRIPTION` varchar(50) NOT NULL,
  `DATE` date NOT NULL,
  `STATUS` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `notice`
--

INSERT INTO `notice` (`NOTICE_ID`, `COMMITTEE_ID`, `DESCRIPTION`, `DATE`, `STATUS`) VALUES
(1, 2, 'society meeting at 9pm', '2020-10-01', 'inactive'),
(2, 4, 'tomorrow electricity powercut between 1pm to 3pm', '2022-05-16', 'inactive'),
(3, 4, 'today society meeting time is changed 9pm to 10pm', '2023-03-22', 'inactive'),
(4, 3, 'meeting for holi celebration', '2024-03-23', 'active'),
(5, 4, 'meeting for renovation', '2024-02-14', 'inactive');

-- --------------------------------------------------------

--
-- Table structure for table `occupant`
--

CREATE TABLE `occupant` (
  `OCCUPANT_ID` int(3) NOT NULL,
  `MEMBER_ID` int(3) NOT NULL,
  `NAME` varchar(20) NOT NULL,
  `GENDER` varchar(6) NOT NULL,
  `RELIGION` varchar(15) DEFAULT NULL,
  `COMMING_DATE` date NOT NULL,
  `RENT_AMOUNT` int(6) DEFAULT NULL,
  `NO._OF_FAMILY_MEMBER` int(2) DEFAULT NULL,
  `PROFILE` varchar(100) DEFAULT NULL,
  `LEAVING_DATE` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `occupant`
--

INSERT INTO `occupant` (`OCCUPANT_ID`, `MEMBER_ID`, `NAME`, `GENDER`, `RELIGION`, `COMMING_DATE`, `RENT_AMOUNT`, `NO._OF_FAMILY_MEMBER`, `PROFILE`, `LEAVING_DATE`) VALUES
(1, 4, 'jigar', 'male', 'hindu', '2021-05-06', 6000, 5, '/pimages/m21.jpg', NULL),
(2, 5, 'harsha', 'female', 'hindu', '2018-01-21', 7000, 3, '/pimages/m16.jpg', NULL),
(3, 9, 'smit', 'male', 'sikh', '2021-07-26', 3000, 1, '/pimages/m9.jpg', NULL),
(4, 10, 'kabir', 'male', 'muslim', '2021-04-14', 4000, 2, '/pimages/m10.jpg', NULL),
(5, 20, 'asha', 'female', 'hindu', '2022-11-13', 6000, 3, '/pimages/m17.jpg', NULL),
(6, 1, 'Rina', 'female', 'hindu', '2024-02-02', 5000, 4, '/pimages/m18.jpg', '2024-04-02'),
(13, 1, 'mohan', 'male', 'hindu', '2024-04-04', 6000, 5, '/pimages/img4_BHiQx52.jpg', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `advertisement`
--
ALTER TABLE `advertisement`
  ADD PRIMARY KEY (`ADVERTISE_ID`),
  ADD KEY `B` (`MEMBER_ID`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`BOOKING_ID`),
  ADD KEY `Z` (`MEMBER_ID`);

--
-- Indexes for table `booking_detail`
--
ALTER TABLE `booking_detail`
  ADD PRIMARY KEY (`BOOKING_DETAIL_ID`),
  ADD KEY `A` (`BOOKING_ID`),
  ADD KEY `J` (`ITEM_ID`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`cart_id`),
  ADD KEY `ci` (`item_id`),
  ADD KEY `cm` (`member_id`);

--
-- Indexes for table `committee`
--
ALTER TABLE `committee`
  ADD PRIMARY KEY (`COMMITTEE_ID`);

--
-- Indexes for table `committee_details`
--
ALTER TABLE `committee_details`
  ADD PRIMARY KEY (`COMMITTEE_DETAIL_ID`),
  ADD KEY `C` (`COMMITTEE_ID`),
  ADD KEY `D` (`MEMBER_ID`);

--
-- Indexes for table `complaint`
--
ALTER TABLE `complaint`
  ADD PRIMARY KEY (`COMPLAINT_ID`),
  ADD KEY `Y` (`MEMBER_ID`),
  ADD KEY `ZW` (`COMMITTEE_DETAIL_ID`);

--
-- Indexes for table `deposit`
--
ALTER TABLE `deposit`
  ADD PRIMARY KEY (`DEPOSIT_ID`),
  ADD KEY `E` (`BANK_NAME`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `expense`
--
ALTER TABLE `expense`
  ADD PRIMARY KEY (`EXPENCE_ID`),
  ADD KEY `OO` (`FUNCTION_ID`);

--
-- Indexes for table `function`
--
ALTER TABLE `function`
  ADD PRIMARY KEY (`FUNCTION_ID`);

--
-- Indexes for table `income`
--
ALTER TABLE `income`
  ADD PRIMARY KEY (`INCOME_ID`),
  ADD KEY `ff` (`DEPOSIT_ID`),
  ADD KEY `bb` (`BOOKING_ID`),
  ADD KEY `SS` (`MEMBER_MAINTENANCE_ID`);

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`ITEM_ID`);

--
-- Indexes for table `maintenance`
--
ALTER TABLE `maintenance`
  ADD PRIMARY KEY (`MAINTENANCE_ID`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`MEMBER_ID`);

--
-- Indexes for table `member_function`
--
ALTER TABLE `member_function`
  ADD PRIMARY KEY (`MEMBER_FUNCTION_ID`),
  ADD KEY `K` (`FUNCTION_ID`),
  ADD KEY `L` (`MEMBER_ID`);

--
-- Indexes for table `member_maintenance`
--
ALTER TABLE `member_maintenance`
  ADD PRIMARY KEY (`MEMBER_MAINTENANCE_ID`),
  ADD KEY `F` (`MAINTENANCE_ID`),
  ADD KEY `G` (`MEMBER_ID`);

--
-- Indexes for table `notice`
--
ALTER TABLE `notice`
  ADD PRIMARY KEY (`NOTICE_ID`),
  ADD KEY `H` (`COMMITTEE_ID`);

--
-- Indexes for table `occupant`
--
ALTER TABLE `occupant`
  ADD PRIMARY KEY (`OCCUPANT_ID`),
  ADD KEY `X` (`MEMBER_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `advertisement`
--
ALTER TABLE `advertisement`
  MODIFY `ADVERTISE_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=141;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `BOOKING_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `booking_detail`
--
ALTER TABLE `booking_detail`
  MODIFY `BOOKING_DETAIL_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `cart_id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `committee`
--
ALTER TABLE `committee`
  MODIFY `COMMITTEE_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `committee_details`
--
ALTER TABLE `committee_details`
  MODIFY `COMMITTEE_DETAIL_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `complaint`
--
ALTER TABLE `complaint`
  MODIFY `COMPLAINT_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `deposit`
--
ALTER TABLE `deposit`
  MODIFY `DEPOSIT_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `expense`
--
ALTER TABLE `expense`
  MODIFY `EXPENCE_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `function`
--
ALTER TABLE `function`
  MODIFY `FUNCTION_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `income`
--
ALTER TABLE `income`
  MODIFY `INCOME_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `ITEM_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `maintenance`
--
ALTER TABLE `maintenance`
  MODIFY `MAINTENANCE_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `member`
--
ALTER TABLE `member`
  MODIFY `MEMBER_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `member_function`
--
ALTER TABLE `member_function`
  MODIFY `MEMBER_FUNCTION_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `member_maintenance`
--
ALTER TABLE `member_maintenance`
  MODIFY `MEMBER_MAINTENANCE_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `notice`
--
ALTER TABLE `notice`
  MODIFY `NOTICE_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `occupant`
--
ALTER TABLE `occupant`
  MODIFY `OCCUPANT_ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `advertisement`
--
ALTER TABLE `advertisement`
  ADD CONSTRAINT `B` FOREIGN KEY (`MEMBER_ID`) REFERENCES `member` (`MEMBER_ID`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `Z` FOREIGN KEY (`MEMBER_ID`) REFERENCES `member` (`MEMBER_ID`);

--
-- Constraints for table `booking_detail`
--
ALTER TABLE `booking_detail`
  ADD CONSTRAINT `A` FOREIGN KEY (`BOOKING_ID`) REFERENCES `booking` (`BOOKING_ID`),
  ADD CONSTRAINT `J` FOREIGN KEY (`ITEM_ID`) REFERENCES `items` (`ITEM_ID`);

--
-- Constraints for table `cart`
--
ALTER TABLE `cart`
  ADD CONSTRAINT `ci` FOREIGN KEY (`item_id`) REFERENCES `items` (`ITEM_ID`),
  ADD CONSTRAINT `cm` FOREIGN KEY (`member_id`) REFERENCES `member` (`MEMBER_ID`);

--
-- Constraints for table `committee_details`
--
ALTER TABLE `committee_details`
  ADD CONSTRAINT `C` FOREIGN KEY (`COMMITTEE_ID`) REFERENCES `committee` (`COMMITTEE_ID`),
  ADD CONSTRAINT `D` FOREIGN KEY (`MEMBER_ID`) REFERENCES `member` (`MEMBER_ID`);

--
-- Constraints for table `complaint`
--
ALTER TABLE `complaint`
  ADD CONSTRAINT `Y` FOREIGN KEY (`MEMBER_ID`) REFERENCES `member` (`MEMBER_ID`),
  ADD CONSTRAINT `ZW` FOREIGN KEY (`COMMITTEE_DETAIL_ID`) REFERENCES `committee_details` (`COMMITTEE_DETAIL_ID`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `expense`
--
ALTER TABLE `expense`
  ADD CONSTRAINT `OO` FOREIGN KEY (`FUNCTION_ID`) REFERENCES `function` (`FUNCTION_ID`);

--
-- Constraints for table `income`
--
ALTER TABLE `income`
  ADD CONSTRAINT `aa` FOREIGN KEY (`MEMBER_MAINTENANCE_ID`) REFERENCES `maintenance` (`MAINTENANCE_ID`),
  ADD CONSTRAINT `bb` FOREIGN KEY (`BOOKING_ID`) REFERENCES `booking` (`BOOKING_ID`),
  ADD CONSTRAINT `di` FOREIGN KEY (`DEPOSIT_ID`) REFERENCES `deposit` (`DEPOSIT_ID`),
  ADD CONSTRAINT `ss` FOREIGN KEY (`MEMBER_MAINTENANCE_ID`) REFERENCES `member_maintenance` (`MEMBER_MAINTENANCE_ID`);

--
-- Constraints for table `member_function`
--
ALTER TABLE `member_function`
  ADD CONSTRAINT `K` FOREIGN KEY (`FUNCTION_ID`) REFERENCES `function` (`FUNCTION_ID`),
  ADD CONSTRAINT `L` FOREIGN KEY (`MEMBER_ID`) REFERENCES `member` (`MEMBER_ID`);

--
-- Constraints for table `member_maintenance`
--
ALTER TABLE `member_maintenance`
  ADD CONSTRAINT `F` FOREIGN KEY (`MAINTENANCE_ID`) REFERENCES `maintenance` (`MAINTENANCE_ID`),
  ADD CONSTRAINT `G` FOREIGN KEY (`MEMBER_ID`) REFERENCES `member` (`MEMBER_ID`);

--
-- Constraints for table `notice`
--
ALTER TABLE `notice`
  ADD CONSTRAINT `H` FOREIGN KEY (`COMMITTEE_ID`) REFERENCES `committee` (`COMMITTEE_ID`);

--
-- Constraints for table `occupant`
--
ALTER TABLE `occupant`
  ADD CONSTRAINT `X` FOREIGN KEY (`MEMBER_ID`) REFERENCES `member` (`MEMBER_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
