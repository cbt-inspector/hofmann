-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Erstellungszeit: 27. Apr 2016 um 09:43
-- Server Version: 5.5.47-0ubuntu0.14.04.1
-- PHP-Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Datenbank: `test`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `DeutscheBiere`
--

CREATE TABLE IF NOT EXISTS `DeutscheBiere` (
  `BierNr` varchar(10) COLLATE latin1_general_ci NOT NULL DEFAULT '',
  `Name` varchar(100) COLLATE latin1_general_ci DEFAULT NULL,
  `Stadt` varchar(100) COLLATE latin1_general_ci DEFAULT NULL,
  `Bundesland` varchar(100) COLLATE latin1_general_ci DEFAULT NULL,
  `Gründungsjahr` int(4) DEFAULT NULL,
  `Biersorte` varchar(100) COLLATE latin1_general_ci DEFAULT NULL,
  `Hefetyp` varchar(100) COLLATE latin1_general_ci DEFAULT NULL,
  `Alkoholgehalt` decimal(2,1) DEFAULT NULL,
  PRIMARY KEY (`BierNr`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Daten für Tabelle `DeutscheBiere`
--

INSERT INTO `DeutscheBiere` (`BierNr`, `Name`, `Stadt`, `Bundesland`, `Gründungsjahr`, `Biersorte`, `Hefetyp`, `Alkoholgehalt`) VALUES
('B01', 'Augustiner', 'München', 'Bayern', 1328, 'Helles', 'untergärig', 5.2),
('B02', 'Augustiner', 'München', 'Bayern', 1328, 'Export', 'untergärig', 5.6),
('B03', 'Beck''s', 'Bremen', 'Bremen', 1873, 'Pils', 'untergärig', 4.9),
('B04', 'Paulaner', 'München', 'Bayern', 1634, 'Weizen', 'obergärig', 5.5),
('B05', 'Paulaner', 'München', 'Bayern', 1634, 'Helles', 'untergärig', 4.9),
('B06', 'Krombacher', 'Krombach', 'Nordrhein-Westfalen', 1803, 'Pils', 'untergärig', 4.8),
('B07', 'Früh', 'Köln', 'Nordrhein-Westfalen', 1904, 'Kölsch', 'obergärig', 4.8),
('B08', 'Gaffel', 'Köln', 'Nordrhein-Westfalen', 1908, 'Kölsch', 'obergärig', 4.8),
('B09', 'Hoepfner', 'Karlsruhe', 'Baden-Württemberg', 1798, 'Pils', 'untergärig', 4.7),
('B10', 'Spaten', 'München', 'Bayern', 1397, 'Helles', 'untergärig', 5.2),
('B11', NULL, NULL, NULL, NULL, 'Lager', 'untergärig', NULL),
('B12', NULL, NULL, NULL, NULL, 'Starkbier', 'ober- und untergärig', NULL),
('B13', NULL, NULL, NULL, NULL, 'Altbier', 'obergärig', NULL);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
