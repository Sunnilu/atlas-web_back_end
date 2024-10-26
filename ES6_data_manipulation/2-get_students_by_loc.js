// 2-get_students_by_loc.js
export default function getStudentsByLocation(students, city) {
  if (!Array.isArray(students) || typeof city !== 'string') {
    return [];
  }
  return students.filter((student) => student.location === city);
}
