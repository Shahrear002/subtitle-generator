import os
import threading
import customtkinter as ctk
from tkinter import filedialog
from faster_whisper import WhisperModel
from datetime import timedelta

# --- CONFIGURATION ---
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class SubtitleGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Whisper AI Subtitle Generator")
        self.geometry("600x450")
        self.resizable(False, False)

        # Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # 1. Title
        self.label_title = ctk.CTkLabel(self, text="AI Subtitle Generator", font=("Segoe UI", 24, "bold"))
        self.label_title.grid(row=0, column=0, padx=20, pady=(20, 10))

        # 2. File Selection Area
        self.frame_file = ctk.CTkFrame(self)
        self.frame_file.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        self.btn_browse = ctk.CTkButton(self.frame_file, text="Select Video File", command=self.select_file)
        self.btn_browse.pack(side="left", padx=10, pady=10)
        
        self.lbl_filename = ctk.CTkLabel(self.frame_file, text="No file selected", text_color="gray")
        self.lbl_filename.pack(side="left", padx=10)

        # 3. Log / Status Area
        self.textbox_log = ctk.CTkTextbox(self, width=500, height=200)
        self.textbox_log.grid(row=2, column=0, padx=20, pady=10)
        self.textbox_log.insert("0.0", "Ready to start...\n")
        self.textbox_log.configure(state="disabled") # Read-only

        # 4. Action Buttons
        self.btn_start = ctk.CTkButton(self, text="Generate Subtitles", command=self.start_thread, state="disabled", fg_color="#2CC985", text_color="white", text_color_disabled="white")
        self.btn_start.grid(row=3, column=0, padx=20, pady=20)

        # Variables
        self.selected_file = None
        self.model = None

    def log(self, message):
        """Thread-safe logging to the text box"""
        self.textbox_log.configure(state="normal")
        self.textbox_log.insert("end", message + "\n")
        self.textbox_log.see("end")
        self.textbox_log.configure(state="disabled")

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.mkv *.mov *.avi *.mp3 *.wav")])
        if file_path:
            self.selected_file = file_path
            self.lbl_filename.configure(text=os.path.basename(file_path), text_color="white")
            self.btn_start.configure(state="normal")
            self.log(f"📂 Selected: {os.path.basename(file_path)}")

    def start_thread(self):
        """Runs the heavy task in a separate thread so UI doesn't freeze"""
        self.btn_start.configure(state="disabled", text="Running...")
        self.btn_browse.configure(state="disabled")
        
        thread = threading.Thread(target=self.process_video)
        thread.start()

    def process_video(self):
        try:
            # 1. Load Model (Lazy Loading)
            if self.model is None:
                self.log("🚀 Loading Whisper Model (Small)... this may take a moment.")
                # Change to "small" or "medium" as needed. "int8" is faster on CPU.
                self.model = WhisperModel("small", device="cpu", compute_type="int8")
                self.log("✅ Model Loaded.")

            # 2. Transcribe
            self.log(f"⏳ Transcribing {os.path.basename(self.selected_file)}...")
            segments, info = self.model.transcribe(self.selected_file, language="bn") # Force Bangla

            # 3. Generate SRT Content
            srt_content = ""
            count = 0
            for i, segment in enumerate(segments, start=1):
                # Format timestamp: 00:00:10,000
                start = str(timedelta(seconds=int(segment.start))) + ",000"
                end = str(timedelta(seconds=int(segment.end))) + ",000"
                text = segment.text.strip()
                
                srt_content += f"{i}\n{start} --> {end}\n{text}\n\n"
                
                # Update UI every 10 segments so user knows it's working
                count += 1
                if count % 10 == 0:
                    self.log(f"   ... Processed {int(segment.end)} seconds")

            # 4. Save File
            base_name = os.path.splitext(self.selected_file)[0]
            output_path = f"{base_name}.srt"
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(srt_content)

            self.log(f"🎉 DONE! Saved to:\n{output_path}")

        except Exception as e:
            self.log(f"❌ Error: {str(e)}")
        
        finally:
            # Reset UI
            self.btn_start.configure(state="normal", text="Generate Subtitles")
            self.btn_browse.configure(state="normal")

if __name__ == "__main__":
    app = SubtitleGeneratorApp()
    app.mainloop()