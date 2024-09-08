import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';

const BASE_URL = 'http://localhost:8000'; // Replace with your backend URL

enum StatusEnum {
  Pending = 'pending',
  Accepted = 'accepted',
  Rejected = 'rejected',
}

enum WorkingFormEnum {
  PartTime = 'part-time',
  FullTime = 'full-time',
  Contract = 'contract',
}

class APIClient {
  private instance: AxiosInstance;

  constructor(baseURL: string, config?: AxiosRequestConfig) {
    this.instance = axios.create({
      baseURL,
      ...config,
    });
  }

  // Set the authorization token for subsequent requests
  setAuthToken(token: string) {
    this.instance.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  }

  // Applications
  async getApplications() {
    const response = await this.instance.get('/api/applications/');
    return response.data;
  }

  async createApplication(data: any) {
    const response = await this.instance.post('/api/applications/', data);
    return response.data;
  }

  async getApplication(id: string) {
    const response = await this.instance.get(`/api/applications/${id}/`);
    return response.data;
  }

  async updateApplication(id: string, data: any) {
    const response = await this.instance.put(`/api/applications/${id}/`, data);
    return response.data;
  }

  async partialUpdateApplication(id: string, data: any) {
    const response = await this.instance.patch(`/api/applications/${id}/`, data);
    return response.data;
  }

  async deleteApplication(id: string) {
    const response = await this.instance.delete(`/api/applications/${id}/`);
    return response.data;
  }

  // Companies
  async getCompanies() {
    const response = await this.instance.get('/api/companies/');
    return response.data;
  }

  async createCompany(data: any) {
    const response = await this.instance.post('/api/companies/', data);
    return response.data;
  }

  async getCompany(id: number) {
    const response = await this.instance.get(`/api/companies/${id}/`);
    return response.data;
  }

  async updateCompany(id: number, data: any) {
    const response = await this.instance.put(`/api/companies/${id}/`, data);
    return response.data;
  }

  async partialUpdateCompany(id: number, data: any) {
    const response = await this.instance.patch(`/api/companies/${id}/`, data);
    return response.data;
  }

  async deleteCompany(id: number) {
    const response = await this.instance.delete(`/api/companies/${id}/`);
    return response.data;
  }

  async getCompanyMembers(companyId: number) {
    const response = await this.instance.get(`/api/companies/${companyId}/members/`);
    return response.data;
  }

  async addUserToCompany(id: string, data: any) {
    const response = await this.instance.put(`/api/companies/add/${id}/`, data);
    return response.data;
  }

  async partialUpdateUserInCompany(id: string, data: any) {
    const response = await this.instance.patch(`/api/companies/add/${id}/`, data);
    return response.data;
  }

  async promoteUserInCompany(id: string, data: any) {
    const response = await this.instance.put(`/api/companies/promote/${id}/`, data);
    return response.data;
  }

  async partialPromoteUserInCompany(id: string, data: any) {
    const response = await this.instance.patch(`/api/companies/promote/${id}/`, data);
    return response.data;
  }

  async removeUserFromCompany(id: string, data: any) {
    const response = await this.instance.put(`/api/companies/remove/${id}/`, data);
    return response.data;
  }

  async partialRemoveUserFromCompany(id: string, data: any) {
    const response = await this.instance.patch(`/api/companies/remove/${id}/`, data);
    return response.data;
  }

  // Job Categories
  async getJobCategories() {
    const response = await this.instance.get('/api/job_categories/');
    return response.data;
  }

  async createJobCategory(data: any) {
    const response = await this.instance.post('/api/job_categories/', data);
    return response.data;
  }

  async getJobCategory(id: number) {
    const response = await this.instance.get(`/api/job_categories/${id}/`);
    return response.data;
  }

  async updateJobCategory(id: number, data: any) {
    const response = await this.instance.put(`/api/job_categories/${id}/`, data);
    return response.data;
  }

  async partialUpdateJobCategory(id: number, data: any) {
    const response = await this.instance.patch(`/api/job_categories/${id}/`, data);
    return response.data;
  }

  async deleteJobCategory(id: number) {
    const response = await this.instance.delete(`/api/job_categories/${id}/`);
    return response.data;
  }

