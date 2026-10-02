import sys
import io

with io.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Footer Links
footer_old = '''            <a href="#" style="font-size:14px;color:rgba(245,245,240,0.82);transition:color 180ms ease" style-hover="color:#CAA7A7">Shipping &amp; delivery</a>
            <a href="#" style="font-size:14px;color:rgba(245,245,240,0.82);transition:color 180ms ease" style-hover="color:#CAA7A7">Privacy policy</a>
            <a href="#" style="font-size:14px;color:rgba(245,245,240,0.82);transition:color 180ms ease" style-hover="color:#CAA7A7">Terms &amp; conditions</a>'''
footer_new = '''            <a href="/shipping-delivery" onClick="{{ goShipping }}" style="font-size:14px;color:rgba(245,245,240,0.82);transition:color 180ms ease" style-hover="color:#CAA7A7">Shipping &amp; delivery</a>
            <a href="/privacy-policy" onClick="{{ goPrivacy }}" style="font-size:14px;color:rgba(245,245,240,0.82);transition:color 180ms ease" style-hover="color:#CAA7A7">Privacy policy</a>
            <a href="/terms-conditions" onClick="{{ goTerms }}" style="font-size:14px;color:rgba(245,245,240,0.82);transition:color 180ms ease" style-hover="color:#CAA7A7">Terms &amp; conditions</a>'''
html = html.replace(footer_old, footer_new)

