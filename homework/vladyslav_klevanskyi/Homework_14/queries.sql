-- 1. Create a student
INSERT INTO students (name, second_name, group_id) VALUES ('Joe', 'Satriani', NULL); -- ID = 3945

-- 2. We create two books and indicate that the created student took them
INSERT INTO books (title, taken_by_student_id) VALUES ('Music for adults', 3945);
INSERT INTO books (title, taken_by_student_id) VALUES ('Music for no one', 3945);

-- 3. We create a group and assign our student to it.
INSERT INTO `groups` (title, start_date, end_date) VALUES ('G7', 'Oct 2022', 'Sep 2023'); -- ID = 2509
UPDATE students SET group_id = 2509 WHERE id = 3945

-- 4. We create new subjects
INSERT INTO subjets (title) VALUES ('Solfeggio'); -- ID = 3835
INSERT INTO subjets (title) VALUES ('Playing guitar'); -- ID = 3836
INSERT INTO subjets (title) VALUES ('Playing drums'); -- ID = 3837

-- 5. We create two lessons for each subject
INSERT INTO lessons (title, subject_id) VALUES ('Solfeggio Basics', 3835); -- ID = 7443
INSERT INTO lessons (title, subject_id) VALUES ('Solfeggio in Details', 3835); -- ID = 7444
INSERT INTO lessons (title, subject_id) VALUES ('Guitar Basics', 3836); -- ID = 7445
INSERT INTO lessons (title, subject_id) VALUES ('Guitar in Details', 3836); -- ID = 7446
INSERT INTO lessons (title, subject_id) VALUES ('Drums Basics', 3837); -- ID = 7447
INSERT INTO lessons (title, subject_id) VALUES ('Drums in Details', 3837); -- ID = 7442

-- 6. We put marks for the student for all created lessons
INSERT INTO marks (value, lesson_id, student_id) VALUES ('A', 7442, 3945);
INSERT INTO marks (value, lesson_id, student_id) VALUES ('B', 7443, 3945);
INSERT INTO marks (value, lesson_id, student_id) VALUES ('C', 7444, 3945);
INSERT INTO marks (value, lesson_id, student_id) VALUES ('D', 7445, 3945);
INSERT INTO marks (value, lesson_id, student_id) VALUES ('F', 7446, 3945);
INSERT INTO marks (value, lesson_id, student_id) VALUES ('G', 7447, 3945);

-----------------------------------------------------------------------

-- 1. We receive all the student's grades
SELECT value, name, second_name
FROM marks
JOIN students on marks.student_id = students.id
WHERE student_id = 3945;

-- 2. We receive all the student's books
SELECT title, name, second_name
FROM books
JOIN students on books.taken_by_student_id = students.id
WHERE taken_by_student_id = 3945;

-- 3. We receive all information about the student
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
WHERE s.id = 3945;
