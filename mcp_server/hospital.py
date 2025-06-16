from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

from add_patient import add_new_patient

# Initialize FastMCP server
mcp = FastMCP("hospital")


@mcp.tool()
async def add_patient_new(name: str, issue: str, time_required: int):
    """
    Adds new patient info into hospital data
    
    Args:
        p_name: name of the patient
        issue: medical issue patient is suffering from
        time_required: time needed to diagonise the patient in hrs
    """
    result= add_new_patient({
        "p_name": name,
        "issue": issue,
        "time_required": time_required
    })
    
    return "Patient Added Successfully"
    

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')