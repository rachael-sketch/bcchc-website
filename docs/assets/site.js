/* Black Canyon Community Health Center — small helpers. No tracking, no cookies. */
(function () {
  // Clinic hours in Arizona time (America/Phoenix, no daylight saving). 0 = Sunday.
  var HOURS = {
    "black-canyon":  { 1: [8, 17], 2: [9, 19], 3: [8, 17], 4: [9, 19], 5: [8, 15] },
    "spring-valley": { 1: [8, 17], 2: [8, 17], 3: [8, 19], 4: [8, 17], 5: [8, 15] }
  };
  var DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

  function azNow() {
    try {
      var parts = new Intl.DateTimeFormat("en-US", { timeZone: "America/Phoenix", weekday: "short", hour: "numeric", minute: "numeric", hour12: false }).formatToParts(new Date());
      var map = {}; parts.forEach(function (p) { map[p.type] = p.value; });
      var day = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].indexOf(map.weekday);
      var h = parseInt(map.hour, 10) % 24, m = parseInt(map.minute, 10);
      return { day: day, mins: h * 60 + m };
    } catch (e) { var d = new Date(); return { day: d.getDay(), mins: d.getHours() * 60 + d.getMinutes() }; }
  }
  function fmt(h) { var s = h >= 12 ? " pm" : " am"; var x = h % 12 || 12; return x + s; }

  var now = azNow();
  document.querySelectorAll("[data-status]").forEach(function (el) {
    var site = HOURS[el.getAttribute("data-status")]; if (!site) return;
    var today = site[now.day];
    if (today && now.mins >= today[0] * 60 && now.mins < today[1] * 60) {
      el.className = "status open"; el.textContent = "Open today until " + fmt(today[1]);
    } else {
      var next = null;
      if (today && now.mins < today[0] * 60) next = "today at " + fmt(today[0]);
      for (var i = 1; !next && i < 8; i++) { var d = (now.day + i) % 7; if (site[d]) next = (i === 1 ? "tomorrow" : DAYS[d]) + " at " + fmt(site[d][0]); }
      el.className = "status later"; el.textContent = "Opens " + next;
    }
  });
  document.querySelectorAll(".hours tr[data-day]").forEach(function (tr) {
    if (parseInt(tr.getAttribute("data-day"), 10) === now.day) tr.classList.add("is-today");
  });

  // Sliding fee estimate — 2026 BCCHC scale (100% FPG = $15,960 + $5,680 per added person).
  var calc = document.getElementById("sfdp-calc");
  if (calc) {
    var size = document.getElementById("sfdp-size"), income = document.getElementById("sfdp-income"), out = document.getElementById("sfdp-result");
    var TIERS = [
      { pct: 1.00, name: "A", pc: "$20", lab: "$10" },
      { pct: 1.25, name: "B", pc: "$25", lab: "$10 + 20% of the lab charge" },
      { pct: 1.50, name: "C", pc: "$30", lab: "$10 + 40% of the lab charge" },
      { pct: 1.75, name: "D", pc: "$35", lab: "$10 + 60% of the lab charge" },
      { pct: 2.00, name: "E", pc: "$40", lab: "$10 + 80% of the lab charge" }
    ];
    function money(n) { return "$" + Math.round(n).toLocaleString("en-US"); }
    function update() {
      var n = parseInt(size.value, 10) || 1;
      var raw = (income.value || "").replace(/[^0-9.]/g, "");
      var base = 15960 + 5680 * (n - 1);
      if (raw === "") {
        out.innerHTML = '<span class="tier">Enter your household income</span><span class="fee">For a household of ' + n + ", the program covers yearly income up to <strong>" + money(base * 2) + "</strong>.</span>";
        return;
      }
      var inc = parseFloat(raw);
      for (var i = 0; i < TIERS.length; i++) {
        if (inc <= Math.round(base * TIERS[i].pct)) {
          var t = TIERS[i];
          out.innerHTML = '<span class="tier">You may qualify for discount level ' + t.name + "</span>" +
            '<span class="fee">Primary care visit: <strong>' + t.pc + "</strong> · Lab: <strong>" + t.lab + "</strong></span>";
          return;
        }
      }
      out.innerHTML = '<span class="tier">Above the sliding fee range</span><span class="fee">The program covers income up to ' + money(base * 2) + " for a household of " + n + ". Our front desk can still help you find coverage, including AHCCCS.</span>";
    }
    size.addEventListener("change", update); income.addEventListener("input", update);
    calc.addEventListener("submit", function (e) { e.preventDefault(); update(); });
    update();
  }
})();
