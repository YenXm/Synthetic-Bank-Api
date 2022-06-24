namespace api_transaction.Models
{
    public class Person: BaseModel
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Phone { get; set; }
        public string Email { get; set; }


        public virtual ICollection<Account> Accounts { get; set; }
    }
}
