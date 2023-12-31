function addProductToOrder(productId) {
  const productCount = $("#product-count").val() || 1;

  $.get(
    "/order/add-to-order?product_id=" + productId + "&count=" + productCount
  ).then((res) => {
    Swal.fire({
      title: "اعلان",
      text: res.text,
      icon: res.icon,
      showCancelButton: false,
      confirmButtonColor: "#3085d6",
      confirmButtonText: res.confirm_button_text,
    }).then((result) => {
      if (result.isConfirmed && res.status === "not_auth") {
        window.location.href = "/accounts/login/";
      } else {
        location.reload();
      }
    });
  });
}
function fillPage(page) {
  $("#page").val(page);
  $("#filter_form").submit();
}

document.addEventListener("DOMContentLoaded", function () {
  var priceSlider = document.getElementById("price-slider");
  var priceRange = document.getElementById("price-range");
  var url = new URL(window.location.href);
  var urlParams = new URLSearchParams(url.search);
  var min = urlParams.get("min_price");
  var max = urlParams.get("max_price");
  if (min | max) {
    noUiSlider.create(priceSlider, {
      start: [min, max],
      connect: true,
      range: {
        min: 0,
        max: maxPrice,
      },
    });
  } else {
    noUiSlider.create(priceSlider, {
      start: [0, maxPrice],
      connect: true,
      range: {
        min: 0,
        max: maxPrice,
      },
    });
  }

  // بروزرسانی مقدار نمایشی برای محدوده
  priceSlider.noUiSlider.on("update", function (values, handle) {
    var min = values[0];
    var max = values[1];
    priceRange.innerHTML = formatCurrency(min, max);
  });

  // تابع فرمت کردن اعداد به فرمت پولی
  function formatCurrency(min, max) {
    return parseFloat(min).toFixed() + "    _     " + parseFloat(max).toFixed();
  }

  // رویداد set برای ارسال به سمت بک‌اند
  priceSlider.noUiSlider.on("set", function (values, handle) {
    var minPrice = parseFloat(values[0]).toFixed();
    var maxPrice = parseFloat(values[1]).toFixed();
    window.location.href = "?min_price=" + minPrice + "&max_price=" + maxPrice;
  });
});

function removeOrderDetail(detailId) {
  $.get("/order/shopping-cart?detail_id=" + detailId).then((res) => {
    // if (res.status === 'success') {
    location.reload();
    console.log("yesss");

    // }
  });
}
function changeCount(detailId) {
  id = 'quantity'+detailId
  var quantity = document.getElementById(id).value;
  $.get(
    "/order/shopping-cart?quantity=" + quantity + "&detail_id=" + detailId
  ).then((res) => {
    location.reload();
  });
}

function update_states() {
  fetch("/static/js/state.js")
    .then((response) => response.json())
    .then((data) => {
      var stateselect = document.getElementById("id_state");
      stateselect.innerHTML = "";
      data.forEach((state) => {
        var option = document.createElement("option");
        option.value = state.id;
        option.text = state.name;
        stateselect.appendChild(option);
      })

    })
    .catch((error) => console.error("Error fetching data:", error));

  
}

function update_city() {
  var id_state = $("#id_state").val();
  fetch("/static/js/city.js")
    .then((response) => response.json())
    .then((data) => {
      const filteredData = data.filter(
        (item) => item.province_id === parseInt(id_state)
      );
      // در اینجا می‌توانید با داده‌های خوانده شده اقدامات لازم را انجام دهید
      console.log(filteredData);
      var citySelect = document.getElementById("id_city");
      
      // پاک کردن گزینه‌های قبلی از select
      citySelect.innerHTML = "";

      // اضافه کردن گزینه‌های جدید به select
      filteredData.forEach((city) => {
        var option = document.createElement("option");
        option.value = city.id;
        option.text = city.name;
        citySelect.appendChild(option);
      });
    })
    .catch((error) => console.error("Error fetching data:", error));
  
}

