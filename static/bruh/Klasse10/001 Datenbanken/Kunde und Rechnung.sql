-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Erstellungszeit: 22. Apr 2016 um 11:06
-- Server Version: 5.5.47-0ubuntu0.14.04.1
-- PHP-Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Datenbank: `9A-lehrer`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Kunde`
--

CREATE TABLE IF NOT EXISTS `KundeConstraint` (
  `KNr` int(10) NOT NULL DEFAULT '0',
  `Vorname` varchar(100) COLLATE latin1_general_ci DEFAULT NULL,
  `Nachname` varchar(100) COLLATE latin1_general_ci DEFAULT NULL,
  `Wohnort` varchar(100) COLLATE latin1_general_ci DEFAULT NULL,
  PRIMARY KEY (`KNr`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Daten für Tabelle `Kunde`
--

INSERT INTO `KundeConstraint` (`KNr`, `Vorname`, `Nachname`, `Wohnort`) VALUES
(1, 'Franz', 'Meier', 'Bad Tölz'),
(2, 'Bettina', 'Schulz', 'München'),
(3, 'Oliver', 'Schmidt', 'Regensburg');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Rechnung`
--

CREATE TABLE IF NOT EXISTS `RechnungConstraint` (
  `RNr` int(10) NOT NULL DEFAULT '0',
  `Kunden` int(10) DEFAULT NULL,
  `Artikel` varchar(100) COLLATE latin1_general_ci DEFAULT NULL,
  `Preis` decimal(10,2) DEFAULT NULL,
  `Datum` date DEFAULT NULL,
  PRIMARY KEY (`RNr`),
  KEY `Kunden` (`Kunden`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Daten für Tabelle `Rechnung`
--

INSERT INTO `RechnungConstraint` (`RNr`, `Kunden`, `Artikel`, `Preis`, `Datum`) VALUES
(1, 1, 'Bleistift', 0.99, '2016-04-01'),
(2, 2, 'Jeans', 29.99, '2016-03-24'),
(3, 3, 'Laptop', 450.00, '2016-03-24'),
(4, 1, 'Armbanduhr', 39.99, '2016-03-24'),
(5, 1, 'Block', 2.99, '2016-03-24');

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `Rechnung`
--
ALTER TABLE `RechnungConstraint`
  ADD CONSTRAINT `Rechnung_ibfk_1` FOREIGN KEY (`Kunden`) REFERENCES `KundeConstraint` (`KNr`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
