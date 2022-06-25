namespace api_transaction.Models
{
    public class Transaction : BaseModel
    {
        public string Date { get; set; }
        public string Description { get; set; }
        public string Category { get; set; }
        public int Amount { get; set; }
        public int AccountId { get; set; }
        public string Tags { get; set; }
        public string Notes { get; set; }
        public bool IsReconciled { get; set; }
        public bool IsCleared { get; set; }


    }
}


