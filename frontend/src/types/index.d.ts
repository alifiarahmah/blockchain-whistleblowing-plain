export interface Report {
  index: number;
  suspect_name: string;
  dept: string;
  action_category: string;
  description: string;
  location: string;
  time_of_occurence: string;
  evidence: string[];
}
