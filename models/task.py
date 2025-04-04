class Task:
    def __init__(self, title, description, due_date, priority):
        # Validate title
        if not title or title.strip() == "":
            raise ValueError("Title cannot be empty")

        # Validate date format (basic validation)
        if not self._is_valid_date(due_date):
            raise ValueError("Invalid date format. Use YYYY-MM-DD")

        # Validate priority
        valid_priorities = ["Alta", "Media", "Baja"]
        if priority not in valid_priorities:
            raise ValueError(f"Priority must be one of: {', '.join(valid_priorities)}")

        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = "Pending"

    def _is_valid_date(self, date_string):
        """Validate date format YYYY-MM-DD"""
        try:
            from datetime import datetime
            datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def to_dict(self):
        """Convert task to dictionary"""
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        """Create a task from dictionary"""
        task = cls(
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
            priority=data["priority"]
        )
        task.status = data["status"]
        return task

    def mark_as_completed(self):
        """Marca la tarea como completada"""
        self.status = "Completed"
        
    def is_completed(self):
        """Verifica si la tarea está completada"""
        return self.status == "Completed"