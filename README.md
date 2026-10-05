# Travelio – optimalizovaná verze

Web fiktivní cestovní agentury Travelio po optimalizaci (kapitoly 4–6).

Hlavní změny: obrázky převedené do WebP a zmenšené na skutečně zobrazovanou velikost,
lazy loading karet, `srcset` + `fetchpriority` u hero obrázku, sémantické HTML (`header`, `main`,
`section`, `article`, `footer`, jeden `h1`), sloučené a vyčištěné CSS bez inline stylů,
JavaScript načítaný přes `defer`.

Původní web: https://paukner.github.io/travelio/

## Spuštění lokálně

```bash
python server.py
```

Poté otevřete `http://localhost:8000`.