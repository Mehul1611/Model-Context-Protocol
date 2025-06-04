from mcp_server.server import mcp
from utils.file_reader import read_csv_summary


@mcp.tool()
def summarize_csv_file(filename: str) -> str:
    """
    Summarize a CSV file by giving out the data in the file.
    Args:
        filename: Name of the CSV file in the /data directory (e.g., 'sample.csv')
    Returns:
        A summary of the file.
    """
    return read_csv_summary(filename)