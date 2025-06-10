import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import json
import threading
import tempfile
import shutil
import requests
import pandas as pd
import zipfile

# -----------------------------------------------
# PDF-Roundup API Invocation Summary:
# PDFs are requested by POSTing JSON to API_ENDPOINT with headers:
# {"Content-Type": "application/json", "x-api-key": api_key}
# and payload {"part_number": part}. On success, resp.json() returns
# a signed URL under key "signed_url" (adjust extract_signed_url as needed).
# -----------------------------------------------

API_ENDPOINT = "https://api.example.com/get_pdf"  # replace with real endpoint
CONFIG_PATH = os.path.expanduser("~/.pdf_roundup/key.json")

class PDFRoundupApp:
    def __init__(self, root):
        self.root = root
        root.title("PDF Round-Up")
        root.geometry("800x600")
        root.iconbitmap("app_icon.ico")

        # Splash/banner
        banner = tk.PhotoImage(file="banner.png")
        splash = tk.Label(root, image=banner, width=500, height=60)
        splash.image = banner
        splash.pack(pady=5)

        # File selectors
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        tk.Label(root, text="Select Excel or CSV file").pack(anchor="w", padx=10)
        in_frame = tk.Frame(root)
        tk.Entry(in_frame, textvariable=self.input_path, width=60).pack(side="left")
        tk.Button(in_frame, text="Browse...", command=self.browse_input).pack(side="left", padx=5)
        in_frame.pack(fill="x", padx=10)

        tk.Label(root, text="Select output folder").pack(anchor="w", padx=10, pady=(10,0))
        out_frame = tk.Frame(root)
        tk.Entry(out_frame, textvariable=self.output_path, width=60).pack(side="left")
        tk.Button(out_frame, text="Browse...", command=self.browse_output).pack(side="left", padx=5)
        out_frame.pack(fill="x", padx=10)

        # Zip options
        self.zip_var = tk.BooleanVar()
        self.zip_var.trace("w", lambda *a: self.toggle_zip())
        tk.Checkbutton(root, text="Zip output?", variable=self.zip_var).pack(anchor="w", padx=10, pady=(10,0))

        self.zip_frame = tk.Frame(root)
        self.zip_type = tk.StringVar(value="single")
        tk.Radiobutton(self.zip_frame, text="Single-zip", variable=self.zip_type, value="single").pack(anchor="w")
        multi_rb = tk.Radiobutton(self.zip_frame, text="Multi-zip", variable=self.zip_type, value="multi")
        multi_rb.pack(anchor="w")
        self.zip_type.trace("w", lambda *a: self.toggle_multi_options())

        self.multi_opts = tk.Frame(self.zip_frame)
        # by count
        count_frame = tk.Frame(self.multi_opts)
        tk.Label(count_frame, text="By file count:").pack(side="left")
        self.count_entry = tk.Entry(count_frame, width=5)
        self.count_entry.insert(0, "100")
        self.count_entry.pack(side="left", padx=5)
        count_frame.pack(anchor="w", pady=2)
        # by size
        size_frame = tk.Frame(self.multi_opts)
        tk.Label(size_frame, text="By archive size:").pack(side="left")
        self.size_entry = tk.Entry(size_frame, width=5)
        self.size_entry.insert(0, "10")
        self.size_entry.pack(side="left", padx=2)
        self.size_unit = tk.StringVar(value="MB")
        tk.OptionMenu(size_frame, self.size_unit, "KB","MB","GB").pack(side="left")
        size_frame.pack(anchor="w", pady=2)
        self.multi_opts.pack_forget()
        self.zip_frame.pack_forget()

        # Start button
        tk.Button(root, text="Start", command=self.start).pack(pady=10)

        # Log area
        self.log_area = scrolledtext.ScrolledText(root, state="disabled", height=15)
        self.log_area.pack(fill="both", expand=True, padx=10)

        # Status label
        self.status_label = tk.Label(root, text="Idle…")
        self.status_label.pack(fill="x", pady=5)

    def browse_input(self):
        path = filedialog.askopenfilename(filetypes=[("Excel/CSV", "*.xlsx *.xls *.csv")])
        if path: self.input_path.set(path)

    def browse_output(self):
        path = filedialog.askdirectory()
        if path: self.output_path.set(path)

    def toggle_zip(self):
        if self.zip_var.get():
            self.zip_frame.pack(fill="x", padx=20, pady=5)
        else:
            self.zip_frame.pack_forget()

    def toggle_multi_options(self):
        if self.zip_type.get() == "multi":
            self.multi_opts.pack(fill="x", padx=20)
        else:
            self.multi_opts.pack_forget()

    def log(self, msg):
        self.log_area.configure(state="normal")
        self.log_area.insert("end", msg + "\n")
        self.log_area.see("end")
        self.log_area.configure(state="disabled")
        with open(os.path.join(self.output_path.get(), "run_log.txt"), "a") as f:
            f.write(msg + "\n")

    def start(self):
        if not self.input_path.get() or not self.output_path.get():
            messagebox.showerror("Error", "Please select input file and output folder")
            return
        threading.Thread(target=self.run_process).start()

    def run_process(self):
        api_key = self.get_api_key()
        df = pd.read_excel(self.input_path.get(), header=0) if self.input_path.get().lower().endswith((".xls",".xlsx")) else pd.read_csv(self.input_path.get(), header=0)
        parts = df.iloc[:,0].dropna().astype(str).tolist()
        total = len(parts)
        temp_dir = tempfile.mkdtemp()
        downloaded = []

        self.clear_log()
        for idx, part in enumerate(parts, 1):
            self.update_status(f"Downloading {idx}/{total}…")
            try:
                resp = requests.post(API_ENDPOINT,
                                     headers={"Content-Type":"application/json","x-api-key":api_key},
                                     json={"part_number": part})
                resp.raise_for_status()
                url = self.extract_signed_url(resp)
                pdf_path = os.path.join(temp_dir, f"{part}.pdf")
                with requests.get(url, stream=True) as r:
                    r.raise_for_status()
                    with open(pdf_path, "wb") as f:
                        for chunk in r.iter_content(8192):
                            f.write(chunk)
                downloaded.append(pdf_path)
                self.log(f"{part}: SUCCESS {url}")
            except Exception as e:
                self.log(f"{part}: ERROR {e}")

        zips = []
        if not self.zip_var.get():
            for p in downloaded:
                shutil.move(p, self.output_path.get())
        else:
            if self.zip_type.get() == "single":
                zip_path = os.path.join(self.output_path.get(), "output.zip")
                with zipfile.ZipFile(zip_path, "w") as zf:
                    for p in downloaded:
                        zf.write(p, os.path.basename(p))
                zips.append(zip_path)
            else:
                if self.count_entry.winfo_ismapped():
                    chunk_size = int(self.count_entry.get())
                    for i in range(0, len(downloaded), chunk_size):
                        subset = downloaded[i:i+chunk_size]
                        zip_path = os.path.join(self.output_path.get(), f"output_{i//chunk_size+1}.zip")
                        with zipfile.ZipFile(zip_path, "w") as zf:
                            for p in subset:
                                zf.write(p, os.path.basename(p))
                        zips.append(zip_path)
                else:
                    max_bytes = int(self.size_entry.get()) * {"KB":1024, "MB":1024**2, "GB":1024**3}[self.size_unit.get()]
                    current_zip = []
                    current_size = 0
                    count = 1
                    for p in downloaded:
                        sz = os.path.getsize(p)
                        if current_size + sz > max_bytes and current_zip:
                            zip_path = os.path.join(self.output_path.get(), f"output_{count}.zip")
                            with zipfile.ZipFile(zip_path, "w") as zf:
                                for fpath in current_zip:
                                    zf.write(fpath, os.path.basename(fpath))
                            zips.append(zip_path)
                            count += 1
                            current_zip, current_size = [], 0
                        current_zip.append(p)
                        current_size += sz
                    if current_zip:
                        zip_path = os.path.join(self.output_path.get(), f"output_{count}.zip")
                        with zipfile.ZipFile(zip_path, "w") as zf:
                            for fpath in current_zip:
                                zf.write(fpath, os.path.basename(fpath))
                        zips.append(zip_path)
        shutil.rmtree(temp_dir)
        self.update_status(f"Done: {len(downloaded)} files → {len(zips)} zips")

    def extract_signed_url(self, resp):
        data = resp.json()
        return data.get("signed_url") or data.get("url")

    def get_api_key(self):
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH) as f:
                return json.load(f).get("api_key")
        key = tk.simpledialog.askstring("API Key", "Enter your PDF API Key:")
        if not key:
            messagebox.showerror("Error", "API Key is required")
            self.root.quit()
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        with open(CONFIG_PATH, "w") as f:
            json.dump({"api_key": key}, f)
        return key

    def clear_log(self):
        log_file = os.path.join(self.output_path.get(), "run_log.txt")
        if os.path.exists(log_file):
            os.remove(log_file)
        self.log_area.configure(state="normal")
        self.log_area.delete("1.0", "end")
        self.log_area.configure(state="disabled")

    def update_status(self, text):
        self.status_label.config(text=text)
        self.status_label.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFRoundupApp(root)
    root.mainloop()
