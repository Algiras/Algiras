
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_timeline():
    # Data
    events = [
        {"period": "2024 - Present", "role": "Senior Software Engineer", "company": "Your Company", "desc": "Leading architectural decisions and building scalable backend systems with Rust."},
        {"period": "2021 - 2024", "role": "Full Stack Developer", "company": "Previous Tech", "desc": "Developed robust web applications using React, Node.js, and TypeScript."},
        {"period": "2019 - 2021", "role": "Junior Developer", "company": "StartUp Inc.", "desc": "Contributed to frontend development and UI implementation."},
    ]

    # Setup figure with dark background
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor('#0d1117') # GitHub Dark background
    fig.patch.set_facecolor('#0d1117')

    # Hide axes
    ax.axis('off')
    
    # Draw vertical line
    start_y = 0.9
    end_y = 0.1
    ax.plot([0.1, 0.1], [start_y, end_y], color='#30363d', linewidth=2, zorder=1) # GitHub border color

    for i, event in enumerate(events):
        y_pos = start_y - (i * 0.25)
        
        # Draw node
        circle = patches.Circle((0.1, y_pos), 0.015, facecolor='#2ea043', edgecolor='#0d1117', linewidth=2, zorder=2) # GitHub green
        ax.add_patch(circle)

        # Draw text
        # Period
        ax.text(0.14, y_pos + 0.02, event['period'], 
                color='#8b949e', fontsize=10, fontfamily='sans-serif', weight='bold') # GitHub dimmed text
        
        # Role & Company
        ax.text(0.14, y_pos - 0.03, f"{event['role']} @ {event['company']}", 
                color='#c9d1d9', fontsize=14, fontfamily='sans-serif', weight='bold') # GitHub primary text
        
        # Description
        ax.text(0.14, y_pos - 0.08, event['desc'], 
                color='#8b949e', fontsize=10, fontfamily='sans-serif', style='italic') # GitHub dimmed text

    # Title
    ax.text(0.05, 0.98, "Professional Journey", 
            color='#58a6ff', fontsize=18, fontfamily='sans-serif', weight='bold') # GitHub link blue

    # Save
    plt.tight_layout()
    plt.savefig('professional-journey.png', dpi=300, bbox_inches='tight', facecolor='#0d1117')
    print("Timeline image generated successfully.")

if __name__ == "__main__":
    create_timeline()
