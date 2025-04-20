function fetchStocksGraph() {
  fetch("http://localhost:8000/stock-graph")
    .then((res) => res.blob())
    .then((imageBlob) => {
      const imageElement = document.getElementById("stocksGraph");
      imageElement.src = URL.createObjectURL(imageBlob);
    });
}

function fetchPrice() {
  const tickerAndName = document.getElementById("tickerInput").value;
  const ticker = tickerAndName.split(":")[0];
  const name = tickerAndName.split(":")[1];

  fetch(`http://localhost:8000/${ticker}`)
    .then((res) => res.json())
    .then((data) => {
      document.getElementById(
        "result"
      ).innerText = `Current price of ${name}: $${data.price}`;
    })
    .catch((err) => {
      console.error("Error fetching price:", err);
      document.getElementById("result").innerText = "Error fetching price.";
    });
}

function fetchStockGraph() {
  const tickerAndName = document.getElementById("tickerInput").value;
  console.log(tickerAndName);
  const ticker = tickerAndName.split(":")[0];
  fetch(`http://localhost:8000/${ticker}-stock-graph`)
    .then((res) => res.blob())
    .then((imageBlob) => {
      const imageElement = document.getElementById("stockGraph");
      imageElement.src = URL.createObjectURL(imageBlob);
    });
}


function sendTradeInput() {
  const tickerAndName = document.getElementById("tickerInput").value;
  const ticker = tickerAndName.split(":")[0];
  const name = tickerAndName.split(":")[1];
  const action = document.getElementById("actionInput").value;
  const quantity = document.getElementById("quantityInput").value;
  fetch("http://localhost:8000/trade", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      ticker: ticker,
      name: name,
      quantity: quantity,
      action: action,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("tradeConfirmation").innerText = data.message;
    })
    .catch((err) => console.error("Error:", err));
}

// Ticker select
function populateTickers() {
    fetch("http://localhost:8000/tickers")
    .then((res) => res.json())
    .then((tickers) => {
      console.log(tickers);
      const select = document.getElementById("tickerInput");
      tickers.forEach((ticker) => {
        const option = document.createElement("option");
        option.value = ticker;
        option.text = ticker;
        select.appendChild(option);
      });
    })
    .catch((err) => console.error("Error fetching tickers:", err));
}

window.onload = function() {
    populateTickers()
    setInterval(fetchStocksGraph, 1000);
    setInterval(fetchStockGraph, 500);
    const sendTradeInputButton = document.getElementById("sendTradeInputButton");
    sendTradeInputButton.addEventListener("click", () => {sendTradeInput()})
    const fetchPriceButton = document.getElementById("fetchPriceButton");
    fetchPriceButton.addEventListener("click", () => {
        fetchPrice()
        fetchStockGraph()
    })
};