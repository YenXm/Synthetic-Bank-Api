using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace api_transaction.Migrations
{
    public partial class DeleteTypeColumn : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Type",
                table: "Transactions");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "Type",
                table: "Transactions",
                type: "longtext",
                nullable: false,
                collation: "utf8mb4_0900_ai_ci")
                .Annotation("MySql:CharSet", "utf8mb4");
        }
    }
}
