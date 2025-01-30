-- Create a group
INSERT INTO `groups` (title, start_date, end_date) VALUES ('G7', 'Oct 2022', 'Sep 2023')

-- Get new group ID
SELECT id FROM `groups` WHERE title = 'G7' AND start_date = 'Oct 2022' AND end_date = 'Sep 2023' -- Received ID - 2509

-- Create a student and assign him to a group wit ID - 2509
INSERT INTO students (name, second_name, group_id) VALUES ('Joe', 'Satriani', 2509); -- 3945
-- Or we can use nested query
INSERT INTO students (name, second_name, group_id)
VALUES ('Steve', 'Vai',
        (SELECT id FROM `groups`
         WHERE title = 'G7'
           AND start_date = 'Oct 2022'
           AND end_date = 'Sep 2023'));

-- We create two books and indicate that the created student took them
INSERT INTO books (title, taken_by_student_id) ;
VALUES ('Music for adults',
        (SELECT id FROM students
         WHERE name = 'Joe' AND second_name = 'Satriani'));

INSERT INTO books (title, taken_by_student_id) VALUES ('Music for no one', 3945);

-- We create new subjects
INSERT INTO subjets (title) VALUES ('Solfeggio'); -- 3835
INSERT INTO subjets (title) VALUES ('Playing guitar'); -- 3836
INSERT INTO subjets (title) VALUES ('Playing drums'); -- 3837

-- We create two lessons for each subject
INSERT INTO lessons (title, subject_id) VALUES ('Solfeggio Basics', 3835); -- 7443
INSERT INTO lessons (title, subject_id) VALUES ('Solfeggio in Details', 3835); -- 7444
INSERT INTO lessons (title, subject_id) VALUES ('Guitar Basics', 3836); -- 7445
INSERT INTO lessons (title, subject_id) VALUES ('Guitar in Details', 3836); -- 7446
INSERT INTO lessons (title, subject_id) VALUES ('Drums Basics', 3837); -- 7447
INSERT INTO lessons (title, subject_id) VALUES ('Drums in Details', 3837); -- 7442

-- We put marks for the student for all created lessons
INSERT INTO marks (value, lesson_id, student_id) VALUES ('A', 7442, 3945);
INSERT INTO marks (value, lesson_id, student_id) VALUES ('B', 7443, 3945);
INSERT INTO marks (value, lesson_id, student_id) VALUES ('C', 7444, 3945);
INSERT INTO marks (value, lesson_id, student_id) VALUES ('D', 7445, 3945);
INSERT INTO marks (value, lesson_id, student_id) VALUES ('F', 7446, 3945);
INSERT INTO marks (value, lesson_id, student_id) VALUES ('G', 7447, 3945);

-- We receive all the student's grades
SELECT value, name, second_name
FROM marks
JOIN students on marks.student_id = students.id
WHERE student_id = (SELECT id FROM students
					WHERE name = 'Joe' AND second_name = 'Satriani');

-- We receive all the student's books
SELECT title, name, second_name
FROM books
JOIN students on books.taken_by_student_id = students.id
WHERE taken_by_student_id = (SELECT id FROM students
							 WHERE name = 'Joe' AND second_name = 'Satriani');

-- We receive all information about the student
SELECT
	s.name,
	s.second_name,
	g.title as group_title,
	b.title as book_title,
	m.value as mark,
	sub.title as subject_title,
	l.title as lesson_title
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets sub ON l.subject_id = sub.id
WHERE s.id = (SELECT id FROM students WHERE name = 'Joe' AND second_name = 'Satriani')
