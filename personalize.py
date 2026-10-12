"""Apply fictional/sample details to Jessica Abby Photography website."""
from pathlib import Path
import re

root = Path(__file__).resolve().parent / 'public'

# 1. Create a clean professional SVG logo
logo_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="70" viewBox="0 0 320 70">
  <text x="160" y="38" text-anchor="middle" fill="#1a1a1a" font-family="'Playfair Display', Georgia, serif" font-size="26" font-weight="600" letter-spacing="3">KAVYA SHARMA</text>
  <text x="160" y="58" text-anchor="middle" fill="#888888" font-family="'Montserrat', sans-serif" font-size="11" letter-spacing="6">PHOTOGRAPHY</text>
</svg>'''
(root / 'jessica-logo.svg').write_text(logo_svg, encoding='utf-8')

# 2. Contact form & details HTML card for contact page
contact_card_html = '''
<div style="max-width: 750px; margin: 40px auto; padding: 35px 30px; background: #faf9f6; border: 1px solid #e8e5df; border-radius: 8px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px; margin-bottom: 35px; border-bottom: 1px solid #e5e2dc; padding-bottom: 25px; text-align: left;">
    <div>
      <h4 style="margin: 0 0 8px; font-size: 13px; text-transform: uppercase; letter-spacing: 1.5px; color: #8c827a;">Studio Address</h4>
      <p style="margin: 0; font-size: 15px; color: #2c2c2c; line-height: 1.5;">
        Studio 4B, Heritage Galleria<br>
        M.G. Road, Connaught Place<br>
        New Delhi, 110001, India
      </p>
    </div>
    <div>
      <h4 style="margin: 0 0 8px; font-size: 13px; text-transform: uppercase; letter-spacing: 1.5px; color: #8c827a;">Direct Contact</h4>
      <p style="margin: 0; font-size: 15px; color: #2c2c2c; line-height: 1.6;">
        <strong>Phone:</strong> +91 98765 43210<br>
        <strong>WhatsApp:</strong> +91 98112 34567<br>
        <strong>Email:</strong> <a href="mailto:hello@kavyasharma.example" style="color: #635343; text-decoration: none;">hello@kavyasharma.example</a>
      </p>
    </div>
    <div>
      <h4 style="margin: 0 0 8px; font-size: 13px; text-transform: uppercase; letter-spacing: 1.5px; color: #8c827a;">Studio Hours</h4>
      <p style="margin: 0; font-size: 15px; color: #2c2c2c; line-height: 1.5;">
        Monday – Saturday<br>
        10:00 AM – 7:00 PM IST<br>
        <em>(By Appointment)</em>
      </p>
    </div>
  </div>

  <h3 style="font-family: 'Playfair Display', Georgia, serif; font-size: 24px; color: #222; margin: 0 0 10px; text-align: center;">Send an Inquiry</h3>
  <p style="text-align: center; color: #666; font-size: 14px; margin-bottom: 25px;">Fill out the details below and we will get back to you within 24 hours.</p>

  <form onsubmit="event.preventDefault(); alert('Thank you for reaching out! Your inquiry has been received. We will connect with you shortly.');" style="display: flex; flex-direction: column; gap: 16px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
      <div>
        <label style="display: block; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; color: #444;">Your Name *</label>
        <input type="text" required placeholder="Aarav Sharma" style="width: 100%; padding: 12px 14px; border: 1px solid #d4cfc7; border-radius: 4px; font-size: 14px; box-sizing: border-box; background: #fff;" />
      </div>
      <div>
        <label style="display: block; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; color: #444;">Email Address *</label>
        <input type="email" required placeholder="aarav@example.com" style="width: 100%; padding: 12px 14px; border: 1px solid #d4cfc7; border-radius: 4px; font-size: 14px; box-sizing: border-box; background: #fff;" />
      </div>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
      <div>
        <label style="display: block; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; color: #444;">Phone Number *</label>
        <input type="tel" required placeholder="+91 98765 00000" style="width: 100%; padding: 12px 14px; border: 1px solid #d4cfc7; border-radius: 4px; font-size: 14px; box-sizing: border-box; background: #fff;" />
      </div>
      <div>
        <label style="display: block; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; color: #444;">Event / Wedding Date</label>
        <input type="date" style="width: 100%; padding: 12px 14px; border: 1px solid #d4cfc7; border-radius: 4px; font-size: 14px; box-sizing: border-box; background: #fff;" />
      </div>
    </div>

    <div>
      <label style="display: block; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; color: #444;">Event Location / City</label>
      <input type="text" placeholder="e.g. Udaipur, Jaipur, New Delhi, Destination" style="width: 100%; padding: 12px 14px; border: 1px solid #d4cfc7; border-radius: 4px; font-size: 14px; box-sizing: border-box; background: #fff;" />
    </div>

    <div>
      <label style="display: block; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; color: #444;">Tell Us About Your Vision & Story</label>
      <textarea rows="4" placeholder="Share your plans, estimated guest count, or any special moments you want captured..." style="width: 100%; padding: 12px 14px; border: 1px solid #d4cfc7; border-radius: 4px; font-size: 14px; box-sizing: border-box; background: #fff; resize: vertical;"></textarea>
    </div>

    <button type="submit" style="align-self: center; background: #222; color: #fff; padding: 14px 40px; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; border: none; border-radius: 4px; cursor: pointer; transition: background 0.2s; margin-top: 10px;">
      Submit Inquiry
    </button>
  </form>
