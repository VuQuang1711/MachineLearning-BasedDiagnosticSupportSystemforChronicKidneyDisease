/**
 * static/js/app.js
 * HUIT HOSPITAL CLINICAL PORTAL — HỆ THỐNG QUẢN LÝ BỆNH VIỆN & TRỰC QUAN HÓA BIỂU ĐỒ AI
 * Bệnh Viện Đại Học Công Thương TP.HCM
 */

document.addEventListener("DOMContentLoaded", () => {
  // ==========================================
  // 1. DANH SÁCH BỆNH NHÂN TIẾP NHẬN TRONG NGÀY
  // ==========================================
  const PATIENT_DATABASE = [
    {
      mrn: "BN-2026-0841",
      name: "Trần Văn Hùng",
      age: 62,
      gender: "male",
      bhyt: "GD 4 79 0123456789",
      bed: "Phòng 302 - Giường 05",
      contact: "Tân Phú, TP.HCM • 0918.xxx.789",
      doctor: "BS. Vũ Thế Quang",
      symptoms: "Tăng huyết áp 10 năm, phù 2 chi dưới, mệt mỏi, tiểu đêm",
      status: "critical",
      statusText: "⚠️ Nguy cơ G4",
      egfrEst: "21.8 mL/phút",
      labData: {
        age: 62, bp: 85, sc: 3.2, bu: 58.0, bgr: 155.0, hemo: 9.5, pcv: 30, sod: 135.0, pot: 4.8, wc: 9200, rc: 3.4,
        sg: "1.010", al: "3.0", su: "1.0", rbc: "abnormal", pc: "abnormal", pcc: "notpresent", ba: "notpresent",
        htn: "yes", dm: "yes", cad: "no", appet: "poor", pe: "yes", ane: "yes"
      }
    },
    {
      mrn: "BN-2026-0842",
      name: "Lê Thị Mai",
      age: 48,
      gender: "female",
      bhyt: "DN 4 79 0987654321",
      bed: "Khám Ngoại Trú - P.102",
      contact: "Bình Tân, TP.HCM • 0903.xxx.112",
      doctor: "BS. Triệu Thị Thu Ngân",
      symptoms: "Đái tháo đường Type 2 trên 8 năm, mờ mắt, khát nước, sụt cân",
      status: "waiting",
      statusText: "⏳ Chờ Hội Chẩn",
      egfrEst: "42.5 mL/phút",
      labData: {
        age: 48, bp: 80, sc: 1.8, bu: 38.0, bgr: 190.0, hemo: 11.2, pcv: 35, sod: 138.0, pot: 4.2, wc: 7800, rc: 4.1,
        sg: "1.015", al: "2.0", su: "2.0", rbc: "normal", pc: "normal", pcc: "notpresent", ba: "notpresent",
        htn: "yes", dm: "yes", cad: "no", appet: "good", pe: "no", ane: "no"
      }
    },
    {
      mrn: "BN-2026-0843",
      name: "Nguyễn Hoàng Nam",
      age: 34,
      gender: "male",
      bhyt: "CN 4 79 0555666777",
      bed: "Khám Sức Khỏe - P.205",
      contact: "Tân Bình, TP.HCM • 0972.xxx.445",
      doctor: "BS. Nguyễn Đình Bảo Tấn",
      symptoms: "Khám sức khỏe định kỳ doanh nghiệp, thể trạng tốt, không tiền sử bệnh",
      status: "analyzed",
      statusText: "✓ Khỏe Mạnh (G1)",
      egfrEst: "105.0 mL/phút",
      labData: {
        age: 34, bp: 70, sc: 0.9, bu: 24.0, bgr: 95.0, hemo: 15.2, pcv: 46, sod: 142.0, pot: 4.1, wc: 6500, rc: 5.1,
        sg: "1.020", al: "0.0", su: "0.0", rbc: "normal", pc: "normal", pcc: "notpresent", ba: "notpresent",
        htn: "no", dm: "no", cad: "no", appet: "good", pe: "no", ane: "no"
      }
    },
    {
      mrn: "BN-2026-0844",
      name: "Phạm Thị Cúc",
      age: 73,
      gender: "female",
      bhyt: "HT 4 79 0111222333",
      bed: "Cấp Cứu Lọc Máu - G.01",
      contact: "Quận 12, TP.HCM • 0938.xxx.998",
      doctor: "BS. Nguyễn Thanh Nhàn",
      symptoms: "Hội chứng Ure huyết cao, khó thở khi nằm, phù toàn thân, vô niệu",
      status: "critical",
      statusText: "🚨 Suy Thận G5",
      egfrEst: "9.2 mL/phút",
      labData: {
        age: 73, bp: 90, sc: 6.8, bu: 112.0, bgr: 145.0, hemo: 7.6, pcv: 24, sod: 130.0, pot: 5.6, wc: 11500, rc: 2.8,
        sg: "1.005", al: "4.0", su: "1.0", rbc: "abnormal", pc: "abnormal", pcc: "present", ba: "notpresent",
        htn: "yes", dm: "yes", cad: "yes", appet: "poor", pe: "yes", ane: "yes"
      }
    },
    {
      mrn: "BN-2026-0845",
      name: "Vũ Đình Trọng",
      age: 56,
      gender: "male",
      bhyt: "DN 4 79 0333444555",
      bed: "Phòng 305 - Giường 08",
      contact: "Gò Vấp, TP.HCM • 0988.xxx.321",
      doctor: "BS. Võ Tấn Đạt",
      symptoms: "Tăng huyết áp vô căn độ 2, đau đầu vùng chẩm, chán ăn nhẹ",
      status: "waiting",
      statusText: "⏳ Chờ Hội Chẩn",
      egfrEst: "64.2 mL/phút",
      labData: {
        age: 56, bp: 85, sc: 1.4, bu: 36.0, bgr: 118.0, hemo: 13.0, pcv: 39, sod: 139.0, pot: 4.4, wc: 7200, rc: 4.4,
        sg: "1.015", al: "1.0", su: "0.0", rbc: "normal", pc: "normal", pcc: "notpresent", ba: "notpresent",
        htn: "yes", dm: "no", cad: "no", appet: "poor", pe: "no", ane: "no"
      }
    }
  ];

  // ==========================================
  // 2. DOM ELEMENTS
  // ==========================================
  const form = document.getElementById("ckdForm");
  const btnSubmit = document.getElementById("btnSubmit");
  const btnReset = document.getElementById("btnReset");
  const btnFillSampleTop = document.getElementById("btnFillSampleTop");
  const btnFillSampleQuick = document.getElementById("btnFillSampleQuick");
  const btnFillHealthyQuick = document.getElementById("btnFillHealthyQuick");

  // KPI Card Elements
  const kpiProbVal = document.getElementById("kpiProbVal");
  const kpiProbSub = document.getElementById("kpiProbSub");
  const kpiEgfrVal = document.getElementById("kpiEgfrVal");
  const kpiEgfrSub = document.getElementById("kpiEgfrSub");
  const kpiRankVal = document.getElementById("kpiRankVal");
  const kpiStatusPill = document.getElementById("kpiStatusPill");

  // Result Box Elements
  const emptyResultBox = document.getElementById("emptyResultBox");
  const activeResultBox = document.getElementById("activeResultBox");
  const mainResultBanner = document.getElementById("mainResultBanner");
  const bannerIcon = document.getElementById("bannerIcon");
  const bannerDiagnosisTitle = document.getElementById("bannerDiagnosisTitle");
  const recommendationBody = document.getElementById("recommendationBody");
  const xaiFactorsList = document.getElementById("xaiFactorsList");

  // Gauge Elements
  const gaugePctText = document.getElementById("gaugePctText");
  const gaugeStatusText = document.getElementById("gaugeStatusText");

  // Reference Table Elements
  const refPatientSc = document.getElementById("refPatientSc");
  const refStatusSc = document.getElementById("refStatusSc");
  const refPatientHemo = document.getElementById("refPatientHemo");
  const refStatusHemo = document.getElementById("refStatusHemo");
  const refPatientAl = document.getElementById("refPatientAl");
  const refStatusAl = document.getElementById("refStatusAl");
  const refPatientEgfr = document.getElementById("refPatientEgfr");
  const refStatusEgfr = document.getElementById("refStatusEgfr");

  // Patient Admin Fields
  const displayPatientMRN = document.getElementById("displayPatientMRN");
  const patientName = document.getElementById("patientName");
  const patientGender = document.getElementById("patientGender");
  const patientBHYT = document.getElementById("patientBHYT");
  const patientBed = document.getElementById("patientBed");
  const patientContact = document.getElementById("patientContact");
  const patientDoctor = document.getElementById("patientDoctor");

  // Prescription Elements
  const rxPrescriptionCode = document.getElementById("rxPrescriptionCode");
  const rxMedsList = document.getElementById("rxMedsList");

  // Search & Filter
  const globalSearch = document.getElementById("globalSearch");
  const patientFilterInput = document.getElementById("patientFilterInput");
  const patientQueueTableBody = document.getElementById("patientQueueTableBody");
  const btnRefreshPatients = document.getElementById("btnRefreshPatients");

  // Print buttons
  const sidebarBtnPrint = document.getElementById("sidebarBtnPrint");
  const topbarBtnPrint = document.getElementById("topbarBtnPrint");
  const btnOpenPrint = document.getElementById("btnOpenPrint");

  // Modal Lightbox
  const imageLightboxModal = document.getElementById("imageLightboxModal");
  const lightboxModalTitle = document.getElementById("lightboxModalTitle");
  const lightboxModalImg = document.getElementById("lightboxModalImg");
  const btnCloseLightbox = document.getElementById("btnCloseLightbox");

  // Benchmark Elements
  const benchmarkTableBody = document.getElementById("benchmarkTableBody");
  const statNormalBadge = document.getElementById("statNormalBadge");
  const statAbnormalBadge = document.getElementById("statAbnormalBadge");
  const benchFilterBtns = document.querySelectorAll(".btn-bench-filter");
  let currentBenchFilter = "all";
  let lastFeatureComparisons = [];

  // ==========================================
  // 3. KHỞI TẠO BIỂU ĐỒ CHART.JS (GLOBAL INSTANCES)
  // ==========================================
  let riskGaugeChart = null;
  let biomarkerRadarChart = null;
  let modelsComparisonChart = null;
  let featureImportanceChart = null;

  // Dữ liệu hiệu năng 6 mô hình thực tế từ Benchmark
  const MODELS_DATA = {
    labels: [
      "Random Forest (ML-RF)",
      "SVM RBF (ML-SVM)",
      "Logistic Reg (ML-LR)",
      "Naïve Bayes (ML-NB)",
      "Decision Tree (ML-DT)",
      "k-NN k=5 (ML-KNN)"
    ],
    recall: [98.0, 98.0, 96.0, 100.0, 94.0, 88.0],
    accuracy: [97.5, 98.75, 97.5, 100.0, 95.0, 92.5],
    f1: [98.0, 98.99, 97.96, 100.0, 95.92, 93.62],
    roc_auc: [99.87, 99.93, 99.87, 100.0, 93.90, 98.87]
  };

  // Top 10 Feature Importance trích xuất từ Random Forest
  const FEATURE_IMPORTANCE_DATA = {
    labels: [
      "Creatinine huyết thanh (sc)",
      "Huyết sắc tố (hemo)",
      "Albumin nước tiểu (al)",
      "Dung tích hồng cầu (pcv)",
      "Hồng cầu máu (rc)",
      "Đường huyết đói (bgr)",
      "Urê máu (bu)",
      "Huyết áp khám (bp)",
      "Tỷ trọng nước tiểu (sg)",
      "Tăng huyết áp (htn)"
    ],
    values: [25.4, 21.2, 18.6, 8.5, 6.2, 5.1, 4.3, 3.8, 3.5, 3.4]
  };

  // 3.1. Khởi tạo Đồng Hồ Đo Nguy Cơ (Half Gauge)
  function initRiskGaugeChart() {
    const canvas = document.getElementById("riskGaugeCanvas");
    if (!canvas || !window.Chart) return;
    if (riskGaugeChart) {
      riskGaugeChart.destroy();
    }

    riskGaugeChart = new Chart(canvas, {
      type: "doughnut",
      data: {
        labels: ["Xác suất CKD", "Ngưỡng an toàn"],
        datasets: [{
          data: [0, 100],
          backgroundColor: ["#10b981", "#e2e8f0"],
          borderWidth: 0,
          cutout: "75%",
          circumference: 180,
          rotation: 270,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { enabled: false }
        },
        animation: {
          animateRotate: true,
          duration: 1200
        }
      }
    });
  }

  // 3.2. Khởi tạo Biểu Đồ Radar Đa Chiều Sinh Hóa
  function initBiomarkerRadarChart() {
    const canvas = document.getElementById("biomarkerRadarCanvas");
    if (!canvas || !window.Chart) return;
    if (biomarkerRadarChart) {
      biomarkerRadarChart.destroy();
    }

    biomarkerRadarChart = new Chart(canvas, {
      type: "radar",
      data: {
        labels: [
          "Creatinine (sc)",
          "Huyết sắc tố (hemo)",
          "Albumin (al)",
          "Huyết áp (bp)",
          "Đường huyết (bgr)",
          "Urê máu (bu)"
        ],
        datasets: [
          {
            label: "Chuẩn An Toàn",
            data: [30, 85, 10, 40, 35, 30],
            backgroundColor: "rgba(2, 132, 199, 0.15)",
            borderColor: "rgba(2, 132, 199, 0.8)",
            borderWidth: 2,
            pointRadius: 3,
            pointBackgroundColor: "#0284c7"
          },
          {
            label: "Chỉ Số Bệnh Nhân",
            data: [80, 45, 75, 70, 60, 65],
            backgroundColor: "rgba(220, 38, 38, 0.25)",
            borderColor: "rgba(220, 38, 38, 0.9)",
            borderWidth: 2,
            pointRadius: 4,
            pointBackgroundColor: "#dc2626"
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          r: {
            angleLines: { color: "rgba(0, 0, 0, 0.08)" },
            grid: { color: "rgba(0, 0, 0, 0.08)" },
            pointLabels: {
              font: { size: 10, weight: "bold" },
              color: "#334155"
            },
            ticks: { display: false, max: 100, min: 0 }
          }
        },
        plugins: {
          legend: { display: false }
        },
        animation: {
          duration: 1200
        }
      }
    });
  }

  // 3.3. Khởi tạo Biểu Đồ So Sánh 6 Mô Hình ML
  function initModelsComparisonChart() {
    const canvas = document.getElementById("modelsComparisonCanvas");
    if (!canvas || !window.Chart) return;

    modelsComparisonChart = new Chart(canvas, {
      type: "bar",
      data: {
        labels: MODELS_DATA.labels,
        datasets: [{
          label: "Recall (Độ nhạy Y tế %)",
          data: MODELS_DATA.recall,
          backgroundColor: [
            "rgba(29, 78, 216, 0.9)", // RF (Đậm nhất - best)
            "rgba(59, 130, 246, 0.7)",
            "rgba(96, 165, 250, 0.7)",
            "rgba(52, 211, 153, 0.7)",
            "rgba(251, 191, 36, 0.7)",
            "rgba(248, 113, 113, 0.7)"
          ],
          borderColor: [
            "#1d4ed8",
            "#3b82f6",
            "#60a5fa",
            "#10b981",
            "#f59e0b",
            "#ef4444"
          ],
          borderWidth: 1.5,
          borderRadius: 6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: false,
            min: 80,
            max: 102,
            ticks: {
              callback: (val) => `${val}%`,
              font: { size: 11 }
            },
            grid: { color: "rgba(0, 0, 0, 0.05)" }
          },
          x: {
            ticks: { font: { size: 11, weight: "600" } },
            grid: { display: false }
          }
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: (ctx) => ` ${ctx.dataset.label}: ${ctx.raw}%`
            }
          }
        }
      }
    });
  }

  // 3.4. Khởi tạo Biểu Đồ Feature Importance (Horizontal Bar)
  function initFeatureImportanceChart() {
    const canvas = document.getElementById("featureImportanceCanvas");
    if (!canvas || !window.Chart) return;

    featureImportanceChart = new Chart(canvas, {
      type: "bar",
      data: {
        labels: FEATURE_IMPORTANCE_DATA.labels,
        datasets: [{
          label: "Mức độ quan trọng Gini (%)",
          data: FEATURE_IMPORTANCE_DATA.values,
          backgroundColor: [
            "#d97706", // Top 1: sc (Gold)
            "#f59e0b", // Top 2: hemo (Gold)
            "#fbbf24", // Top 3: al (Gold)
            "#2563eb",
            "#3b82f6",
            "#60a5fa",
            "#93c5fd",
            "#bfdbfe",
            "#cbd5e1",
            "#e2e8f0"
          ],
          borderRadius: 4
        }]
      },
      options: {
        indexAxis: "y",
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            beginAtZero: true,
            max: 30,
            ticks: { callback: (val) => `${val}%` },
            grid: { color: "rgba(0, 0, 0, 0.05)" }
          },
          y: {
            ticks: { font: { size: 11, weight: "600" } },
            grid: { display: false }
          }
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: (ctx) => ` Tỷ trọng: ${ctx.raw}%`
            }
          }
        }
      }
    });
  }

  // Cập nhật biểu đồ Gauge và Radar theo dữ liệu bệnh nhân
  function updateVisualCharts(probPct, isCKD, payload) {
    // 1. Cập nhật Gauge Chart
    if (riskGaugeChart) {
      const riskVal = parseFloat(probPct);
      const safeVal = Math.max(0, 100 - riskVal);
      riskGaugeChart.data.datasets[0].data = [riskVal, safeVal];

      // Đổi màu theo độ rủi ro
      let gaugeColor = "#10b981"; // Xanh
      let statusLabel = "Bình Thường";
      let statusColor = "#16a34a";

      if (riskVal >= 70) {
        gaugeColor = "#dc2626"; // Đỏ
        statusLabel = "Nguy Cơ Cao";
        statusColor = "#dc2626";
      } else if (riskVal >= 30) {
        gaugeColor = "#d97706"; // Vàng cam
        statusLabel = "Nguy Cơ Vừa";
        statusColor = "#d97706";
      }

      riskGaugeChart.data.datasets[0].backgroundColor = [gaugeColor, "#e2e8f0"];
      riskGaugeChart.update();

      if (gaugePctText) gaugePctText.textContent = `${probPct}%`;
      if (gaugeStatusText) {
        gaugeStatusText.textContent = statusLabel;
        gaugeStatusText.style.color = statusColor;
        gaugeStatusText.style.backgroundColor = `${statusColor}15`;
      }
    }

    // 2. Cập nhật Radar Chart (Chuẩn hóa 6 chỉ số về thang điểm 0 - 100)
    if (biomarkerRadarChart) {
      const sc = parseFloat(payload.sc || 1.0);
      const hemo = parseFloat(payload.hemo || 15.0);
      const al = parseFloat(payload.al || 0.0);
      const bp = parseFloat(payload.bp || 80.0);
      const bgr = parseFloat(payload.bgr || 100.0);
      const bu = parseFloat(payload.bu || 30.0);

      // Công thức chuẩn hóa trực quan
      const scoreSc = Math.min(100, Math.max(10, (sc / 4.0) * 100));
      const scoreHemo = Math.min(100, Math.max(10, ((16.0 - Math.min(hemo, 16.0)) / 10.0) * 100)); // Hemo càng thấp càng nguy
      const scoreAl = Math.min(100, Math.max(10, (al / 4.0) * 100));
      const scoreBp = Math.min(100, Math.max(15, ((bp - 60) / 100.0) * 100));
      const scoreBgr = Math.min(100, Math.max(15, ((bgr - 70) / 180.0) * 100));
      const scoreBu = Math.min(100, Math.max(15, (bu / 100.0) * 100));

      biomarkerRadarChart.data.datasets[1].data = [
        scoreSc,
        scoreHemo,
        scoreAl,
        scoreBp,
        scoreBgr,
        scoreBu
      ];

      if (isCKD) {
        biomarkerRadarChart.data.datasets[1].backgroundColor = "rgba(220, 38, 38, 0.3)";
        biomarkerRadarChart.data.datasets[1].borderColor = "rgba(220, 38, 38, 0.95)";
      } else {
        biomarkerRadarChart.data.datasets[1].backgroundColor = "rgba(16, 185, 129, 0.25)";
        biomarkerRadarChart.data.datasets[1].borderColor = "rgba(16, 185, 129, 0.9)";
      }

      biomarkerRadarChart.update();
    }
  }

  // Khởi động toàn bộ biểu đồ
  initRiskGaugeChart();
  initBiomarkerRadarChart();
  initModelsComparisonChart();
  initFeatureImportanceChart();

  // ==========================================
  // 4. XỬ LÝ CHUYỂN TAB TRUNG TÂM BIỂU ĐỒ (ANALYTICS HUB)
  // ==========================================
  const hubTabButtons = document.querySelectorAll(".hub-tab-btn");
  const hubTabContents = document.querySelectorAll(".hub-tab-content");

  hubTabButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      hubTabButtons.forEach(b => b.classList.remove("active"));
      hubTabContents.forEach(c => c.classList.remove("active"));

      btn.classList.add("active");
      const targetId = btn.getAttribute("data-tab");
      const targetContent = document.getElementById(targetId);
      if (targetContent) targetContent.classList.add("active");
    });
  });

  // Chuyển tiêu chí đánh giá mô hình (Recall, Accuracy, F1, ROC-AUC)
  const metricFilterBtns = document.querySelectorAll(".metric-filter-btn");
  metricFilterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      metricFilterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      const metric = btn.getAttribute("data-metric");
      let dataArr = MODELS_DATA.recall;
      let labelText = "Recall (Độ nhạy Y tế %)";

      if (metric === "accuracy") {
        dataArr = MODELS_DATA.accuracy;
        labelText = "Accuracy (Độ chính xác %)";
      } else if (metric === "f1") {
        dataArr = MODELS_DATA.f1;
        labelText = "F1-Score (%)";
      } else if (metric === "roc_auc") {
        dataArr = MODELS_DATA.roc_auc;
        labelText = "ROC-AUC (Quy đổi %)";
      }

      if (modelsComparisonChart) {
        modelsComparisonChart.data.datasets[0].label = labelText;
        modelsComparisonChart.data.datasets[0].data = dataArr;
        modelsComparisonChart.update();
      }
    });
  });

  // ==========================================
  // 5. LIGHTBOX MODAL CHO THƯ VIỆN ĐỒ THỊ
  // ==========================================
  const galleryCards = document.querySelectorAll(".gallery-card");
  galleryCards.forEach(card => {
    card.addEventListener("click", () => {
      const imgSrc = card.getAttribute("data-img");
      const title = card.getAttribute("data-title");

      if (lightboxModalImg && lightboxModalTitle && imageLightboxModal) {
        lightboxModalImg.src = imgSrc;
        lightboxModalTitle.textContent = title;
        imageLightboxModal.classList.remove("hidden");
      }
    });
  });

  if (btnCloseLightbox) {
    btnCloseLightbox.addEventListener("click", () => {
      if (imageLightboxModal) imageLightboxModal.classList.add("hidden");
    });
  }

  if (imageLightboxModal) {
    imageLightboxModal.addEventListener("click", (e) => {
      if (e.target === imageLightboxModal) {
        imageLightboxModal.classList.add("hidden");
      }
    });
  }

  // Benchmark filter tabs event listeners
  benchFilterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      benchFilterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      currentBenchFilter = btn.getAttribute("data-benchfilter");
      renderBenchmarkTable(lastFeatureComparisons, currentBenchFilter);
    });
  });

  // Render bảng đối chiếu 24 chỉ số lâm sàng với khoảng chuẩn người bình thường
  function renderBenchmarkTable(comparisons, filterMode = "all") {
    if (!benchmarkTableBody || !comparisons || comparisons.length === 0) return;
    benchmarkTableBody.innerHTML = "";

    // Thống kê số lượng chỉ số chuẩn vs lệch chuẩn
    const normalCount = comparisons.filter(c => c.status === "normal").length;
    const abnormalCount = comparisons.length - normalCount;

    if (statNormalBadge) statNormalBadge.textContent = `✓ ${normalCount}/24 Đạt Chuẩn`;
    if (statAbnormalBadge) statAbnormalBadge.textContent = `⚠️ ${abnormalCount}/24 Lệch Chuẩn`;

    // Lọc danh sách theo tab
    let filtered = comparisons;
    if (filterMode === "abnormal") {
      filtered = comparisons.filter(c => c.status !== "normal");
    } else if (filterMode === "normal") {
      filtered = comparisons.filter(c => c.status === "normal");
    }

    if (filtered.length === 0) {
      benchmarkTableBody.innerHTML = `
        <tr>
          <td colspan="7" style="text-align: center; padding: 20px; color: #64748b;">
            Không có chỉ số nào trong bộ lọc này.
          </td>
        </tr>
      `;
      return;
    }

    filtered.forEach(c => {
      const tr = document.createElement("tr");

      let valClass = "val-success";
      let markerClass = "marker-success";
      let devText = `${c.deviation_pct > 0 ? "+" : ""}${c.deviation_pct}%`;
      let devColor = "#16a34a";

      if (c.status === "high") {
        valClass = "val-danger";
        markerClass = "marker-danger";
        devColor = "#dc2626";
      } else if (c.status === "low") {
        valClass = "val-warning";
        markerClass = "marker-warning";
        devColor = "#d97706";
      } else if (c.status === "abnormal") {
        valClass = "val-danger";
        markerClass = "marker-danger";
        devText = "Lệch Chuẩn";
        devColor = "#dc2626";
      } else {
        devText = "Chuẩn 0.0%";
      }

      // Thanh đo trực quan dạng Bullet Range Bar
      let rangeBarHtml = "";
      if (c.type === "numerical") {
        const val = parseFloat(c.patient_val || 0);
        const nMin = c.normal_min;
        const nMax = c.normal_max;
        const span = Math.max(0.01, nMax - nMin);

        const dMin = Math.max(0, nMin - span * 0.8);
        const dMax = Math.max(val * 1.15, nMax + span * 1.5);
        const totalSpan = Math.max(0.01, dMax - dMin);

        const zoneLeft = Math.max(0, Math.min(100, ((nMin - dMin) / totalSpan) * 100));
        const zoneWidth = Math.max(5, Math.min(100 - zoneLeft, ((nMax - nMin) / totalSpan) * 100));
        const markerPos = Math.max(2, Math.min(98, ((val - dMin) / totalSpan) * 100));

        rangeBarHtml = `
          <div class="range-bar-track" title="Giá trị: ${val} (Chuẩn: ${nMin} - ${nMax})">
            <div class="range-bar-normal-zone" style="left: ${zoneLeft.toFixed(1)}%; width: ${zoneWidth.toFixed(1)}%;"></div>
            <div class="range-bar-marker ${markerClass}" style="left: ${markerPos.toFixed(1)}%;"></div>
          </div>
        `;
      } else {
        const isNorm = c.status === "normal";
        rangeBarHtml = `
          <div class="range-bar-track">
            <div class="range-bar-normal-zone" style="left: 0; width: 100%; background-color: ${isNorm ? "#bbf7d0" : "#fecaca"};"></div>
            <div class="range-bar-marker ${markerClass}" style="left: ${isNorm ? "50%" : "85%"};"></div>
          </div>
        `;
      }

      const goldenBadge = c.is_golden ? `<span class="gold-star" title="Chỉ số vàng chẩn đoán CKD">★ Vàng</span>` : "";

      tr.innerHTML = `
        <td>
          <span class="bench-feature-name">${c.name}</span>
          ${goldenBadge}
          <span class="bench-feature-key">(${c.key})</span>
        </td>
        <td>
          <span class="patient-val-strong ${valClass}">${c.display_val}</span>
        </td>
        <td>
          <code>${c.normal_text}</code>
        </td>
        <td>
          <strong style="color: ${devColor}; font-size: 11.5px;">${devText}</strong>
        </td>
        <td>
          ${rangeBarHtml}
        </td>
        <td>
          <span class="${c.badge}">${c.status_text.split(" (")[0]}</span>
        </td>
        <td>
          <small style="color: #64748b; font-size: 11px;">${c.desc}</small>
        </td>
      `;

      benchmarkTableBody.appendChild(tr);
    });
  }

  // Tô màu viền và đánh dấu trực quan ngay trên 24 ô input của form khám bệnh
  function highlightFormInputsWithBenchmark(comparisons) {
    if (!comparisons || comparisons.length === 0) return;
    comparisons.forEach(c => {
      const el = document.getElementById(c.key);
      if (!el) return;
      el.classList.remove("input-deviated-high", "input-deviated-low", "input-deviated-normal");
      if (c.status === "high") {
        el.classList.add("input-deviated-high");
      } else if (c.status === "low") {
        el.classList.add("input-deviated-low");
      } else if (c.status === "normal") {
        el.classList.add("input-deviated-normal");
      } else if (c.status === "abnormal") {
        el.classList.add("input-deviated-high");
      }
    });
  }

  // ==========================================
  // 6. RENDER DANH SÁCH BỆNH NHÂN TIẾP NHẬN
  // ==========================================
  function renderPatientTable(filterQuery = "") {
    if (!patientQueueTableBody) return;
    patientQueueTableBody.innerHTML = "";

    const q = filterQuery.trim().toLowerCase();
    const filtered = PATIENT_DATABASE.filter(p => {
      if (!q) return true;
      return p.name.toLowerCase().includes(q) ||
        p.mrn.toLowerCase().includes(q) ||
        p.bhyt.toLowerCase().includes(q) ||
        p.symptoms.toLowerCase().includes(q);
    });

    if (filtered.length === 0) {
      patientQueueTableBody.innerHTML = `
        <tr>
          <td colspan="9" style="text-align: center; padding: 20px; color: #64748b;">
            Không tìm thấy bệnh nhân nào phù hợp với từ khóa "${filterQuery}".
          </td>
        </tr>
      `;
      return;
    }

    filtered.forEach((p) => {
      const tr = document.createElement("tr");

      let badgeClass = "badge-status-waiting";
      if (p.status === "critical") badgeClass = "badge-status-critical";
      if (p.status === "analyzed") badgeClass = "badge-status-analyzed";

      const genderText = p.gender === "male" ? "Nam" : "Nữ";

      tr.innerHTML = `
        <td><span class="mrn-badge">${p.mrn}</span></td>
        <td class="patient-cell-name">${p.name}</td>
        <td>${p.age} tuổi (${genderText})</td>
        <td><code>${p.bhyt}</code></td>
        <td>${p.bed}</td>
        <td style="max-width: 260px;" title="${p.symptoms}">${p.symptoms}</td>
        <td><strong>${p.egfrEst}</strong></td>
        <td><span class="badge-tag-status ${badgeClass}">${p.statusText}</span></td>
        <td>
          <button type="button" class="btn-select-patient" data-mrn="${p.mrn}">
            🩺 Chọn Khám
          </button>
        </td>
      `;

      patientQueueTableBody.appendChild(tr);
    });

    // Wire click events
    patientQueueTableBody.querySelectorAll(".btn-select-patient").forEach(btn => {
      btn.addEventListener("click", () => {
        const mrn = btn.getAttribute("data-mrn");
        loadPatientData(mrn);
      });
    });
  }

  // Nạp toàn bộ dữ liệu hồ sơ bệnh nhân
  function loadPatientData(mrn) {
    const patient = PATIENT_DATABASE.find(p => p.mrn === mrn);
    if (!patient) return;

    // Điền trường hành chính EMR
    if (displayPatientMRN) displayPatientMRN.textContent = patient.mrn;
    if (patientName) patientName.value = patient.name;
    if (patientGender) patientGender.value = patient.gender;
    if (patientBHYT) patientBHYT.value = patient.bhyt;
    if (patientBed) patientBed.value = patient.bed;
    if (patientContact) patientContact.value = patient.contact;
    if (patientDoctor) patientDoctor.value = patient.doctor;

    // Điền 24 chỉ số lâm sàng
    const d = patient.labData;
    for (const key in d) {
      const el = document.getElementById(key);
      if (el) {
        el.value = d[key];
      }
    }

    // Cuộn mượt đến vị trí khám
    const diagSec = document.getElementById("diagnosis-section");
    if (diagSec) {
      diagSec.scrollIntoView({ behavior: "smooth" });
    }

    // Kích hoạt suy luận AI ngay lập tức
    triggerDiagnosis();
  }

  // Khởi tạo bảng danh sách
  renderPatientTable();

  // Tìm kiếm trong bảng
  if (patientFilterInput) {
    patientFilterInput.addEventListener("input", (e) => {
      renderPatientTable(e.target.value);
    });
  }

  if (btnRefreshPatients) {
    btnRefreshPatients.addEventListener("click", () => {
      if (patientFilterInput) patientFilterInput.value = "";
      renderPatientTable();
    });
  }

  // Phím tắt Ctrl + K
  window.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      if (globalSearch) globalSearch.focus();
    }
  });

  if (globalSearch) {
    globalSearch.addEventListener("input", (e) => {
      const val = e.target.value;
      if (patientFilterInput) {
        patientFilterInput.value = val;
      }
      renderPatientTable(val);
    });
  }

  // ==========================================
  // 7. CÁC NÚT NẠP MẪU NHANH
  // ==========================================
  function loadSevereCKD() {
    loadPatientData("BN-2026-0841");
  }

  function loadHealthyCase() {
    loadPatientData("BN-2026-0843");
  }

  if (btnFillSampleTop) btnFillSampleTop.addEventListener("click", loadSevereCKD);
  if (btnFillSampleQuick) btnFillSampleQuick.addEventListener("click", loadSevereCKD);
  if (btnFillHealthyQuick) btnFillHealthyQuick.addEventListener("click", loadHealthyCase);

  // ==========================================
  // 8. GỬI BIỂU MẪU ĐẾN MÁY CHỦ API ML
  // ==========================================
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    triggerDiagnosis();
  });

  // Reset form
  btnReset.addEventListener("click", () => {
    if (emptyResultBox) emptyResultBox.classList.remove("hidden");
    if (activeResultBox) activeResultBox.classList.add("hidden");

    if (kpiProbVal) {
      kpiProbVal.textContent = "0,0%";
      kpiProbVal.className = "kpi-large-num";
    }
    if (kpiProbSub) kpiProbSub.textContent = "Thang đo mô hình Ensemble Random Forest";

    if (kpiEgfrVal) kpiEgfrVal.textContent = "--";
    if (kpiEgfrSub) kpiEgfrSub.textContent = "Đo lường chức năng lọc cầu thận theo MDRD";

    if (kpiRankVal) {
      kpiRankVal.textContent = "Chờ Khám";
      kpiRankVal.className = "kpi-large-num-text text-normal";
    }

    if (kpiStatusPill) {
      kpiStatusPill.textContent = "✓ SẴN SÀNG";
      kpiStatusPill.className = "status-badge-pill pill-neutral";
    }

    // Xóa màu viền đối chiếu của các ô nhập liệu
    document.querySelectorAll(".field-item input, .field-item select").forEach(el => {
      el.classList.remove("input-deviated-high", "input-deviated-low", "input-deviated-normal");
    });
    if (benchmarkTableBody) {
      benchmarkTableBody.innerHTML = `
        <tr>
          <td colspan="7" style="text-align: center; padding: 24px; color: #64748b;">
            Hệ thống chưa có dữ liệu khám. Vui lòng bấm <strong>"Tiến Hành Phân Tích & Chẩn Đoán"</strong> để hệ thống đối chiếu 24 chỉ số.
          </td>
        </tr>
      `;
    }
    if (statNormalBadge) statNormalBadge.textContent = "✓ --/24 Đạt Chuẩn";
    if (statAbnormalBadge) statAbnormalBadge.textContent = "⚠️ --/24 Lệch Chuẩn";
    lastFeatureComparisons = [];
  });

  async function triggerDiagnosis() {
    btnSubmit.disabled = true;
    btnSubmit.innerHTML = `<span>⏳</span> ĐANG PHÂN TÍCH 24 CHỈ SỐ...`;

    // Thu thập 24 chỉ số
    const formData = new FormData(form);
    const payload = {};
    formData.forEach((val, key) => {
      payload[key] = val;
    });

    try {
      const response = await fetch("/api/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const resJson = await response.json();

      if (response.ok && resJson.status === "success") {
        renderClinicalDashboard(resJson.data, payload);
      } else {
        alert("Lỗi chẩn đoán y tế: " + (resJson.message || "Không xác định"));
      }
    } catch (err) {
      alert("Lỗi kết nối máy chủ HUIT Hospital API: " + err.message);
    } finally {
      btnSubmit.disabled = false;
      btnSubmit.innerHTML = `<span>⚡</span> TIẾN HÀNH PHÂN TÍCH & CHẨN ĐOÁN (AI DIAGNOSIS)`;
    }
  }

  // ==========================================
  // 9. RENDER KẾT QUẢ, BIỂU ĐỒ, XAI & ĐƠN THUỐC
  // ==========================================
  function renderClinicalDashboard(data, inputPayload) {
    const isCKD = data.prediction === 1;
    const probPct = (data.probability_ckd * 100).toFixed(1);
    const egfr = data.egfr || 90.0;
    const egfrStage = data.egfr_stage || "G1";

    // 1. CẬP NHẬT 4 THẺ KPI TRÊN ĐẦU TRANG
    if (kpiProbVal) {
      kpiProbVal.textContent = `${probPct.replace(".", ",")}%`;
      kpiProbVal.className = `kpi-large-num ${isCKD ? "text-danger" : "text-success"}`;
    }
    if (kpiProbSub) {
      kpiProbSub.textContent = isCKD ? "Nguy cơ bệnh thận mãn tính cao" : "Ngưỡng xác suất an toàn";
    }

    if (kpiEgfrVal) {
      kpiEgfrVal.textContent = egfr.toFixed(1).replace(".", ",");
    }
    if (kpiEgfrSub) {
      kpiEgfrSub.textContent = `${egfrStage} (${data.kdigo_stage ? data.kdigo_stage.description : "Chức năng lọc"})`;
    }

    if (kpiRankVal) {
      kpiRankVal.textContent = isCKD ? (egfr < 30 ? "Nguy Cơ Rất Cao" : "Nguy Cơ Cao") : "Bình Thường";
      kpiRankVal.className = `kpi-large-num-text ${isCKD ? "text-danger" : "text-success"}`;
    }

    if (kpiStatusPill) {
      if (isCKD) {
        kpiStatusPill.textContent = `⚠️ CẢNH BÁO ${egfrStage.split(" ")[0]}`;
        kpiStatusPill.className = "status-badge-pill pill-danger";
      } else {
        kpiStatusPill.textContent = "✓ KHỎE MẠNH (G1)";
        kpiStatusPill.className = "status-badge-pill pill-success";
      }
    }

    // 2. KHỐI KẾT QUẢ BÊN PHẢI
    if (emptyResultBox) emptyResultBox.classList.add("hidden");
    if (activeResultBox) activeResultBox.classList.remove("hidden");

    if (!riskGaugeChart) initRiskGaugeChart();
    if (!biomarkerRadarChart) initBiomarkerRadarChart();

    if (mainResultBanner && bannerIcon && bannerDiagnosisTitle) {
      if (isCKD) {
        mainResultBanner.className = "result-banner banner-danger";
        bannerIcon.textContent = "⚠️";
        bannerDiagnosisTitle.textContent = `BỆNH THẬN MÃN TÍNH (CKD - ${egfrStage.split(" ")[0]})`;
      } else {
        mainResultBanner.className = "result-banner banner-success";
        bannerIcon.textContent = "✓";
        bannerDiagnosisTitle.textContent = "BÌNH THƯỜNG (KHÔNG MẮC CKD)";
      }
    }

    if (recommendationBody) {
      recommendationBody.textContent = data.recommendation;
    }

    // 3. 🌟 CẬP NHẬT BỘ ĐÔI BIỂU ĐỒ GAUGE & RADAR
    updateVisualCharts(probPct, isCKD, inputPayload);

    // 4. HIỂN THỊ DANH SÁCH LÝ GIẢI XAI
    if (xaiFactorsList) {
      xaiFactorsList.innerHTML = "";
      if (data.xai_rationale && data.xai_rationale.length > 0) {
        data.xai_rationale.forEach((item) => {
          const li = document.createElement("li");
          li.textContent = item;
          xaiFactorsList.appendChild(li);
        });
      }
    }

    // 5. CẬP NHẬT BẢNG THAM CHIẾU SINH LÝ (NẾU CÓ)
    const scVal = parseFloat(inputPayload.sc || 0);
    if (refPatientSc) refPatientSc.textContent = `${scVal} mg/dL`;
    if (refStatusSc) {
      if (scVal > 1.4) {
        refStatusSc.textContent = "VƯỢT NGƯỠNG";
        refStatusSc.className = "badge-tag-red";
      } else {
        refStatusSc.textContent = "BÌNH THƯỜNG";
        refStatusSc.className = "badge-tag-green";
      }
    }

    const hemoVal = parseFloat(inputPayload.hemo || 15);
    if (refPatientHemo) refPatientHemo.textContent = `${hemoVal} g/dL`;
    if (refStatusHemo) {
      if (hemoVal < 12.0) {
        refStatusHemo.textContent = "THIẾU MÁU";
        refStatusHemo.className = "badge-tag-red";
      } else {
        refStatusHemo.textContent = "BÌNH THƯỜNG";
        refStatusHemo.className = "badge-tag-green";
      }
    }

    const alVal = parseFloat(inputPayload.al || 0);
    if (refPatientAl) refPatientAl.textContent = `${alVal} (${alVal >= 1 ? "+".repeat(Math.min(alVal, 4)) : "Âm tính"})`;
    if (refStatusAl) {
      if (alVal >= 1.0) {
        refStatusAl.textContent = "ĐẠM NIỆU";
        refStatusAl.className = "badge-tag-red";
      } else {
        refStatusAl.textContent = "BÌNH THƯỜNG";
        refStatusAl.className = "badge-tag-green";
      }
    }

    if (refPatientEgfr) refPatientEgfr.textContent = `${egfr} mL/min`;
    if (refStatusEgfr) {
      if (egfr < 60) {
        refStatusEgfr.textContent = egfrStage.split(" ")[0];
        refStatusEgfr.className = "badge-tag-red";
      } else {
        refStatusEgfr.textContent = "BÌNH THƯỜNG";
        refStatusEgfr.className = "badge-tag-green";
      }
    }

    // 5.5. CẬP NHẬT BẢNG ĐỐI CHIẾU 24 CHỈ SỐ LÂM SÀNG VỚI KHOẢNG CHUẨN NGƯỜI BÌNH THƯỜNG
    if (data.feature_comparisons && data.feature_comparisons.length > 0) {
      lastFeatureComparisons = data.feature_comparisons;
      renderBenchmarkTable(lastFeatureComparisons, currentBenchFilter);
      highlightFormInputsWithBenchmark(lastFeatureComparisons);
    }

    // 5.6. RENDER GIẢI TRÌNH CHUYÊN SÂU: "TẠI SAO CÓ KẾT QUẢ NÀY?" (CLINICAL XAI)
    renderDetailedXAI(data, inputPayload);

    // 6. CẬP NHẬT ĐƠN THUỐC
    renderPrescription(isCKD, egfr, inputPayload);

    // 7. CẬP NHẬT DỮ LIỆU IN PHIẾU KHÁM
    preparePrintSheet(data, inputPayload);
  }

  // ==========================================
  // 10. TẠO ĐƠN THUỐC LÂM SÀNG DỰA TRÊN TÌNH TRẠNG
  // ==========================================
  function renderPrescription(isCKD, egfr, payload) {
    if (!rxMedsList) return;
    rxMedsList.innerHTML = "";

    const mrn = (displayPatientMRN ? displayPatientMRN.textContent : "") || "BN-2026-0841";
    if (rxPrescriptionCode) {
      rxPrescriptionCode.textContent = `Mã Toa: DT-2026-${mrn.replace("BN-", "HUIT-")}`;
    }

    const meds = [];

    if (isCKD) {
      if (payload.htn === "yes" || parseFloat(payload.al || 0) >= 1) {
        meds.push({
          name: "Losartan Potassium (Cozaar)",
          dose: "50 mg",
          usage: "Uống 1 viên vào mỗi buổi sáng sau ăn",
          purpose: "Hạ áp, giảm áp lực mao mạch cầu thận & đạm niệu"
        });
      }

      meds.push({
        name: "Dapagliflozin (Forxiga)",
        dose: "10 mg",
        usage: "Uống 1 viên/ngày vào buổi sáng",
        purpose: "Bảo tồn chức năng lọc thận & giảm tiến triển CKD"
      });

      if (parseFloat(payload.hemo || 15) < 11.0 || payload.ane === "yes") {
        meds.push({
          name: "Sắt Polymaltose (Maltofer) + Acid Folic",
          dose: "100 mg",
          usage: "Uống 1 viên x 2 lần/ngày sau bữa ăn chính",
          purpose: "Bổ sung dự trữ sắt cho quá trình tạo hồng cầu"
        });
        if (parseFloat(payload.hemo || 15) < 9.0) {
          meds.push({
            name: "Erythropoietin Alfa (Epogin)",
            dose: "4000 IU",
            usage: "Tiêm dưới da 2 lần/tuần theo y lệnh bác sĩ",
            purpose: "Kích thích sinh hồng cầu điều trị thiếu máu do thận"
          });
        }
      }

      if (payload.pe === "yes") {
        meds.push({
          name: "Furosemide (Lasix)",
          dose: "40 mg",
          usage: "Uống 1 viên vào 08:00 sáng",
          purpose: "Lợi tiểu quai, giảm phù nề mu bàn chân & ứ trệ tuần hoàn"
        });
      }

      if (egfr < 30) {
        meds.push({
          name: "Natri Bicarbonat",
          dose: "500 mg",
          usage: "Uống 2 viên x 2 lần/ngày sau ăn",
          purpose: "Hiệu chỉnh toan chuyển hóa trong suy thận tiến triển"
        });
      }
    } else {
      meds.push({
        name: "Vitamin B-Complex + Kẽm (Zinc)",
        dose: "1 viên",
        usage: "Uống 1 viên/ngày vào buổi sáng",
        purpose: "Bổ sung vi chất, tăng cường chuyển hóa năng lượng"
      });
      meds.push({
        name: "Dung dịch bù nước Oresol hoặc Nước khoáng",
        dose: "2000 mL/ngày",
        usage: "Uống đều trong ngày",
        purpose: "Duy trì đủ thể tích tuần hoàn và bảo vệ chức năng thận khỏe mạnh"
      });
    }

    meds.forEach(m => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td><strong>${m.name}</strong></td>
        <td><code>${m.dose}</code></td>
        <td>${m.usage}</td>
        <td><small style="color: #475569;">${m.purpose}</small></td>
      `;
      rxMedsList.appendChild(tr);
    });
  }

  // ==========================================
  // 11. CHUẨN BỊ PHIẾU IN KHÁM BỆNH (@media print)
  // ==========================================
  function preparePrintSheet(data, inputPayload) {
    const printMrnDisplay = document.getElementById("printMrnDisplay");
    const printDateDisplay = document.getElementById("printDateDisplay");
    const printName = document.getElementById("printName");
    const printAge = document.getElementById("printAge");
    const printGender = document.getElementById("printGender");
    const printBHYT = document.getElementById("printBHYT");
    const printBed = document.getElementById("printBed");
    const printDoctor = document.getElementById("printDoctor");
    const printLabTableBody = document.getElementById("printLabTableBody");
    const printDiagSummary = document.getElementById("printDiagSummary");
    const printMedsBody = document.getElementById("printMedsBody");

    const todayStr = new Date().toLocaleDateString("vi-VN");

    if (printMrnDisplay) printMrnDisplay.textContent = `Mã Hồ Sơ: ${displayPatientMRN ? displayPatientMRN.textContent : ""}`;
    if (printDateDisplay) printDateDisplay.textContent = `Ngày lập: ${todayStr}`;
    if (printName) printName.textContent = patientName.value;
    if (printAge) printAge.textContent = `${inputPayload.age} tuổi`;
    if (printGender) printGender.textContent = patientGender.value === "male" ? "Nam" : "Nữ";
    if (printBHYT) printBHYT.textContent = patientBHYT.value;
    if (printBed) printBed.textContent = patientBed.value;
    if (printDoctor) printDoctor.textContent = patientDoctor.value;

    if (printLabTableBody) {
      printLabTableBody.innerHTML = `
        <tr>
          <td><strong>Serum Creatinine (sc)</strong></td>
          <td>${inputPayload.sc} mg/dL</td>
          <td>0.6 - 1.2 mg/dL</td>
          <td><strong>${parseFloat(inputPayload.sc) > 1.2 ? "VƯỢT NGƯỠNG (BẤT THƯỜNG)" : "Bình thường"}</strong></td>
        </tr>
        <tr>
          <td><strong>Hemoglobin (hemo)</strong></td>
          <td>${inputPayload.hemo} g/dL</td>
          <td>12.0 - 16.0 g/dL</td>
          <td><strong>${parseFloat(inputPayload.hemo) < 12.0 ? "THIẾU MÁU" : "Bình thường"}</strong></td>
        </tr>
        <tr>
          <td><strong>Albumin Nước Tiểu (al)</strong></td>
          <td>${inputPayload.al} (Độ đạm niệu)</td>
          <td>0.0 (Âm tính)</td>
          <td><strong>${parseFloat(inputPayload.al) >= 1.0 ? "ĐẠM NIỆU DƯƠNG TÍNH" : "Âm tính"}</strong></td>
        </tr>
        <tr>
          <td><strong>Mức Lọc Cầu Thận eGFR (MDRD)</strong></td>
          <td><strong>${(data.egfr || 90).toFixed(1)} mL/phút/1.73m²</strong></td>
          <td>&ge; 90 mL/phút</td>
          <td><strong>${data.egfr_stage || "G1"}</strong></td>
        </tr>
        <tr>
          <td><strong>Huyết Áp Khám (bp)</strong></td>
          <td>${inputPayload.bp} mmHg</td>
          <td>&le; 80 mmHg</td>
          <td>${parseInt(inputPayload.bp) > 80 ? "Tăng huyết áp" : "Bình thường"}</td>
        </tr>
        <tr>
          <td><strong>Đường Huyết (bgr)</strong></td>
          <td>${inputPayload.bgr} mg/dL</td>
          <td>70 - 110 mg/dL</td>
          <td>${parseFloat(inputPayload.bgr) > 126 ? "Tăng đường huyết" : "Bình thường"}</td>
        </tr>
      `;
    }

    if (printDiagSummary) {
      const isCKD = data.prediction === 1;
      const probPct = (data.probability_ckd * 100).toFixed(1);
      const stage = data.egfr_stage || "G1";

      printDiagSummary.innerHTML = `
        <p><strong>1. Chẩn đoán xác định:</strong> ${isCKD ? `Bệnh thận mãn tính (CKD) - Phân độ ${stage}` : "Chức năng thận trong giới hạn bình thường (Not CKD)"}.</p>
        <p><strong>2. Mức lọc cầu thận (eGFR MDRD):</strong> ${(data.egfr || 90).toFixed(1)} mL/phút/1.73m² (Xếp loại: ${stage}).</p>
        <p><strong>3. Xác suất tiên lượng AI Random Forest (Recall 98.0%):</strong> ${probPct}% nguy cơ suy thận.</p>
        <p><strong>4. Hướng xử trí:</strong> ${data.recommendation}</p>
      `;
    }

    if (printMedsBody && rxMedsList) {
      printMedsBody.innerHTML = "";
      const rows = rxMedsList.querySelectorAll("tr");
      rows.forEach((r, idx) => {
        const tds = r.querySelectorAll("td");
        if (tds.length >= 3) {
          const ptr = document.createElement("tr");
          ptr.innerHTML = `
            <td>${idx + 1}</td>
            <td><strong>${tds[0].textContent}</strong> (${tds[1].textContent})</td>
            <td>1 Hộp</td>
            <td>${tds[2].textContent}</td>
          `;
          printMedsBody.appendChild(ptr);
        }
      });
    }
  }

  // ==========================================
  // 12. RENDER GIẢI TRÌNH CHUYÊN SÂU: "TẠI SAO CÓ KẾT QUẢ NÀY?" (XAI)
  // ==========================================
  function renderDetailedXAI(data, payload) {
    const isCKD = data.prediction === 1;
    const xai = data.detailed_xai;
    if (!xai) return;

    // 1. Luận điểm tóm tắt của mô hình AI
    const xaiHeadlineBox = document.getElementById("xaiHeadlineBox");
    const xaiHeadlineText = document.getElementById("xaiHeadlineText");
    if (xaiHeadlineBox && xaiHeadlineText) {
      xaiHeadlineText.textContent = xai.summary_headline;
      if (isCKD) {
        xaiHeadlineBox.className = "xai-headline-box headline-danger";
      } else {
        xaiHeadlineBox.className = "xai-headline-box";
      }
    }

    // 2. Biểu đồ thanh đo trọng số tác động (Feature Impact Bars)
    const impactContainer = document.getElementById("xaiImpactBarsContainer");
    if (impactContainer && xai.all_ranked_factors) {
      impactContainer.innerHTML = "";
      xai.all_ranked_factors.slice(0, 6).forEach(f => {
        const item = document.createElement("div");
        item.className = "impact-bar-item";
        const isRisk = f.direction === "risk";
        item.innerHTML = `
          <div class="impact-bar-header">
            <div>
              <span class="impact-bar-name">${f.name}</span>
              <span class="impact-bar-val">(${f.val_str})</span>
            </div>
            <span class="impact-weight-tag ${isRisk ? 'tag-risk' : 'tag-safe'}">
              ${isRisk ? '▲ ' : '▼ '}${f.weight}% ${isRisk ? 'Đẩy Tới Bệnh Thận' : 'Bảo Vệ / An Toàn'}
            </span>
          </div>
          <div class="impact-bar-track">
            <div class="impact-bar-fill ${isRisk ? 'fill-risk' : 'fill-safe'}" style="width: ${Math.min(100, f.weight * 2.8)}%;"></div>
          </div>
          <div class="impact-reason-note">${f.reason}</div>
        `;
        impactContainer.appendChild(item);
      });
    }

    // 3. Quy trình 3 trụ cột KDIGO
    const pGStatus = document.getElementById("pillarGlomerularStatus");
    const pFStatus = document.getElementById("pillarFiltrationStatus");
    const pSStatus = document.getElementById("pillarSystemicStatus");

    const alNum = parseFloat(payload.al || 0);
    const rbcStr = String(payload.rbc || "normal").toLowerCase();
    if (pGStatus) {
      if (alNum >= 1.0 || rbcStr === "abnormal") {
        pGStatus.textContent = "⚠️ Màng Lọc Bị Tổn Thương (Đạm/Hồng Cầu Niệu)";
        pGStatus.className = "pillar-status status-danger";
      } else {
        pGStatus.textContent = "✓ Màng Lọc Cầu Thận Nguyên Vẹn";
        pGStatus.className = "pillar-status status-safe";
      }
    }

    const egfrNum = data.egfr || 90;
    if (pFStatus) {
      if (egfrNum < 60) {
        pFStatus.textContent = `⚠️ Suy Giảm Lọc eGFR ${egfrNum.toFixed(1)} (${data.egfr_stage.split(" ")[0]})`;
        pFStatus.className = "pillar-status status-danger";
      } else {
        pFStatus.textContent = `✓ Lọc Cầu Thận Bình Thường eGFR ${egfrNum.toFixed(1)} (G1)`;
        pFStatus.className = "pillar-status status-safe";
      }
    }

    if (pSStatus) {
      const hasSystemic = payload.htn === "yes" || payload.ane === "yes" || payload.pe === "yes" || payload.dm === "yes";
      if (hasSystemic) {
        pSStatus.textContent = "⚠️ Có Biến Chứng / Tiền Sử Bệnh Nền";
        pSStatus.className = "pillar-status status-danger";
      } else {
        pSStatus.textContent = "✓ Không Ghi Nhận Biến Chứng";
        pSStatus.className = "pillar-status status-safe";
      }
    }

    // 4. Các bước tính toán MDRD
    const mdrdList = document.getElementById("mdrdStepsList");
    if (mdrdList && xai.mdrd_calc_steps) {
      mdrdList.innerHTML = "";
      xai.mdrd_calc_steps.forEach(st => {
        const li = document.createElement("li");
        li.textContent = st;
        mdrdList.appendChild(li);
      });
    }
  }

  // ==========================================
  // 13. DATASET EXPLORER: KHO DỮ LIỆU GỐC 400 CA BỆNH ÁN
  // ==========================================
  const datasetTableBody = document.getElementById("datasetTableBody");
  const dsTotalBadge = document.getElementById("dsTotalBadge");
  const dsCkdBadge = document.getElementById("dsCkdBadge");
  const dsNotckdBadge = document.getElementById("dsNotckdBadge");
  const dsFilterBtns = document.querySelectorAll(".btn-ds-filter");
  const datasetSearchInput = document.getElementById("datasetSearchInput");
  const datasetPageSizeSelect = document.getElementById("datasetPageSizeSelect");
  const btnDsPrevPage = document.getElementById("btnDsPrevPage");
  const btnDsNextPage = document.getElementById("btnDsNextPage");
  const datasetPageCurrentDisplay = document.getElementById("datasetPageCurrentDisplay");
  const datasetPaginationInfo = document.getElementById("datasetPaginationInfo");

  let currentDsPage = 1;
  let currentDsPageSize = 15;
  let currentDsFilter = "all";
  let currentDsSearch = "";
  let totalDsPages = 1;
  let cachedDatasetRecords = [];

  async function fetchDatasetRecords() {
    if (!datasetTableBody) return;
    datasetTableBody.innerHTML = `<tr><td colspan="17" style="text-align: center; padding: 24px; color: #64748b;">⏳ Đang tải dữ liệu 400 ca bệnh án từ máy chủ...</td></tr>`;

    try {
      const url = `/api/dataset?page=${currentDsPage}&page_size=${currentDsPageSize}&classification=${currentDsFilter}&search=${encodeURIComponent(currentDsSearch)}`;
      const res = await fetch(url);
      const resJson = await res.json();

      if (res.ok && resJson.status === "success") {
        cachedDatasetRecords = resJson.records;
        const s = resJson.summary;
        const p = resJson.pagination;
        totalDsPages = p.total_pages;

        if (dsTotalBadge) dsTotalBadge.textContent = `📊 ${s.total_count} Mẫu Dữ Liệu`;
        if (dsCkdBadge) dsCkdBadge.textContent = `⚠️ ${s.ckd_count} Ca Bệnh Thận (${s.ckd_pct}%)`;
        if (dsNotckdBadge) dsNotckdBadge.textContent = `✓ ${s.notckd_count} Ca Khỏe Mạnh (${s.notckd_pct}%)`;

        if (datasetPageCurrentDisplay) datasetPageCurrentDisplay.textContent = `Trang ${p.current_page} / ${p.total_pages}`;
        if (datasetPaginationInfo) {
          const fromIdx = (p.current_page - 1) * p.page_size + 1;
          const toIdx = Math.min(p.current_page * p.page_size, p.total_records);
          datasetPaginationInfo.textContent = `Đang hiển thị ${p.total_records > 0 ? fromIdx : 0} - ${toIdx} trên tổng số ${p.total_records} ca bệnh án (Bộ lọc: ${currentDsFilter})`;
        }

        if (btnDsPrevPage) btnDsPrevPage.disabled = p.current_page <= 1;
        if (btnDsNextPage) btnDsNextPage.disabled = p.current_page >= p.total_pages;

        renderDatasetTable(cachedDatasetRecords);
      }
    } catch (err) {
      if (datasetTableBody) {
        datasetTableBody.innerHTML = `<tr><td colspan="17" style="text-align: center; padding: 20px; color: #dc2626;">Lỗi tải dữ liệu: ${err.message}</td></tr>`;
      }
    }
  }

  function renderDatasetTable(records) {
    if (!datasetTableBody) return;
    datasetTableBody.innerHTML = "";

    if (!records || records.length === 0) {
      datasetTableBody.innerHTML = `<tr><td colspan="17" style="text-align: center; padding: 24px; color: #64748b;">Không tìm thấy ca bệnh nào phù hợp với bộ lọc hiện tại.</td></tr>`;
      return;
    }

    records.forEach(r => {
      const tr = document.createElement("tr");
      const isCKD = String(r.classification).toLowerCase() === "ckd";
      const classBadge = isCKD
        ? `<span class="tag-label-ckd">⚠️ CKD (Bệnh)</span>`
        : `<span class="tag-label-notckd">✓ NOT CKD</span>`;

      tr.innerHTML = `
        <td><strong>#${r.id}</strong></td>
        <td>${r.age !== null ? r.age : '--'}</td>
        <td>${r.bp !== null ? r.bp : '--'}</td>
        <td>${r.sg !== null ? r.sg : '--'}</td>
        <td>${r.al !== null ? r.al : '--'}</td>
        <td>${r.su !== null ? r.su : '--'}</td>
        <td>${r.rbc !== null ? r.rbc : '--'}</td>
        <td>${r.bgr !== null ? r.bgr : '--'}</td>
        <td>${r.bu !== null ? r.bu : '--'}</td>
        <td><strong>${r.sc !== null ? r.sc : '--'}</strong></td>
        <td>${r.hemo !== null ? r.hemo : '--'}</td>
        <td>${r.htn !== null ? r.htn : '--'}</td>
        <td>${r.dm !== null ? r.dm : '--'}</td>
        <td>${r.pe !== null ? r.pe : '--'}</td>
        <td>${r.ane !== null ? r.ane : '--'}</td>
        <td>${classBadge}</td>
        <td style="text-align: center;">
          <button type="button" class="btn-ds-analyze" data-id="${r.id}" title="Nạp dữ liệu ca bệnh này và chẩn đoán ngay">
            <span>⚡</span> Phân Tích
          </button>
        </td>
      `;
      datasetTableBody.appendChild(tr);
    });

    // Gắn sự kiện cho các nút "Phân Tích"
    datasetTableBody.querySelectorAll(".btn-ds-analyze").forEach(btn => {
      btn.addEventListener("click", () => {
        const id = parseInt(btn.getAttribute("data-id"));
        const record = cachedDatasetRecords.find(item => item.id === id);
        if (record) {
          loadDatasetRecordToForm(record);
        }
      });
    });
  }

  function loadDatasetRecordToForm(r) {
    // 1. Cập nhật thông tin hành chính EMR
    if (displayPatientMRN) displayPatientMRN.textContent = `BN-RAW-${String(r.id).padStart(4, "0")}`;
    if (patientName) patientName.value = `Bệnh Nhân Mẫu #${r.id} (Dữ Liệu Gốc UCI)`;
    if (patientGender) patientGender.value = "male";
    if (patientBHYT) patientBHYT.value = `GD 4 79 ${String(r.id).padStart(10, "0")}`;
    if (patientBed) patientBed.value = `Khảo sát thực nghiệm #${r.id}`;
    if (patientContact) patientContact.value = `Bộ dữ liệu 400 mẫu • Khoa Học Dữ Liệu HUIT`;
    if (patientDoctor) patientDoctor.value = "BS. Vũ Thế Quang";

    // 2. Điền các chỉ số vào form (nếu r[key] là null thì điền giá trị trung vị mặc định)
    const defaults = {
      age: 50, bp: 80, sc: 1.0, bu: 30, bgr: 100, hemo: 14.0, pcv: 40, sod: 140, pot: 4.5, wc: 7500, rc: 4.5,
      sg: "1.020", al: "0.0", su: "0.0", rbc: "normal", pc: "normal", pcc: "notpresent", ba: "notpresent",
      htn: "no", dm: "no", cad: "no", appet: "good", pe: "no", ane: "no"
    };

    for (const key in defaults) {
      const el = document.getElementById(key);
      if (el) {
        if (r[key] !== null && r[key] !== undefined && r[key] !== "") {
          el.value = r[key];
        } else {
          el.value = defaults[key];
        }
      }
    }

    // 3. Cuộn mượt đến phần chẩn đoán
    const diagSec = document.getElementById("diagnosis-section");
    if (diagSec) {
      diagSec.scrollIntoView({ behavior: "smooth" });
    }

    // 4. Kích hoạt suy luận AI ngay lập tức
    triggerDiagnosis();
  }

  // Gắn sự kiện cho các điều khiển của Dataset Explorer
  if (dsFilterBtns) {
    dsFilterBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        dsFilterBtns.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentDsFilter = btn.getAttribute("data-dsfilter");
        currentDsPage = 1;
        fetchDatasetRecords();
      });
    });
  }

  if (datasetSearchInput) {
    let searchTimeout = null;
    datasetSearchInput.addEventListener("input", (e) => {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(() => {
        currentDsSearch = e.target.value.trim();
        currentDsPage = 1;
        fetchDatasetRecords();
      }, 300);
    });
  }

  if (datasetPageSizeSelect) {
    datasetPageSizeSelect.addEventListener("change", (e) => {
      const val = e.target.value;
      currentDsPageSize = val === "all" ? 400 : parseInt(val);
      currentDsPage = 1;
      fetchDatasetRecords();
    });
  }

  if (btnDsPrevPage) {
    btnDsPrevPage.addEventListener("click", () => {
      if (currentDsPage > 1) {
        currentDsPage--;
        fetchDatasetRecords();
      }
    });
  }

  if (btnDsNextPage) {
    btnDsNextPage.addEventListener("click", () => {
      if (currentDsPage < totalDsPages) {
        currentDsPage++;
        fetchDatasetRecords();
      }
    });
  }

  // Khởi động nạp dữ liệu bảng 400 ca bệnh án
  fetchDatasetRecords();

  // ==========================================
  // 14. WIRE PRINT BUTTONS
  // ==========================================
  function triggerPrint() {
    window.print();
  }

  if (sidebarBtnPrint) sidebarBtnPrint.addEventListener("click", triggerPrint);
  if (topbarBtnPrint) topbarBtnPrint.addEventListener("click", triggerPrint);
  if (btnOpenPrint) btnOpenPrint.addEventListener("click", triggerPrint);

  // Khởi động tự động nạp ca bệnh mẫu đầu tiên khi vừa mở trang Web
  setTimeout(() => {
    loadPatientData("BN-2026-0841");
  }, 250);
});
