using api_transaction.Models;
using api_transaction.Services;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace api_transaction.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class DataGeneratorController : ControllerBase
    {
        private readonly BankDatabaseContext _context;

        public DataGeneratorController(BankDatabaseContext context)
        {
            _context = context;
        }

        [HttpGet("GetNextId")]
        public async Task<IActionResult> GetNextId()
        {
            var accountId = _context.Accounts.OrderByDescending(x => x.Id).FirstOrDefault().Id;
            var personId = _context.Persons.OrderByDescending(x => x.Id).FirstOrDefault().Id;
            var transactionId = _context.Transactions.OrderByDescending(x => x.Id).FirstOrDefault().Id;
            return new JsonResult(new { transactionId, accountId, personId });

        }

        [HttpPost("ImportJsonData")]
        public async void PostGeneratedData([FromBody] Person[] json)
        {
            _context.Persons.AddRange(json);
            _context.SaveChanges();
            return;
        }
    }
}
