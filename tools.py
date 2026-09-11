from langchain.tools import tool


@tool
def create_email(to: str, subject: str, body: str) -> str:
    """
    Create an email draft.

    Use this tool when the user wants to prepare or draft an email.
    Do not send the email with this tool.
    """

    return (
        f"EMAIL DRAFT\n"
        f"To: {to}\n"
        f"Subject: {subject}\n"
        f"Body: {body}"
    )


@tool
def send_email(to: str, subject: str, body: str) -> str:
    """
    Send an email.

    Use this tool only when the user explicitly confirms
    that the email should be sent.
    """

    return (
        f"Email sent successfully.\n"
        f"To: {to}\n"
        f"Subject: {subject}"
    )