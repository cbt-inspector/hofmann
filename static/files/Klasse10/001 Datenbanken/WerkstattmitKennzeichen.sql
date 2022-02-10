-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Erstellungszeit: 04. Mrz 2020 um 10:42
-- Server-Version: 5.7.27-0ubuntu0.16.04.1
-- PHP-Version: 7.0.33-0ubuntu0.16.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `test`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Werkstatt`
--

CREATE TABLE `Werkstatt2` (
  `Kennzeichen` varchar(255) PRIMARY KEY,
  `Hersteller` varchar(255) DEFAULT NULL,
  `Farbe` varchar(255) DEFAULT NULL,
  `Vorname` varchar(255) DEFAULT NULL,
  `Nachname` varchar(255) NOT NULL,
  `Kilometerstand` int(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `Werkstatt`
--

INSERT INTO `Werkstatt2` (`Kennzeichen`, `Hersteller`, `Farbe`, `Vorname`, `Nachname`, `Kilometerstand`) VALUES
('EVB-G-01', 'VW', 'schwarz', 'Peter', 'Schmidt', 125325),
('EVB-G-02', 'Audi', 'rot', 'Fritz', 'Schneider', 412),
('EVB-G-03', 'BMW', 'silber', 'Max', 'Maier', 57723),
('EVB-G-04', 'Porsche', 'blau', 'Sabine', 'Schneider', 7832),
('EVB-G-05', 'BMW', 'schwarz', 'Susanne', 'Maier', 85492),
('EVB-G-06', 'VW', 'weiß', 'Peter', 'Schmidt', 26497),
('EVB-G-07', 'Porsche', 'schwarz', 'Max', 'Maier', 35074),
('EVB-G-08', 'BMW', 'schwarz', 'Siemens', 'Siemens', 63842),
('EVB-G-09', 'BMW', 'schwarz', 'Siemens', 'Siemens', 61374),
('EVB-G-10', 'BMW', 'schwarz', 'Siemens', 'Siemens', 63842);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
