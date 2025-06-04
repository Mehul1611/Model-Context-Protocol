from mcp_server.server import mcp
from utils.file_reader import read_parquet_summary

@mcp.tool()
def summarize_parquet_file(filename: str) -> str:
    """
    Summarize a Parquet file by giving out the data in the file.
    Args:
        filename: Name of the Parquet file in the /data directory (e.g., 'sample.parquet')
    Returns:
        A summary of the file.
    """
    return read_parquet_summary(filename)


# @mcp.prompt()
# def parquet_file_funny(filename: str) -> str:
#     """
#     Summarize a Parquet file by giving out the data in the file.
#     Args:
#         filename: Name of the Parquet file in the /data directory (e.g., 'sample.parquet')
#     Returns:
#         A summary of the file.
#     """
#     return read_parquet_summary(filename)