function filterSafeDeliveries(deliveryQueue) {
    return deliveryQueue
        .filter(order => order.baha === false)
        .map(order => `IPADALA: Order #${order.orderId} para kay ${order.kustomer} sa ${order.lugar}`);
}

const deliveryQueue = [
    { orderId: 101, kustomer: "Syron", lugar: "España", baha: true },
    { orderId: 102, kustomer: "Leomel", lugar: "BGC", baha: false },
    { orderId: 103, kustomer: "Reinier", lugar: "Taft Avenue", baha: true },
    { orderId: 104, kustomer: "Paul", lugar: "Makati Legazpi", baha: false },
    { orderId: 105, kustomer: "Tharen", lugar: "Araneta Avenue", baha: true },
    { orderId: 106, kustomer: "Eduard", lugar: "Ortigas Center", baha: false }
];

const dispatchList = filterSafeDeliveries(deliveryQueue);

console.log(dispatchList);