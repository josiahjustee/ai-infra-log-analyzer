# AI Infrastructure Log Analyzer

A Python-based desktop tool for analyzing and triaging hardware errors 
in NVIDIA enterprise AI infrastructure environments. Built from real 
data center experience working with Vulcan, Umbriel B200, and 
Umbriel B300 server platforms.

## 🔍 Overview
In large-scale AI data centers, engineers deal with hundreds of errors 
logs daily across multiple server platforms. Manually reading through 
dense log output to identify the root cause of a failure is 
time-consuming and error-prone — especially under pressure when 
Production systems are down. This tool automates that process. Paste an error code or log snippet, 
and the analyzer instantly:
- Identifies which platform generated the error
- Classifies the type of hardware failure
- Recommends the exact troubleshooting steps
- Assigns a priority level so engineers know what to fix first
## 💼 Business Value
| Problem | How This Tool Solves It |
|---|---|
| Engineers waste time manually reading logs | Instant automated classification |
| Inconsistent troubleshooting across team members | Standardized recommendations from a central database |
| Hard to prioritize which issues to fix first | Automatic severity assignment (Critical/High/Medium/Low) |
| New technicians lack institutional knowledge | Tool encodes expert knowledge into an accessible interface |
| Production downtime costs money | Faster diagnosis = faster resolution = less downtime |

In enterprise AI environments, where a single server can cost 
$200,000+, reducing mean time to resolution (MTTR) by even 
30 minutes per incident has a significant financial impact.
## 🖥️ Supported Platforms

| Platform | Description |
|---|---|
| Vulcan | NVIDIA multi-GPU server with NVSwitch fabric |
| Umbriel B200 | NVIDIA Blackwell B200 GPU server |
| Umbriel B300 | NVIDIA Blackwell B300 GPU server with CX8 retimers |

---

## ⚙️ How It Works

1. **Input** — Engineer pastes an error code or log snippet into the tool
2. **Platform Detection** — Tool automatically identifies the server 
platform based on keywords in the log
3. **Error Matching** — Log is scanned against a database of 26 known 
error patterns covering GPU failures, NVLink issues, thermal faults, 
firmware errors, power failures, and more
4. **Output** — Tool returns the platform, issue classification, 
recommended action, and priority level instantly

## 🚨 Error Categories Covered

- GPU Failures & Memory Errors
- NVLink & NVSwitch Failures
- Thermal & Sensor Issues
- Firmware Errors & Version Mismatches
- PCIe & Retimer Failures
- Power Failures
- HMC & FRU Errors
- Timeout Issues
- GPU Detection Failures

## 📊 Priority Levels

| Level | Trigger |
|---|---|
| CRITICAL | GPU or baseboard replacement required |
| HIGH | Hardware failure or thermal issue detected |
| MEDIUM | Timeout or retest required |
| LOW | Minor or unclassified issue |


## 🛠️ Tech Stack

- **Python** — Core logic and application framework
- **tkinter** — Desktop GUI interface
- **Regex pattern matching** — Error keyword detection
- **Structured error database** — 26 known hardware failure patterns



## 🚀 How To Run

1. Make sure Python is installed on your machine
2. Clone this repository:
