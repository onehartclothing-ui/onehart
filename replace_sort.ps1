$content = Get-Content -Raw "C:\Users\Tirth Rathod\onehart- main\index.html"

$search1 = "          open: (e) => { e.preventDefault(); window.scrollTo(0, 0); this.setState({ page: 'pdp', pdp: i, view: 0, size: null, scale: 1, rotY: 0, tx: 0, ty: 0 }); }`r`n        })).filter((p, mappedIdx) => {"
$replace1 = "          open: (e) => { e.preventDefault(); window.scrollTo(0, 0); this.setState({ page: 'pdp', pdp: i, view: 0, size: null, scale: 1, rotY: 0, tx: 0, ty: 0 }); },`r`n          origIdx: i`r`n        })).filter((p, mappedIdx) => {"

$search2 = "          return q.split(/\s+/).every((term) => searchString.includes(term));`r`n        }),"
$replace2 = "          return q.split(/\s+/).every((term) => searchString.includes(term));`r`n        }).sort((a, b) => {`r`n          const order = [0, 1, 2, 3, 4, 5, 9, 10, 6, 7, 8];`r`n          return order.indexOf(a.origIdx) - order.indexOf(b.origIdx);`r`n        }),"

$content = $content.Replace($search1, $replace1)
$content = $content.Replace($search2, $replace2)

Set-Content -NoNewline -Path "C:\Users\Tirth Rathod\onehart- main\index.html" -Value $content
Write-Host "Replacements completed."
