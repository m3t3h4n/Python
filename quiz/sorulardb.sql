-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1:3308
-- Üretim Zamanı: 19 Ara 2019, 06:29:19
-- Sunucu sürümü: 8.0.18
-- PHP Sürümü: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `sorulardb`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `sorular`
--

DROP TABLE IF EXISTS `sorular`;
CREATE TABLE IF NOT EXISTS `sorular` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `soru` varchar(1000) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `a` varchar(500) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `b` varchar(500) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `c` varchar(500) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `d` varchar(500) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `dogruCevap` varchar(1) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `sorular`
--

INSERT INTO `sorular` (`id`, `soru`, `a`, `b`, `c`, `d`, `dogruCevap`) VALUES
(1, 'Türkiyenin Başkenti?', 'İstanbul', 'Ankara', 'Antalya', 'Konya', 'b'),
(2, 'Dünya dönüyorsa neden zıpladığımız zaman aynı yere düşüyoruz?', '-_-', 'Ölçmedim ki ahmnaue', 'Yerçekimi Yüzünden', 'Dünaynın etrafındaki manyetik alan yüzünden', 'b'),
(3, 'Eğer japon yapıştırıcısı bir yapıştırıcıysa, neden içinde bulunduğu tüpün içini yapıştırmıyor?', 'Çok fazla yapıştırıcı bir arada olduğu için', 'Tüpün yapıldığı madde yüzünden', 'Hava ile temas edince yapıştırma özelliği kazanmasından dolayı', 'Ölçmedim ki ahmnaue', 'c'),
(23, 'Dünyanın en uzun romanı hangisidir?', 'Medeleine de Scudery - Artamene', 'Tolstoy - Diriliş', 'Oscar Wilde - Dorian Gayin Portresi', 'Miquel De Cervantes - Don Kişot', 'a'),
(7, 'Yüz ölçümü en büyük şehirimiz hangisidir?', 'İstanbul', 'Adana', 'Ankara', 'Konya', 'd'),
(8, 'Türkiyeye sınırına en uzun komşu ülke hangisidir?', 'Suriye', 'İran', 'Irak', 'Yunanistan', 'a'),
(24, 'Filmerin çekiminde kullanılan perde neden yeşildir?', 'Öyelsine', 'Yeşilin en düşük ton olması ve ışığı en iyi şekilde emdiği için', 'Canları öyle istediği için', 'Daha havalı gözüktüğü için', 'b'),
(22, 'Mozart neden Türk Marşını besteledi?', 'Türkleri sevdiği için', 'Birden ilham geldiği için', 'Piyano çalmayı sevdiği için', 'Mehter marşından esinlendiği için', 'd'),
(21, 'Dünyanın ilk romanı hangisdir?', 'Suç ve Ceza', 'İnsan ne ile yaşar', 'Genjinin hikayesi', 'Dönüşüm', 'c'),
(20, 'Birisi bir yere geldiğinde, o kişiye Geldin mi? diye soruluyorsa, o kişi oraya gelmiş midir?', 'Gelmiştir', 'Hem gelmiştir hemde gelmemiştir', 'Gelmemiştir', 'Yukarıdakilerin hepsi', 'a'),
(19, 'Aşağıdakilerden hangisi kırılır?', 'Kalbim', 'Bez', 'Pamuk', 'Kitap', 'a'),
(25, 'Tohumlar hangi yöne  göre büyüyeceklerini nasıl birlirler?', 'Rabbim öyle yaratmış', 'Çok zeki oldukları için', 'Yerçekimsel alanın yönünü hissettikleri için', 'Canları öyle istediği için', 'c');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
