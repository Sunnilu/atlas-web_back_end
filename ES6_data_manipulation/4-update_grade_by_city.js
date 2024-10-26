// 4-update_grade_by_city.js
export default function updateStudentGradeByCity(students, city, newGrade) {
  // Filter students by the specified city
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      // Find the grade for the current student
      const gradObj = newGrade.find(() => (grade) => grade.studentId === student.id);
      return {
        id: student.id,
        firstName: student.firstName,
        location: student.location,
        grade: gradObj ? gradObj.grade : 'N/A',
      };
    });
}