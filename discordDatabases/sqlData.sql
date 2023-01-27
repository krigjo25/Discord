
/* Welcome and leave messages*/
INSERT INTO welcome (welcome) VALUES
('noOne : . {member.mention} : appeared.'),
('{member.mention} brought us a :nut: '),
('pyButt just sent the server a gift. {member.mention}'),
('we are pleased to meat you, {member.mention}.'),
('{self.bot.user} Threw a pokemon ball, {member.mention} appeard'),
('');

INSERT INTO abcent (abcent) VALUES
('vanished'),
('we wish the best for you, {member.mention}'),
('{member.mention} just used a nut and disapeared into the jungle :nuts:'),
('{member.mention}, used a time machine back to 1800s'),
('I hope you find happyness anywhere else, {member.mention}.'),
(' ');




INSERT INTO waltdisney ( characters, roles, animationname) VALUES
('Aladdin', 'Hero', 'Aladdin'),
('Clayton', 'Villian', 'Tarzan'),
('Simba', 'Hero', ' The Lion King'),
('Robin Hood', ' Hero', 'Robin Hood'),
('Pinhoccio', 'Hero', 'Pinocchio'),
('Tarzan', ' Hero', 'Tarzan'),
('Quasimodo', 'Hero', 'The Hunchback Of Notredame'),
('Hercules', ' Hero', 'Hercules'),
('The Beast', 'Hero', ' The Beauti And the Beast'),
('Jasmine', 'Princess','Aladdin'),
('Mulan', 'Princess', 'Mulan'),
('Ariel', 'Princess', ' The Little Marmaid'),
('Aurora', 'Princess', 'Sleeping Beauti'),
('Belle', 'Princess', 'Beauti And The Beast'),
('Cinderella', 'Princess', ' Cinderella'),
('Merida', 'Princess', 'Brave'),
('Moana', 'Princess', ' Moana'),
('Snow White', 'Princess', 'Snow White And the Seven Dwarfs'),
('Tiana', 'Princess', 'The Princess And The Frog'),
('Rapunzel', 'Princess', 'Rapunzel'),
('Govenor John Ratcliff', 'Villain', 'Pocahontas'),
('Maleficent', 'Villian', 'Sleeping Beauti'),
('The Wicked Queen', 'Villian', 'Snow White and the Seven Dwarfs'),
('Lady Tremaine', 'Villian', 'Cinderella'),
('Jafar', 'Villian', 'Aladdin'),
('Scar', 'Villian', 'The Lion King'),
('Ursurella', 'Villian', 'The little Marmaid'),
('Dr.Farciller', 'Villian', 'The Princess And The Frog'),
('Judge Claude Frollo', 'Villian', 'The Hunchback Of Notredame'),
('Mother Gothel', ' Villian', 'Rapunzel'),
('Shan Yu', 'Villian', 'Mulan'),
("Mor'du", 'Villian', ' Brave'),
('Hades', 'Villian', 'Hercules'),
('Gideon', 'Villian', 'Pinocchio'),
('Gaston', ' Villian', 'The Beauti And The Beast');

DELIMITER ;
INSERT INTO `waltDisneyTitles` (`title`) VALUES
('Aladdin'),
('Brave'),
('Cinderella'),
('Hercules'),
('Moana'),
('Mulan'),
('Pinocchio'),
('Pocahontas'),
('Rapunzel'),
('Robin Hood'),
('Sleeping Beauti'),
('Snow White And The Seven Dwarfs'),
('Tarzan'),
('The Beauti And The Beast'),
('The Hunchback Of Notredame'),
('The Lion King'),
('The Little Marmaid'),
('The Princsess And The Frog');


INSERT INTO `categories` (`categories`) VALUES
("random");

INSERT INTO `categories` (`categories`, `sub`, `sub1`, `sub2`) VALUES
("waltdisney", "Heros", "Princess", "Classics");