# Insert the pages HTML before aboutOpen
pages_html = """
  <sc-if value="{{ isShipping }}" hint-placeholder-val="{{ false }}">
    <div style="position:relative;z-index:1;background:#0A0A0A;padding-top:96px;min-height:100vh">
      <div style="max-width:800px;margin:0 auto;padding:48px 32px 96px">
        <h1 style="margin:0 0 24px;font-family:'Bodoni Moda',Georgia,serif;font-weight:400;font-size:38px;line-height:1.1">Shipping & Delivery</h1>
        <p style="font-size:14px;color:rgba(245,245,240,0.65);margin-bottom:32px">Last updated: 2 October 2026</p>
        
        <div style="display:flex;flex-direction:column;gap:24px;font-size:16px;line-height:1.6;color:#F5F5F0">
          <p>At Onehart, we want your new tees to reach you quickly and safely.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Free Shipping</h2>
          <p>We offer free shipping on all orders to serviceable addresses in India. No minimum order value is required.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Delivery Time</h2>
          <p>Orders are delivered in under 7 calendar days from order confirmation. This includes processing, packing, dispatch, and delivery.</p>
          <p>Exceptional circumstances, such as severe weather, transport disruptions, or courier service interruptions, may cause delays. If your order is delayed, contact us for an update and assistance. This does not affect your rights under applicable law.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Delivery Locations</h2>
          <p>Delivery is available to Indian addresses supported by our courier partners. If we cannot deliver to your address, we will contact you. Any payment collected for an order we cannot fulfil will be refunded.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Shipping Updates</h2>
          <p>Once your order is dispatched, we will share available tracking details through the contact information provided at checkout.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Delivery Details</h2>
          <p>Please provide your complete address, correct PIN code, and an active phone number.</p>
          <p>If you notice an error after placing your order, contact us immediately. Address changes depend on whether the order has already been dispatched.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Missing, Damaged, or Incorrect Deliveries</h2>
          <p>If your package has not arrived, appears damaged, or contains an incorrect item, contact us with your order number and details of the issue. Include photographs where relevant so we can investigate and arrange an appropriate resolution.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Contact Us</h2>
          <p>Email: <a href="mailto:onehart.clothing@gmail.com" style="color:#CAA7A7;text-decoration:underline">onehart.clothing@gmail.com</a><br>
          Phone: <a href="tel:+919994013477" style="color:#CAA7A7;text-decoration:underline">+91 99940 13477</a><br>
          Instagram: <a href="https://www.instagram.com/onehart.clothing" target="_blank" style="color:#CAA7A7;text-decoration:underline">https://www.instagram.com/onehart.clothing</a></p>
        </div>
      </div>
    </div>
  </sc-if>

  <sc-if value="{{ isPrivacy }}" hint-placeholder-val="{{ false }}">
    <div style="position:relative;z-index:1;background:#0A0A0A;padding-top:96px;min-height:100vh">
      <div style="max-width:800px;margin:0 auto;padding:48px 32px 96px">
        <h1 style="margin:0 0 24px;font-family:'Bodoni Moda',Georgia,serif;font-weight:400;font-size:38px;line-height:1.1">Privacy Policy</h1>
        <p style="font-size:14px;color:rgba(245,245,240,0.65);margin-bottom:32px">Last updated: 2 October 2026</p>
        
        <div style="display:flex;flex-direction:column;gap:24px;font-size:16px;line-height:1.6;color:#F5F5F0">
          <p>This Privacy Policy explains how Onehart collects, uses, and handles personal information when you visit <a href="http://www.onehart.in/" style="color:#CAA7A7;text-decoration:underline">www.onehart.in</a>, place an order, or contact us.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Information We Collect</h2>
          <p>Depending on how you use our website, we collect information such as:</p>
          <ul style="margin:0;padding-left:20px;display:flex;flex-direction:column;gap:8px">
            <li>Your name, email address, and phone number.</li>
            <li>Your shipping and billing addresses.</li>
            <li>Order details, products purchased, and payment status or transaction references.</li>
            <li>Information you provide when contacting customer support.</li>
            <li>Technical information generated when you use the website, such as your IP address, browser, device information, and pages visited, where collected by our website tools.</li>
          </ul>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">How We Use Your Information</h2>
          <p>We use relevant information to process orders, arrange delivery, communicate order updates, respond to questions, resolve complaints, prevent fraud, and maintain our website.</p>
          <p>Where you have opted in, we may send promotional messages. You can unsubscribe or contact us to stop receiving them. Essential order and service messages may still be sent.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Payments</h2>
          <p>Payments are processed by the payment providers available at checkout. Sensitive payment credentials are handled under those providers’ privacy and security policies.</p>
          <p>Please do not send us your card PIN, CVV, passwords, or payment OTPs.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Sharing Information</h2>
          <p>We share information needed to provide our services with relevant providers, such as delivery partners, payment processors, website hosting or store providers, and communication services.</p>
          <p>We may also disclose information where legally required or necessary to investigate fraud or protect lawful rights.</p>
          <p>We do not sell your personal information.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Cookies and Similar Technologies</h2>
          <p>Where used, cookies and similar technologies help the website function, remember preferences, and understand website usage.</p>
          <p>You can manage cookies through your browser settings. Disabling certain cookies may affect website features.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Information Security and Retention</h2>
          <p>We take reasonable steps to protect personal information. However, no online system can guarantee complete security.</p>
          <p>We keep information for as long as needed to fulfil orders, provide support, maintain necessary business records, and meet applicable legal obligations.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Your Choices</h2>
          <p>You can contact us to request access to, correction of, or deletion of your personal information, or to withdraw consent where processing depends on consent. We will handle requests according to applicable law.</p>
          <p>Some records may need to be retained for legal, accounting, fraud prevention, or unresolved order requirements.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Children’s Information</h2>
          <p>Our website is not intended to collect personal information from children without appropriate parent or guardian involvement. If you believe a child has provided information improperly, contact us so we can investigate.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Updates to This Policy</h2>
          <p>We may update this policy as our services change. The latest version will be published on this page.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Contact Us</h2>
          <p>For privacy questions or requests:<br>
          Email: <a href="mailto:onehart.clothing@gmail.com" style="color:#CAA7A7;text-decoration:underline">onehart.clothing@gmail.com</a><br>
          Phone: <a href="tel:+919994013477" style="color:#CAA7A7;text-decoration:underline">+91 99940 13477</a></p>
        </div>
      </div>
    </div>
  </sc-if>

  <sc-if value="{{ isTerms }}" hint-placeholder-val="{{ false }}">
    <div style="position:relative;z-index:1;background:#0A0A0A;padding-top:96px;min-height:100vh">
      <div style="max-width:800px;margin:0 auto;padding:48px 32px 96px">
        <h1 style="margin:0 0 24px;font-family:'Bodoni Moda',Georgia,serif;font-weight:400;font-size:38px;line-height:1.1">Terms & Conditions</h1>
        <p style="font-size:14px;color:rgba(245,245,240,0.65);margin-bottom:32px">Last updated: 2 October 2026</p>
        
        <div style="display:flex;flex-direction:column;gap:24px;font-size:16px;line-height:1.6;color:#F5F5F0">
          <p>These Terms & Conditions apply to your use of <a href="http://www.onehart.in/" style="color:#CAA7A7;text-decoration:underline">www.onehart.in</a> and purchases made from Onehart. Please read them before placing an order.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Using Our Website</h2>
          <p>You agree to provide accurate information and use the website lawfully. You must not attempt to disrupt the website, gain unauthorised access, commit fraud, or misuse another person’s information.</p>
          <p>If you are under 18, purchases must be made with the involvement and consent of a parent or legal guardian.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Products</h2>
          <p>Onehart sells T-shirts featuring original text and graphic designs. Please check the product description, size guide, colour, and selected size before ordering.</p>
          <p>We aim to display products accurately. Colours may appear slightly different depending on your screen and lighting. This does not affect your rights if a product is defective or materially different from its description.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Prices and Payments</h2>
          <p>Prices are displayed in Indian rupees. The final payable amount, including any applicable taxes or discounts, is shown at checkout.</p>
          <p>Shipping is free to serviceable addresses in India. Available payment methods are displayed at checkout.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Order Confirmation and Availability</h2>
          <p>Orders are subject to stock availability and successful payment where required.</p>
          <p>If we cannot fulfil your order because an item is unavailable or an order contains a material listing error, we will contact you. Any payment collected for an order we cancel will be refunded.</p>
          <p>We will not charge a revised price without your agreement.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Shipping and Delivery</h2>
          <p>Orders are delivered in under 7 calendar days from order confirmation, subject to the exceptional circumstances described in our <a href="/shipping-delivery" onClick="{{ goShipping }}" style="color:#CAA7A7;text-decoration:underline">Shipping & Delivery</a> policy.</p>
          <p>Please provide accurate delivery details and an active contact number.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Order Changes and Cancellations</h2>
          <p>If you need to change or cancel an order, contact us immediately with your order number. We will confirm whether the request can be accommodated based on the order’s processing and dispatch status.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Returns and Order Issues</h2>
          <p>All sales are final. Onehart does not accept returns for change of mind, personal preference, or incorrect size selection. Please check the size guide and product details before placing your order.</p>
          <p>If you receive a damaged, defective, or incorrect item, an item materially different from its description, or your order is not delivered or arrives late, contact us with your order number and photographs where relevant.</p>
          <p>We will investigate and provide an appropriate resolution, including a replacement or refund where required by applicable law.</p>
          <p>This policy does not limit your statutory consumer rights.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Intellectual Property</h2>
          <p>Onehart’s branding, original designs, images, and website content belong to Onehart or their respective rights holders. Commercial copying, reproduction, or distribution requires permission.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Third-Party Services</h2>
          <p>Our website may use third-party payment, delivery, or other service providers. Their services may also be governed by their own terms and privacy policies.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Applicable Law</h2>
          <p>These terms are governed by the laws of India. Nothing here removes your right to approach a competent consumer commission or other authority.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Changes to These Terms</h2>
          <p>We may update these terms. Changes will apply prospectively and will not remove rights relating to orders already placed.</p>
          
          <h2 style="margin:0;font-size:20px;font-weight:600">Contact Us</h2>
          <p>For order support or complaints:<br>
          Email: <a href="mailto:onehart.clothing@gmail.com" style="color:#CAA7A7;text-decoration:underline">onehart.clothing@gmail.com</a><br>
          Phone: <a href="tel:+919994013477" style="color:#CAA7A7;text-decoration:underline">+91 99940 13477</a><br>
          Website: <a href="https://www.onehart.in" target="_blank" style="color:#CAA7A7;text-decoration:underline">https://www.onehart.in</a><br>
          Instagram: <a href="https://www.instagram.com/onehart.clothing" target="_blank" style="color:#CAA7A7;text-decoration:underline">https://www.instagram.com/onehart.clothing</a></p>
        </div>
      </div>
    </div>
  </sc-if>
"""
html = html.replace('<sc-if value="{{ aboutOpen }}" hint-placeholder-val="{{ false }}">', pages_html + '\n  <sc-if value="{{ aboutOpen }}" hint-placeholder-val="{{ false }}">')

