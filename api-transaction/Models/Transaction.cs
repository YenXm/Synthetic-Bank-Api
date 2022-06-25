namespace api_transaction.Models
{
    public class Transaction
    {
        public int Id { get; set; }
        public int AccountId { get; set; }
        public decimal Amount { get; set; }
        public DateTime Date { get; set; }
        public string Description { get; set; }
        public string Category { get; set; }
        public string Tags { get; set; }
        public string Notes { get; set; }
        public bool IsReconciled { get; set; }
        public bool IsCleared { get; set; }


    }
}