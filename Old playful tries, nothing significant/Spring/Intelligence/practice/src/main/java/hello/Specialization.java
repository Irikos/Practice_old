package hello;

/**
 * Created by Andrei on 01-Nov-16.
 */
public class Specialization {
    private String name;
    private String universityName;
    private String facultyName;
    private String description;
    private String domain;
    private String programDomain;
    private String specialization;
    private Type type;
    private boolean canApply;
    private String admissionCode;
    private int studyDuration;
    private String wordpress;
    private Language language;
    private String courses;
    private String admissions;
    private int specialStatus; // bool ?
    private String completionRate;

    private enum Type {
        License, Master
    }
    private enum Language {
        RO, EN
    }
    private enum studyForm {
        IF, ID
    }
    private long id;

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUniversityName() {
        return universityName;
    }

    public void setUniversityName(String universityName) {
        this.universityName = universityName;
    }

    public String getFacultyName() {
        return facultyName;
    }

    public void setFacultyName(String facultyName) {
        this.facultyName = facultyName;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }

    public String getProgramDomain() {
        return programDomain;
    }

    public void setProgramDomain(String programDomain) {
        this.programDomain = programDomain;
    }

    public String getSpecialization() {
        return specialization;
    }

    public void setSpecialization(String specialization) {
        this.specialization = specialization;
    }

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

    public boolean isCanApply() {
        return canApply;
    }

    public void setCanApply(boolean canApply) {
        this.canApply = canApply;
    }

    public String getAdmissionCode() {
        return admissionCode;
    }

    public void setAdmissionCode(String admissionCode) {
        this.admissionCode = admissionCode;
    }

    public int getStudyDuration() {
        return studyDuration;
    }

    public void setStudyDuration(int studyDuration) {
        this.studyDuration = studyDuration;
    }

    public String getWordpress() {
        return wordpress;
    }

    public void setWordpress(String wordpress) {
        this.wordpress = wordpress;
    }

    public Language getLanguage() {
        return language;
    }

    public void setLanguage(Language language) {
        this.language = language;
    }

    public String getCourses() {
        return courses;
    }

    public void setCourses(String courses) {
        this.courses = courses;
    }

    public String getAdmissions() {
        return admissions;
    }

    public void setAdmissions(String admissions) {
        this.admissions = admissions;
    }

    public int getSpecialStatus() {
        return specialStatus;
    }

    public void setSpecialStatus(int specialStatus) {
        this.specialStatus = specialStatus;
    }

    public String getCompletionRate() {
        return completionRate;
    }

    public void setCompletionRate(String complessionRate) {
        this.completionRate = complessionRate;
    }

}
