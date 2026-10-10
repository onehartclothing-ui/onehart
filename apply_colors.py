import re
import io

def run():
    with io.open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. HTML Color Selector
    size_html = '''          <div style="display:flex;flex-direction:column;gap:12px">
            <div style="display:flex;align-items:center;justify-content:space-between;gap:16px">
              <span style="font-size:12px;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;color:rgba(245,245,240,0.65)">Select size</span>'''
    
    color_html = '''          <sc-if value="{{ hasColors }}" hint-placeholder-val="{{ false }}">
            <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:12px">
              <div style="display:flex;align-items:center;justify-content:space-between;gap:16px">
                <span style="font-size:12px;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;color:rgba(245,245,240,0.65)">Color: <span style="color:#F5F5F0">{{ pdpColorName }}</span></span>
              </div>
              <div style="display:flex;flex-wrap:wrap;gap:14px;align-items:center;">
                <sc-for list="{{ pdpColorOptions }}" as="col" hint-placeholder-count="3">
                  <button onClick="{{ col.select }}" aria-label="{{ col.name }}" style="width:28px;height:28px;border-radius:50%;background:{{ col.hex }};border:1px solid rgba(255,255,255,0.15);cursor:pointer;outline:none;padding:0;transition:all 200ms ease;position:relative;box-shadow:0 2px 5px rgba(0,0,0,0.5)">
                    <span style="position:absolute;inset:-4px;border-radius:50%;border:1px solid {{ col.ring }};transition:border-color 200ms ease"></span>
                  </button>
                </sc-for>
              </div>
            </div>
          </sc-if>
          <div style="display:flex;flex-direction:column;gap:12px">
            <div style="display:flex;align-items:center;justify-content:space-between;gap:16px">
              <span style="font-size:12px;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;color:rgba(245,245,240,0.65)">Select size</span>'''
    
    html = html.replace(size_html, color_html)

    # 2. Add pdpColor to state
    html = html.replace("pdp: 0, view: 0,", "pdp: 0, pdpColor: 0, view: 0,")
    html = html.replace("pdp: ci, view: 0,", "pdp: ci, pdpColor: 0, view: 0,")
    html = html.replace("pdp: i, view: 0,", "pdp: i, pdpColor: 0, view: 0,")
    html = html.replace("pdp: (s.pdp + 1) % cat.length, view: 0", "pdp: (s.pdp + 1) % cat.length, pdpColor: 0, view: 0")
    html = html.replace("pdp: (s.pdp - 1 + cat.length) % cat.length, view: 0", "pdp: (s.pdp - 1 + cat.length) % cat.length, pdpColor: 0, view: 0")

    # 3. Update catalog()
    catalog_old = r"""  catalog\(\) \{\s*return \[(.*?)\];\s*\}"""
    catalog_new = """  catalog() {
    return [
      ['Blue Obsession', 899, 999, this.asset('tee1', './Front/Blue Obsession.png'), this.asset('tee1_b', './back/Blue Obsession.png'), [{name:'Black',hex:'#111111'},{name:'Beige',hex:'#E6DCC8',front:'./Front/Blue Obsession Beige.png',back:'./back/Blue Obsession Beige.png'}]],
      ['Born Iconic', 799, 899, this.asset('tee2', './Front/Born Iconic.png'), this.asset('tee2_b', './back/Born Iconic.png'), [{name:'Black',hex:'#111111'},{name:'Navy',hex:'#111827',front:'./Front/Born Iconic Navy.png',back:'./back/Born Iconic Navy.png'}]],
      ['Diva Energy', 799, 899, this.asset('tee3', './Front/Diva Energy.png'), this.asset('tee3_b', './back/Diva Energy.png'), [{name:'Black',hex:'#111111'}]],
      ['Faith Unbroken', 799, 899, this.asset('tee4', './Front/Faith Unbroken.png'), this.asset('tee4_b', './back/Faith Unbroken.png'), [{name:'Black',hex:'#111111'},{name:'Navy',hex:'#111827',front:'./Front/Faith Unbroken Navy.png',back:'./back/Faith Unbroken Navy.png'}]],
      ['Forever Yours', 899, 999, this.asset('tee5', './Front/Forever Yours.png'), this.asset('tee5_b', './back/Forever Yours.png'), [{name:'Black',hex:'#111111'},{name:'Beige',hex:'#E6DCC8',front:'./Front/Forever Yours Beige.png',back:'./back/Forever Yours Beige.png'}]],
      ['Heartbreaker', 799, 899, this.asset('tee6', './Front/Heartbreaker.png'), this.asset('tee6_b', './back/Heartbreaker.png'), [{name:'Black',hex:'#111111'}]],
      ['Kiss & Kill', 799, 899, this.asset('tee7', './Front/Kiss & Kill.png'), this.asset('tee7_b', './back/Kiss & Kill.png'), [{name:'Black',hex:'#111111'},{name:'Beige',hex:'#E6DCC8',front:'./Front/Kiss & Kill Beige.png',back:'./back/Kiss & Kill Beige.png'},{name:'Navy',hex:'#111827',front:'./Front/Kiss & Kill Navy.png',back:'./back/Kiss & Kill Navy.png'}]],
      ['Lucky Theory', 899, 999, this.asset('tee8', './Front/Lucky Theory.png'), this.asset('tee8_b', './back/Lucky Theory.png'), [{name:'Black',hex:'#111111'},{name:'Beige',hex:'#E6DCC8',front:'./Front/Lucky Theory Beige.png',back:'./back/Lucky Theory Beige.png'}]],
      ['Midnight Madness', 899, 999, this.asset('tee9', './Front/Midnight Madness.png'), this.asset('tee9_b', './back/Midnight Madness.png'), [{name:'Black',hex:'#111111'},{name:'Navy',hex:'#111827',front:'./Front/Midnight Madness Navy.png',back:'./back/Midnight Madness Navy.png'}]],
      ['Money Talks', 799, 899, this.asset('tee10', './Front/Money Talks.png'), this.asset('tee10_b', './back/Money Talks.png'), [{name:'Black',hex:'#111111'}]],
      ['No Pressure', 899, 999, this.asset('tee11', './Front/No Pressure.png'), this.asset('tee11_b', './back/No Pressure.png'), [{name:'Black',hex:'#111111'},{name:'Navy',hex:'#111827',front:'./Front/No Pressure Navy.png',back:'./back/No Pressure Navy.png'}]],
      ['Sugar Rush', 799, 899, this.asset('tee12', './Front/Sugar Rush.png'), this.asset('tee12_b', './back/Sugar Rush.png'), [{name:'Black',hex:'#111111'},{name:'Beige',hex:'#E6DCC8',front:'./Front/Sugar Rush Beige.png',back:'./back/Sugar Rush Beige.png'}]],
      ['Wild West', 899, 999, this.asset('tee13', './Front/Wild West.png'), this.asset('tee13_b', './back/Wild West.png'), [{name:'Black',hex:'#111111'},{name:'Beige',hex:'#E6DCC8',front:'./Front/Wild West Beige.png',back:'./back/Wild West Beige.png'},{name:'Navy',hex:'#111827',front:'./Front/Wild West Navy.png',back:'./back/Wild West Navy.png'}]]
    ];
  }"""
    html = re.sub(catalog_old, catalog_new, html, flags=re.DOTALL)

    # 4. Update variants()
    variants_old = r"""  variants\(\) \{\s*return \[(.*?)\];\s*\}"""
    variants_new = """  variants() {
    return [
      [ { S: '47796266205340', M: '47796266238108', L: '47796266270876', XL: '47796266303644' }, null ],
      [ { S: '47796274036892', M: '47796274069660', L: '47796274102428', XL: '47796274135196' }, null ],
      [ { S: '47796289175708', M: '47796289208476', L: '47796289241244', XL: '47796289274012' } ],
      [ { S: '47796297367708', M: '47796297400476', L: '47796297433244', XL: '47796297466012' }, null ],
      [ { S: '47796305887388', M: '47796305920156', L: '47796305952924', XL: '47796305985692' }, null ],
      [ { S: '47796314964124', M: '47796314996892', L: '47796315029660', XL: '47796315062428' } ],
      [ { S: '47796322304156', M: '47796322336924', L: '47796322369692', XL: '47796322402460' }, null, null ],
      [ { S: '47796349960348', M: '47796349993116', L: '47796350025884', XL: '47796350058652' }, null ],
      [ { S: '47796333314204', M: '47796333346972', L: '47796333379740', XL: '47796333412508' }, null ],
      [ { S: '47796357103772', M: '47796357136540', L: '47796357169308', XL: '47796357202076' } ],
      [ { S: '47796342620316', M: '47796342653084', L: '47796342685852', XL: '47796342718620' }, null ],
      [ { S: '47796363919516', M: '47796363952284', L: '47796363985052', XL: '47796364017820' }, null ],
      [ { S: '47796365164700', M: '47796365197468', L: '47796365230236', XL: '47796365263004' }, null, null ]
    ];
  }"""
    html = re.sub(variants_old, variants_new, html, flags=re.DOTALL)

    # 5. Update render logic inside render() or the state derivation map
    render_old = '''      pdpName: cur[0],
      pdpPrice: this.rupees(cur[1]),
      pdpOriginalPrice: this.rupees(cur[2]),
      pdpImage: cur[3],
      pdpBack: cur[4] || cur[3],'''
      
    render_new = '''      pdpName: cur[0],
      pdpPrice: this.rupees(cur[1]),
      pdpOriginalPrice: this.rupees(cur[2]),
      pdpImage: (cur[5] && cur[5][this.state.pdpColor] && cur[5][this.state.pdpColor].front) ? cur[5][this.state.pdpColor].front : cur[3],
      pdpBack: (cur[5] && cur[5][this.state.pdpColor] && cur[5][this.state.pdpColor].back) ? cur[5][this.state.pdpColor].back : (cur[4] || cur[3]),
      hasColors: cur[5] && cur[5].length > 1,
      pdpColorName: cur[5] ? (cur[5][this.state.pdpColor] ? cur[5][this.state.pdpColor].name : '') : '',
      pdpColorOptions: (cur[5] || []).map((c, i) => ({
        name: c.name,
        hex: c.hex,
        ring: this.state.pdpColor === i ? '#FFFFFF' : 'transparent',
        select: (e) => { e.preventDefault(); this.setState({ pdpColor: i }); }
      })),'''
    
    html = html.replace(render_old, render_new)

    # 6. Update addToCart
    add_old = '''      addToCart: () => {
        if (!this.state.size) return;
        const key = this.state.pdp + '|' + this.state.size;'''
    add_new = '''      addToCart: () => {
        if (!this.state.size) return;
        const key = this.state.pdp + '|' + this.state.pdpColor + '|' + this.state.size;'''
    html = html.replace(add_old, add_new)

    # 7. Update checkout
    check_old = '''      const [idx, size] = key.split('|');
      const id = variants[Number(idx)] && variants[Number(idx)][size];'''
    check_new = '''      const parts = key.split('|');
      const idx = parts[0];
      const size = parts[parts.length - 1];
      const colorIdx = parts.length === 3 ? parts[1] : 0;
      const id = variants[Number(idx)] && variants[Number(idx)][colorIdx] && variants[Number(idx)][colorIdx][size];'''
    html = html.replace(check_old, check_new)

    # 8. Update bag logic (lines) in HTML/JS
    bag_total_old = '''      bagTotal: this.rupees(bagEntries.reduce((t, [k, qty]) => t + cat[Number(k.split('|')[0])][1] * qty, 0)),'''
    bag_total_new = '''      bagTotal: this.rupees(bagEntries.reduce((t, [k, qty]) => t + cat[Number(k.split('|')[0])][1] * qty, 0)),'''
    # Wait, bagTotal is fine as is.
    
    # 9. Find bagItems logic in state mapping
    # Actually wait, how are bag items rendered in the cart sidebar? Let's check `bagLines`
    lines_old = '''      bagLines: bagEntries.map(([k, qty]) => {
        const [idx, size] = k.split('|');
        const c = cat[Number(idx)];'''
        
    lines_new = '''      bagLines: bagEntries.map(([k, qty]) => {
        const parts = k.split('|');
        const idx = parts[0];
        const size = parts[parts.length - 1];
        const colorIdx = parts.length === 3 ? parts[1] : 0;
        const c = cat[Number(idx)];
        const colorName = (c[5] && c[5][colorIdx]) ? c[5][colorIdx].name : '';
        const imgFront = (c[5] && c[5][colorIdx] && c[5][colorIdx].front) ? c[5][colorIdx].front : c[3];'''
    html = html.replace(lines_old, lines_new)
    
    # Replace in bagItems rendering logic where it uses `c[3]` -> `imgFront`
    # Let's just fix it locally in `bagLines`:
    bag2_old = '''        return {
          key: k, name: c[0], size, qty, price: this.rupees(c[1]), img: c[3],'''
    bag2_new = '''        return {
          key: k, name: c[0], size: colorName ? (colorName + ' / ' + size) : size, qty, price: this.rupees(c[1]), img: imgFront,'''
    html = html.replace(bag2_old, bag2_new)

    with io.open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("Patched index.html")

if __name__ == '__main__':
    run()
