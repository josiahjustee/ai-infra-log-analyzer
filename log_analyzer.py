import tkinter as tk
error_db = [

    ("gpu", "GPU Failure", "Swap GPU. If error follows GPU → replace GPU, else replace baseboard", "ALL"),

    ("mle", "GPU Memory / MLE Error", "Reseat GPU if minor, replace if persistent", "ALL"),

    ("nvlink", "NVLink Failure", "Swap GPUs or replace baseboard", "VULCAN/B300"),

    ("link down", "Link Failure", "Check GPU / NVLink / baseboard", "ALL"),

    ("thermal", "Overheating", "Check heatsink, airflow, thermal paste", "ALL"),

    ("bmc_temp", "Thermal Sensor Issue", "Check thermal paste / replace baseboard", "ALL"),

    ("timeout", "Timeout Issue", "Retest / different tester / possible baseboard failure", "ALL"),

    ("task timeout 1800", "Timeout Failure", "Retest, if persists replace baseboard", "ALL"),

    ("lspci", "GPU Detection Failure", "Reseat GPUs, isolate faulty GPU, or replace baseboard", "B200"),

    ("missing gpu", "GPU Not Detected", "Reseat or replace GPU", "ALL"),

    ("pcie", "PCIe Issue", "Replace GPU or baseboard", "ALL"),

    ("cx8", "Retimer / CX8 Failure", "Check thermal paste or replace baseboard", "B300"),

    ("retimer", "Retimer Failure", "Replace baseboard", "B300"),

    ("write_protect", "Firmware Write Protection Issue", "Replace baseboard or HMC", "ALL"),

    ("firmware", "Firmware Failure", "Check firmware / replace component", "ALL"),

    ("rc version mismatch", "Version Mismatch", "Replace baseboard", "ALL"),

    ("power on fail", "Power Failure", "Retest / replace baseboard", "ALL"),

    ("dc power", "Power Issue", "Retest or replace baseboard", "ALL"),

    ("hmc", "HMC Failure", "Replace HMC or baseboard", "ALL"),

    ("fru", "FRU Error", "Retest / replace baseboard or battery", "ALL"),

    ("nvflash", "GPU Firmware Error", "Check GPU logs / swap GPU", "ALL"),

    ("nvswitch", "NVSwitch Failure", "Replace baseboard or GPU depending on logs", "VULCAN"),

    ("segmentation fault", "GPU Failure", "Replace GPU", "ALL"),

    ("row remapping failed", "GPU Memory Failure", "Replace GPU", "ALL"),

    ("crc", "GPU Data Error", "Replace GPU", "ALL"),

    ("heartbeat", "GPU Not Responding", "Replace GPU", "ALL"),

    ("invalid fw count", "Firmware / Wrong Hardware", "Replace HMC / verify hardware match", "ALL"),

]


# PLATFORM DETECTION


def detect_platform(text):

    text = text.lower()

 

    if "cx8" in text or "retimer" in text:

        return "Umbriel B300"

    elif "lspci" in text:

        return "Umbriel B200"

    elif "nvswitch" in text or "nvlink" in text:

        return "Vulcan"

    else:

        return "Unknown Platform"

 

# SEVERITY

def severity(issue):

    if "GPU" in issue or "Baseboard" in issue:

        return "CRITICAL"

    elif "Failure" in issue or "Thermal" in issue:

        return "HIGH"

    elif "Timeout" in issue:

        return "MEDIUM"

    else:

        return "LOW"


# ANALYZER

def analyze():

    user_input = entry.get()

 

    if not user_input:

        result.set("Please paste an error code.")

        return

 

    text = user_input.lower()

    platform = detect_platform(text)

 

    found_matches = []

 

    for keyword, issue, action, system in error_db:

        if keyword in text:

            found_matches.append((issue, action))

 

    if found_matches:

        issue, action = found_matches[0]

        priority = severity(issue)

 

        result.set(

            f"Platform: {platform}\n"

            f"Issue: {issue}\n"

            f"Action: {action}\n"

            f"Priority: {priority}"

        )

    else:

        result.set(

            f"Platform: {platform}\n"

            f"Issue: Unknown\n"

            f"Action: Check full logs"

        )

 

# UI

root = tk.Tk()

root.title("AI Infra Log Analyzer")

root.geometry("550x350")

root.configure(bg="#111")

 

title = tk.Label(root, text="AI Infrastructure Log Analyzer", font=("Arial", 16), bg="#111", fg="white")

title.pack(pady=10)

 

entry = tk.Entry(root, width=70)

entry.pack(pady=10)

 

button = tk.Button(root, text="Analyze", command=analyze, bg="#00adb5", fg="black", font=("Arial", 10))

button.pack(pady=10)

 

result = tk.StringVar()

output = tk.Label(root, textvariable=result, justify="left", font=("Consolas", 10), bg="#111", fg="white")

output.pack(pady=15)

 

root.mainloop()
