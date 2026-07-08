# PASSWORD VALIDATION

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

# ^           → Start
# (?=.*[A-Z]) → At least one uppercase letter
# (?=.*[a-z]) → At least one lowercase letter
# (?=.*\d)    → At least one digit
# .{8,}       → At least eight total characters
# $           → End