# Modify state setup for routing
state_old = "state = { page: 'home', scrolled: false, size: null, cart: 0, open: {},"
state_new = "state = { page: (typeof window !== 'undefined' && window.location.pathname.includes('shipping')) ? 'shipping' : (typeof window !== 'undefined' && window.location.pathname.includes('privacy')) ? 'privacy' : (typeof window !== 'undefined' && window.location.pathname.includes('terms')) ? 'terms' : 'home', scrolled: false, size: null, cart: 0, open: {},"
html = html.replace(state_old, state_new)

# Add logic methods
methods_old = "      isPdp: this.state.page === 'pdp',"
methods_new = '''      isPdp: this.state.page === 'pdp',
      isShipping: this.state.page === 'shipping',
      isPrivacy: this.state.page === 'privacy',
      isTerms: this.state.page === 'terms',
      goShipping: (e) => { e?.preventDefault(); window.scrollTo(0, 0); if(typeof window !== 'undefined') window.history.pushState({}, '', '/shipping-delivery'); this.setState({ page: 'shipping', menuOpen: false }); },
      goPrivacy: (e) => { e?.preventDefault(); window.scrollTo(0, 0); if(typeof window !== 'undefined') window.history.pushState({}, '', '/privacy-policy'); this.setState({ page: 'privacy', menuOpen: false }); },
      goTerms: (e) => { e?.preventDefault(); window.scrollTo(0, 0); if(typeof window !== 'undefined') window.history.pushState({}, '', '/terms-conditions'); this.setState({ page: 'terms', menuOpen: false }); },'''
html = html.replace(methods_old, methods_new)

with io.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
