CREATE TABLE student_names (
    id INT PRIMARY KEY AUTOINCREMENT,
    name TEXT,
);

CREATE TABLE quiz_number  (
    id INT PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    quiz_questions INT,
    date DATE,
);

CREATE TABLE student_quiz_score(
    id INT PRIMARY KEY AUTOINCREMENT,
    student TEXT,
    FOREIGN KEY(student) REFERENCES students(first_name, last_name),
    score INT,
);