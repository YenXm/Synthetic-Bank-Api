namespace api_transaction.Models
{
    public class Account : BaseModel
    {
        public int PersonId { get; set; }
        public string Provider { get; set; }
        public string CardNumber { get; set; }
        public string AccountType { get; set; }
        public int StartingBalance { get; set; }
        public int Balance { get; set; }

        public virtual ICollection<Transaction> Transactions { get; set; }
    }
}




