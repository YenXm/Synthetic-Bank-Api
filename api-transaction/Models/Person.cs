namespace api_transaction.Models
{
    public class Person: BaseModel
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Email { get; set; }
        public string Phone { get; set; }
        public string BirthDate { get; set; }
        public string Address { get; set; }
        public string City { get; set; }
        public string State { get; set; }
        public string Zip { get; set; }
        public string Country { get; set; }
        public string Company { get; set; }
        public string JobTitle { get; set; }
        public string CompanyDescription { get; set; }
        public string CompanyDomain { get; set; }


        public virtual ICollection<Account> Accounts { get; set; }
    }
}