</div>
'''

new_footer_copyright = '''Kavya Sharma Photography&nbsp; |&nbsp; Studio 4B, MG Road, New Delhi&nbsp; |&nbsp; +91 98765 43210&nbsp; |&nbsp; <a href="/contact-jessica-abby-photography/">hello@kavyasharma.example</a>&nbsp; |&nbsp; <a href="/sitemap/index.html">Sitemap</a>'''

count = 0
for file in root.rglob('*.html'):
    text = file.read_text(encoding='utf-8')

    # Replace brand names and titles
    text = text.replace('Jessica Abby Photography', 'Kavya Sharma Photography')
    text = text.replace('Jessica Abby', 'Kavya Sharma')
    text = text.replace('hello@jessicaabby.com', 'hello@kavyasharma.example')
    text = text.replace('instagram.com/jessicaabbyphotography/', 'instagram.com/kavyasharmaphotography/')
    text = text.replace('Wedding photography packages begin at $3,800', 'Wedding photography packages begin at ₹1,49,000')

    # Update copyright notice
    text = re.sub(
        r'Copyright\s*[©\ufffd\?]*\s*\d{4}\s*jessicaabbyphotography',
        'Copyright © 2026 Kavya Sharma Photography',
        text,
        flags=re.IGNORECASE
    )

    # Replace logo image in header with SVG logo
    text = text.replace(
        '/assets/format.creatorcdn.com/5849172b2ab81cf99f6f160c.jpg',
        '/jessica-logo.svg'
    )

    # Replace footer copyright line
    text = re.sub(
        r'<small class="copyright">.*?</small>',
        f'<small class="copyright">{new_footer_copyright}</small>',
        text,
        flags=re.DOTALL
    )

    # Specific update for contact page
    if file.parent.name == 'contact-jessica-abby-photography':
        text = re.sub(
            r'<p style="padding:30px;text-align:center">Local preview.*?</p><script.*?</script>',
            contact_card_html,
            text,
            flags=re.DOTALL
        )
        # Update intro text on contact page
        text = text.replace(
            'Based in Melbourne, Victoria, I’m always ready to travel! I frequently photograph weddings and sessions throughout Victoria and South Australia',
            'Based in New Delhi, India, I’m always ready to travel! I frequently photograph weddings and sessions across Delhi NCR, Rajasthan, Goa, and worldwide'
        )
        text = text.replace(
            'Based in Melbourne, Victoria, I\ufffdm always ready to travel! I frequently photograph weddings and sessions throughout Victoria and South Australia',
            'Based in New Delhi, India, I’m always ready to travel! I frequently photograph weddings and sessions across Delhi NCR, Rajasthan, Goa, and worldwide'
        )

    # Specific update for about page
    if file.parent.name == 'aboutjessicaabby':
        text = text.replace('Dog Lover, Rabbit Lover, Travel Lover, Garden Lover', 'Destination Wedding & Intimate Portrait Photographer')
        text = text.replace('photograph over 400 weddings both in Australia and worldwide', 'photograph over 350 weddings across India and worldwide')

    file.write_text(text, encoding='utf-8')
    count += 1

print(f"Successfully personalized {count} HTML files in Jessica website!")
