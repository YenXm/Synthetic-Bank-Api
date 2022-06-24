using api_transaction.Models;
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

        [HttpPost("ImportJsonData")]
        public async void PostGeneratedData([FromBody] Person[] data)
        {
            _context.Persons.AddRange(data);
            _context.SaveChanges();
            return;
        }
    }
}
