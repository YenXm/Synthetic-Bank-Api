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

        [HttpPost("ImportJsonData")]
        public async void PostGeneratedData([FromBody] Person[] data)
        {
            var test = PythonService.run_cmd();

            //_context.Persons.AddRange(data);
            //_context.SaveChanges();
            return;
        }
    }
}
