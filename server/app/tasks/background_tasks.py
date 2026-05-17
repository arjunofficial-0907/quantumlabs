from fastapi import BackgroundTasks

from app.email.email_service import (
    send_contact_email
)


def send_contact_notification(
    background_tasks: BackgroundTasks,
    name: str,
    email: str,
    message: str
):

    background_tasks.add_task(
        send_contact_email,
        name,
        email,
        message
    )