  // Jobs
  async getJobs() {
    const response = await this.instance.get('/api/jobs/');
    return response.data;
  }

  async createJob(data: any) {
    const response = await this.instance.post('/api/jobs/', data);
    return response.data;
  }

  async getJob(id: number) {
    const response = await this.instance.get(`/api/jobs/${id}/`);
    return response.data;
  }

  async updateJob(id: number, data: any) {
    const response = await this.instance.put(`/api/jobs/${id}/`, data);
    return response.data;
  }

  async partialUpdateJob(id: number, data: any) {
    const response = await this.instance.patch(`/api/jobs/${id}/`, data);
    return response.data;
  }

  async deleteJob(id: number) {
    const response = await this.instance.delete(`/api/jobs/${id}/`);
    return response.data;
  }

  async getJobApplications(jobId: number) {
    const response = await this.instance.get(`/api/jobs/${jobId}/applications/`);
    return response.data;
  }

  async getJobApplication(jobId: number, applicationId: string) {
    const response = await this.instance.get(`/api/jobs/${jobId}/applications/${applicationId}/`);
    return response.data;
  }

  async updateJobApplicationStatus(jobId: number, applicationId: string, data: any) {
    const response = await this.instance.put(`/api/jobs/${jobId}/applications/${applicationId}/update/`, data);
    return response.data;
  }

  async partialUpdateJobApplicationStatus(jobId: number, applicationId: string, data: any) {
    const response = await this.instance.patch(`/api/jobs/${jobId}/applications/${applicationId}/update/`, data);
    return response.data;
  }

  // Resumes
  async getResumes() {
    const response = await this.instance.get('/api/resumes/');
    return response.data;
  }

  async createResume(data: any) {
    const response = await this.instance.post('/api/resumes/', data);
    return response.data;
  }

  async getResume(id: string) {
    const response = await this.instance.get(`/api/resumes/${id}/`);
    return response.data;
  }

  async updateResume(id: string, data: any) {
    const response = await this.instance.put(`/api/resumes/${id}/`, data);
    return response.data;
  }

  async partialUpdateResume(id: string, data: any) {
    const response = await this.instance.patch(`/api/resumes/${id}/`, data);
    return response.data;
  }

  async deleteResume(id: string) {
    const response = await this.instance.delete(`/api/resumes/${id}/`);
    return response.data;
  }

  // Skills
  async getSkills() {
    const response = await this.instance.get('/api/skills/');
    return response.data;
  }

  async createSkill(data: any) {
    const response = await this.instance.post('/api/skills/', data);
    return response.data;
  }

  async getSkill(id: number) {
    const response = await this.instance.get(`/api/skills/${id}/`);
    return response.data;
  }

  async updateSkill(id: number, data: any) {
    const response = await this.instance.put(`/api/skills/${id}/`, data);
    return response.data;
  }

  async partialUpdateSkill(id: number, data: any) {
    const response = await this.instance.patch(`/api/skills/${id}/`, data);
    return response.data;
  }

  async deleteSkill(id: number) {
    const response = await this.instance.delete(`/api/skills/${id}/`);
    return response.data;
  }

  // Authentication
  async register(data: any) {
    const response = await this.instance.post('/api/register/', data);
    return response.data;
  }

  async login(data: any) {
    const response = await this.instance.post('/api/token/', data);
    return response.data;
  }

  async refreshToken(refreshToken: string) {
    const response = await this.instance.post('/api/token/refresh/', { refresh: refreshToken });
    return response.data;
  }

  // Users
  async getUser(id: string) {
    const response = await this.instance.get(`/api/users/${id}/`);
    return response.data;
  }

  async updateUser(id: string, data: any) {
    const response = await this.instance.put(`/api/users/${id}/`, data);
    return response.data;
  }

  async partialUpdateUser(id: string, data: any) {
    const response = await this.instance.patch(`/api/users/${id}/`, data);
    return response.data;
  }

  async deleteUser(id: string) {
    const response = await this.instance.delete(`/api/users/${id}/`);
    return response.data;
  }
}

export default new APIClient(BASE_URL);