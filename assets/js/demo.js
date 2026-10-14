/* Homepage v1: the hero's replenishment tool. Sample numbers only.
   As it comes: one lever (coverage). Tailored: coverage, a shared capital pool and sales pace,
   with the brand's container rule applied. */
(function () {
  var RATE = 180;          // units sold per day, sample
  var PIPELINE = 6000;     // units already on hand and inbound, sample
  var COST = 4.6;          // landed cost per unit, sample
  var CASE = 50;           // case pack
  var CONTAINER = 2600;    // units per 40-ft container, sample
  var LANDS = Date.UTC(2027, 0, 22);
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  var $ = function (id) { return document.getElementById(id); };
  var num = function (n) { return Math.round(n).toLocaleString('en-US'); };
  var money = function (n) {
    var k = n / 1000;
    return '$' + k.toFixed(1) + 'k';
  };
  var day = function (offset) {
    var d = new Date(LANDS + offset * 864e5);
    return MONTHS[d.getUTCMonth()] + ' ' + d.getUTCDate();
  };

  var a = $('a-cover');
  if (a) {
    var renderA = function () {
      var cover = +a.value;
      var units = Math.max(0, Math.ceil((RATE * cover - PIPELINE) / CASE) * CASE);
      $('a-cover-out').textContent = cover + ' days';
      $('a-units').textContent = num(units);
      $('a-cap').textContent = money(units * COST);
      $('a-until').textContent = day(cover);
    };
    a.addEventListener('input', renderA);
    renderA();
  }

  var bc = $('b-cover'), bp = $('b-pool'), bs = $('b-pace');
  if (bc && bp && bs) {
    var renderB = function () {
      var cover = +bc.value, pool = +bp.value * 1000, pace = +bs.value;
      var rate = RATE * (1 + pace / 100);
      var need = Math.max(0, Math.ceil((rate * cover - PIPELINE) / CONTAINER) * CONTAINER);
      var fundable = Math.floor(pool / COST / CONTAINER) * CONTAINER;
      var funded = Math.min(need, fundable);
      var shortUnits = need - funded;
      var shortCap = shortUnits * COST;
      $('b-cover-out').textContent = cover + ' days';
      $('b-pool-out').textContent = '$' + bp.value + 'k';
      $('b-pace-out').textContent = (pace > 0 ? '+' : '') + pace + '%';
      $('b-need').textContent = money(need * COST);
      $('b-need-units').textContent = num(need) + ' units';
      $('b-fund').textContent = money(funded * COST);
      $('b-short').textContent = num(shortUnits);
      var tile = $('b-fund-tile'), badge = $('b-badge');
      if (shortUnits > 0) {
        var cut = shortUnits / CONTAINER;
        badge.textContent = money(shortCap) + ' short · ' + cut + (cut === 1 ? ' container' : ' containers') + ' cut';
        tile.classList.add('sp-kpi-alert');
      } else {
        badge.textContent = 'Fully funded';
        tile.classList.remove('sp-kpi-alert');
      }
    };
    [bc, bp, bs].forEach(function (el) { el.addEventListener('input', renderB); });
    renderB();
  }
})();
