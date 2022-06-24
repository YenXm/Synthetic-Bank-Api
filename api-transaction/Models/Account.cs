namespace api_transaction.Models
{
    public class Account : BaseModel
    {
        public int PersonId { get; set; }
        public string Provider { get; set; }
        public string CardNumber { get; set; }
        public string CardType { get; set; }
        public int? CreditCap { get; set; }
        public int StartingBalance { get; set; }
        public int CurrentBalance { get; set; }

        public virtual ICollection<Transaction> Transactions { get; set; }
    }
}




